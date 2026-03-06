from flask import Flask, send_file
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, world!")


schema = graphene.Schema(query=Query)

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


@app.route("/schema.gql", methods=["GET"])
def get_schema_gql():
    try:
        return send_file("schema.gql")
    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
