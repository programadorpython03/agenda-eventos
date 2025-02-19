from flask import Blueprint, jsonify, request
from src.http_types.http_response import HttpResponse
from src.http_types.http_resquest import HttpRequest


event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    http_request = HttpRequest(body=request.json)



    http_response = HttpResponse(http_request.body, status_code=201)
    return jsonify(http_response.body), http_response.status_code