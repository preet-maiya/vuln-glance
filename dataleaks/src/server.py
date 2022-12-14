from flask import Flask, Response, render_template
from dateutil.relativedelta import relativedelta
from helpers import get_data
import config
import json
import psycopg2
import datetime
import traceback
import requests

app = Flask(__name__)
base_route = f"{config.api_version}"


@app.route(f"{base_route}/")
@app.route("/")
def hello():
    resp = {
        "validPaths": ["/v1/leaks","/v1/leaks/<num_years>"],
        "msg": "Recent data leaks Service. Use one of the mentioned valid endpoints",
        "version": config.api_version.strip("/")
    }
    return Response(response=json.dumps(resp), status=200, mimetype="application/json")

@app.route('/home')
def home():
    #return parse_json
    return render_template('home.html')

@app.route(f"{base_route}/recentcves", methods=["GET"])
def recent_cve():
    response_API = requests.get('https://cve.circl.lu/api/last')
    data = response_API.text
    parse_json = json.loads(data)
    columns=["id","summary"]
    header=["Vulnerability","Summary"]
    return render_template('recentcves.html',data=parse_json,colnames=columns,header=header)

@app.route(f"{base_route}/leaks", methods=["GET"], defaults={'years': None})
@app.route(f"{base_route}/leaks/<years>", methods=["GET"])
def get_recent_leaks(years=None):

    if years and not years.isdigit():
        err_resp = {"msg": "Enter valid number of years"}
        return Response(response=json.dumps(err_resp), status=400, mimetype="application/json")
    
    epoch_time = int((datetime.datetime.utcnow() - relativedelta(years=int(config.default_time))).timestamp())
    if years:
        epoch_time = int((datetime.datetime.utcnow() - relativedelta(years=int(years))).timestamp())
    
    query = config.get_query.replace("%s", str(epoch_time))
    resp = []
    try:
        conn = psycopg2.connect(host=config.psql_host, user=config.psql_user, password=config.psql_password, dbname=config.psql_dbname)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(f"Fetched a total of {len(results)} leaks")

        if len(results) == 0:
            resp = get_data()

        for result in results:
            resp.append(result[2])
        
        columns=config.resp_fields
        header=config.resp_fields

        return render_template('first.html',data=resp,colnames=columns,header=header, size=len(resp))

        # return Response(response=json.dumps(resp), status=200, mimetype="application/json")
    except Exception as ex:
        traceback.print_exc()
        err_resp = {"msg": "Failed to fetch the recent data leaks."}
        return Response(response=json.dumps(err_resp), status=500, mimetype="application/json")
    finally:
        conn.close()


if __name__ == "__main__":
    app.run(port=config.PORT, host=config.HOST)