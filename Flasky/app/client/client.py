from client import client_api
from flask import Response
from flask import make_response

@client_api.route("/list/<user_id>")
def user_client_list():
    response = make_response({"asf": "asd"})
    return response
