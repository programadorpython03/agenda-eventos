from flask import Blueprint, jsonify, request
from src.controlles.events_link_controller.events_link_creator import EventsLinkCreator
from src.models.repositories.events_links_repository import EventsLinksRepository
from src.controlles.events_link_controller.events_link_manager import EventsLinkManager
from src.http_types.http_request import HttpRequest

events_links_route_bp = Blueprint("events_links_route", __name__)

@events_links_route_bp.route("/events_links", methods=["POST"])
def create_new_events_link():
    events_link_creator = EventsLinkCreator()
    events_links_repository = EventsLinksRepository()
    events_link_creator = EventsLinkCreator(events_links_repository)

    http_request = HttpRequest(body=request.json)
    http_response = events_link_creator.create_events_link(http_request)

    return jsonify(http_response.body), http_response.status_code

@events_links_route_bp.route("/events_links/<event_id>", methods=["GET"])
def get_events_links(event_id):
    events_links_repository = EventsLinksRepository()
    events_links_manager = EventsLinkManager(events_links_repository)

    http_request = HttpRequest(params={"event_id": event_id})
    http_response = events_links_manager.get_events_links(http_request)

    return jsonify(http_response.body), http_response.status_code

@events_links_route_bp.route("/events_links/<event_id>", methods=["DELETE"])
def delete_events_link(event_id):
    events_links_repository = EventsLinksRepository()
    events_links_manager = EventsLinkManager(events_links_repository)

    http_request = HttpRequest(params={"event_id": event_id})
    http_response = events_links_manager.delete_events_link(http_request)

    return jsonify(http_response.body), http_response.status_code

@events_links_route_bp.route("/events_links/<event_id>", methods=["PUT"])
def update_events_link(event_id):
    events_links_repository = EventsLinksRepository()
    events_links_manager = EventsLinkManager(events_links_repository)

    http_request = HttpRequest(params={"event_id": event_id})
    http_response = events_links_manager.update_events_link(http_request) 

    return jsonify(http_response.body), http_response.status_code 