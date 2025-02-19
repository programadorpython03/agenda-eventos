from src.models.interfaces.events_repository_interface import EventsRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventsCreator:
    def __init__(self, events_repository: EventsRepositoryInterface):
        self.__events_repository = events_repository

    def create_event(self, http_request: HttpRequest) -> HttpResponse:
        events_info = http_request.body["data"]
        event_name = events_info["nome"]

        self.__check_events(event_name)
        self.__insert_event(event_name)

        return self.__format_response(event_name)


    def __check_events(self, event_name: str) -> bool:
        response = self.__events_repository.select_events(event_name)
        if response: raise Exception("Event already exists")
    
    def __insert_event(self, event_name: str) -> None:
        self.__events_repository.insert_event(event_name)

    def __format_response(self, event_name: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "Event",
                    "count": 1,
                    "attributes": {
                    "event_name": event_name
                    }
                }
            },
            status_code=201
         )
        
