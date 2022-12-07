import requests
import json
from flask import *

from flask import Flask,render_template
app=Flask(__name__)


@app.route('/recentcves')
def recent_cve():
    response_API = requests.get('https://cve.circl.lu/api/last')
    data = response_API.text
    parse_json = json.loads(data)
    columns=["id","summary"]
    header=["Vulnerability","Summary"]
    #return parse_json
    return render_template('first.html',data=parse_json,colnames=columns,header=header)


if __name__=='__main__':
    app.run()
