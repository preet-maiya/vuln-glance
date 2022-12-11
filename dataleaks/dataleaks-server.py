import requests
import json
from flask import *

from flask import Flask,render_template
app=Flask(__name__)


@app.route('/dataleaks',methods=["GET","POST"])
def recent_cve():
    if request.method == "POST":
        response_API = requests.get('https://haveibeenpwned.com/api/v2/breach/Adobe')
        data = response_API.text
        parse_json = json.loads(data)
    #print(parse_json)
        columns=["Name","Domain","BreachDate","PwnCount","Description","DataClasses"]
        header=["Company Name","Breach Date","Count","Description","Data Classes"]
    #return parse_json
        return render_template('first.html',data=parse_json,colnames=columns,header=header)


if __name__=='__main__':
    app.run()
