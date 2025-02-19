from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.interfaces.events_links_interface import EventsLinksRepositoryInterface

class EventsLinkCreator:
    def __init__(self, events_link_repository: EventsLinksRepositoryInterface):
        self.__events_link_repository = events_link_repository

    def create_events_link(self, http_request: HttpRequest) -> HttpResponse:
        event_link_info = http_request.body["data"]
        event_id = event_link_info["event_id"]
        subscriber_id = event_link_info["subscriber_id"]

        self.__check_events_link(event_id, subscriber_id)
        new_link = self.__create_events_link(event_id, subscriber_id)
        return self.__format_response(new_link, event_id, subscriber_id)

    def __check_events_link(self, event_id: int, subscriber_id: int) -> bool:
        response = self.__events_link_repository.select_events_link(event_id, subscriber_id)
        if response: raise Exception("Events link already exists")
  
    def __create_events_link(self, event_id: int, subscriber_id: int) -> str:
        new_link = self.__events_link_repository.insert_events_link(event_id, subscriber_id)
        return new_link
    
    def __format_response(self, new_link: str, event_id: int, subscriber_id: int) -> HttpResponse: 
        return HttpResponse(
            body={
                "data": {
                    "type": "EventsLink",
                    "count": 1,
                    "attributes": {
                        "event_id": event_id,
                        "subscriber_id": subscriber_id,
                        "link": new_link
                    }
                }
            },
            status_code=201
        )
  