import json
from flask import Flask, request, jsonify, make_response
import config
from helpers import create_new_user, user_login, user_logout, check_userinfo

app = Flask(__name__)
base_route = f"/{config.api_version}"


@app.route(f"/")
def hello():
    return "<h1>haveibeenpwned Service</h1><p> Use a valid endpoint </p>"

@app.route(f"{base_route}/create_user", methods=["POST"])
def create_user():
    user_data = request.json
    # TODO: Add check for email and password present
    create_new_user(user_data["username"], user_data["password"])
    return jsonify({"message": "user created"})

@app.route(f"{base_route}/login", methods=["POST"])
def login():
    user_data = request.json
    token = user_login(user_data["username"], user_data["password"])
    resp = make_response(jsonify({"message": "logged in successfully"}), 200)
    for key, value in token.items():
        resp.set_cookie(key, json.dumps(value))
    resp.set_cookie("auth_token", json.dumps(token))
    return resp

@app.route(f"{base_route}/logout")
def logout():
    token = request.json()["token"]
    user_logout(token)
    return jsonify({"message": "logged out"})

@app.route(f"{base_route}/userinfo")
def userinfo():
    access_token = request.cookies.get("access_token")
    refresh_token = request.cookies.get("refresh_token")
    # token = request.cookies.get("auth_token")
    # print(token)
    # token = token.replace("\"", "'")
    # print(token)
    # token = json.loads(token)
    auth_token = {"access_token": access_token, "refresh_token": refresh_token}
    print(auth_token)
    valid = check_userinfo(auth_token)
    return jsonify({"authorized": valid})


if __name__ == "__main__":
    app.run(port=config.PORT, host=config.HOST)