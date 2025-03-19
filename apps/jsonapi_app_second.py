from flask import Flask
from flask_smorest import Api, Blueprint

app = Flask(__name__)
app.config["API_TITLE"] = "JSON:API Example"
app.config["API_VERSION"] = "1"
app.config["OPENAPI_VERSION"] = "3.1"
api = Api(app)

blp = Blueprint("hello", __name__, url_prefix="/v2")


@blp.route("/<string:name>")
@blp.response(200)
def hello(name):
    return {"message": f"Hello, {name}!"}


api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
