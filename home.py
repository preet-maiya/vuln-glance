import requests
import json
from flask import *

from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def home():
    #return parse_json
    return render_template('home.html')

# @app.route('/recentcves', methods=["GET","POST"])
# def recent_cve():
#     if request.method == "POST":
#         response_API = requests.get('https://cve.circl.lu/api/last')
#         data = response_API.text
#         parse_json = json.loads(data)
#         columns=["id","summary"]
#         header=["Vulnerability","Summary"]
#     #return parse_json
#         return render_template('first.html',data=parse_json,colnames=columns,header=header) 


if __name__=='__main__':
    app.run()
