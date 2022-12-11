from flask import Flask, request, jsonify, make_response
import logging
from db_models import db
from helpers import get_breached_account_details

import config

base_route = f"{config.api_version}"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = config.postgres_connection_string
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def hello():
    return "<h1>haveibeenpwned Service</h1><p> Use a valid endpoint </p>"

@app.route(f"{base_route}/pwned")
def is_pwned():
    email = request.args.get("email")

    if email is None:
        logging.debug(f"email not provided")
        return make_response(jsonify({"message": "Email not provided"}), 400)

    breached_sites = get_breached_account_details(email)
    return make_response(jsonify({"breached_sites": breached_sites}))


if __name__ == "__main__":
    app.run(port=config.PORT, host=config.HOST)
