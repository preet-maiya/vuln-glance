from flask import Flask

import config

app = Flask(__name__)
base_route = f"{config.api_version}"


@app.route(f"/")
def hello():
    return "<h1>haveibeenpwned Service</h1><p> Use a valid endpoint </p>"


if __name__ == "__main__":
    app.run(port=config.PORT, host=config.HOST)
