from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.controlles.subscribers_controllers.subscribers_creator import SubscribersCreator
from src.validators.subscriber_creator_validator import subscribers_creator_validator
from src.models.repositories.subscribers_repository import SubscribersRepository


subscriber_route_bp = Blueprint("subscriber_route", __name__)

@subscriber_route_bp.route("/subscriber", methods=["POST"])
def create_new_subscriber():
    subscribers_creator_validator(request)

    http_request = HttpRequest(body=request.json)

    subscribers_repository = SubscribersRepository()
    subscribers_creator = SubscribersCreator(subscribers_repository)

    http_response = subscribers_creator.create_subscriber(http_request)

    return jsonify(http_response.body), http_response.status_code
    