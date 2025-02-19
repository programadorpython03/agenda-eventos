from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repositories.events_links_repository import EventsLinksRepository

class EventsLinkManager:
    def __init__(self, events_links_repository: EventsLinksRepository):
        self.events_links_repository = events_links_repository

    def get_events_links(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.params["event_id"]
        events_links = self.events_links_repository.select_events_links(event_id)
        return HttpResponse(status_code=200, body=events_links)

    def delete_events_link(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.params["event_id"]
        self.events_links_repository.delete_events_link(event_id)
        return HttpResponse(status_code=200, body={"message": "Event link deleted successfully"})

    def update_events_link(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.params["event_id"]
        self.events_links_repository.update_events_link(event_id)
        return HttpResponse(status_code=200, body={"message": "Event link updated successfully"}) 