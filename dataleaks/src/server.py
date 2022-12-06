from flask import Flask, Response
from dateutil.relativedelta import relativedelta
import config
import json
import psycopg2
import datetime
import traceback

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

@app.route(f"{base_route}/leaks", methods=["GET"], defaults={'years': None})
@app.route(f"{base_route}/leaks/<years>", methods=["GET"])
def get_recent_leaks(years=None):
    epoch_time = int((datetime.datetime.utcnow() - relativedelta(years=1)).timestamp())
    if years:
        epoch_time = int((datetime.datetime.utcnow() - relativedelta(years=int(years))).timestamp())
    
    query = config.get_query.replace("%s", str(epoch_time))
    resp = []
    try:
        conn = psycopg2.connect(host=config.psql_host, user=config.psql_user, password=config.psql_password)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(f"Fetched a total of {len(results)} leaks")
        for result in results:
            resp.append(result[2])
        return Response(response=json.dumps(resp), status=200, mimetype="application/json")
    except Exception as ex:
        traceback.print_exc()
        err_resp = {"msg": "Failed to fetch the recent data leaks."}
        return Response(response=json.dumps(err_resp), status=500, mimetype="application/json")
    finally:
        conn.close()

# def get_latest():
#     conn = psycopg2.connect(host="localhost", user="postgres", password="postgres")
#     cursor = conn.cursor()
#     for data in datas:
#         add_date = int(datetime.datetime.strptime(f'{data["BreachDate"]}', '%Y-%m-%d').timestamp())
#         insert_data = f'''INSERT INTO dataleaks (breach_epoch, leak_info) values ({add_date}, $${json.dumps(data)}$$);'''
#         cursor.execute(insert_data)
#     conn.commit()
#     conn.close()
#     datetime.datetime.strptime('2016-07-08T01:55:03Z', '%Y-%m-%dT%H:%M:%SZ').timestamp()
#     now=datetime.datetime.utcnow()
#     new_now = now - relativedelta(months=1)

if __name__ == "__main__":
    app.run(port=config.PORT, host=config.HOST)