from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.controlles.subscribers_controllers.subscribers_creator import SubscribersCreator
from src.validators.subscriber_creator_validator import subscribers_creator_validator
from src.models.repositories.subscribers_repository import SubscribersRepository
from src.controlles.subscribers_controllers.subscribers_manager import SubscribersManager


subscriber_route_bp = Blueprint("subscriber_route", __name__)

@subscriber_route_bp.route("/subscriber", methods=["POST"])
def create_new_subscriber():
    subscribers_creator_validator(request)

    http_request = HttpRequest(body=request.json)

    subscribers_repository = SubscribersRepository()
    subscribers_creator = SubscribersCreator(subscribers_repository)

    http_response = subscribers_creator.create_subscriber(http_request)

    return jsonify(http_response.body), http_response.status_code

@subscriber_route_bp.route("/subscriber/link/<link>/event/<event_id>", methods=["GET"])
def subscriber_by_link(link, event_id): 
    subscribers_repository = SubscribersRepository()
    subscribers_manager = SubscribersManager(subscribers_repository)

    http_request = HttpRequest(params={"link": link, "event_id": event_id})
    http_response = subscribers_manager.get_subscriber_by_link(http_request)

    return jsonify(http_response.body), http_response.status_code

@subscriber_route_bp.route("/subscriber/ranking/<event_id>", methods=["GET"])
def link_ranking(event_id):
    subscribers_repository = SubscribersRepository()
    subscribers_manager = SubscribersManager(subscribers_repository)

    http_request = HttpRequest(params={"event_id": event_id})
    http_response = subscribers_manager.get_event_ranking(http_request)

    return jsonify(http_response.body), http_response.status_code