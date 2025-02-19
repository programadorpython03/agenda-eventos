from src.models.interfaces.subscribers_repository_interface import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersCreator:
    def __init__(self, subscribers_repository: SubscribersRepositoryInterface):
        self.__subscribers_repository = subscribers_repository

    def create_subscriber(self, http_request: HttpRequest) -> HttpResponse:
        subscriber_info = http_request.body["data"]
        subscriber_email = subscriber_info["email"]
        subscriber_event_id = subscriber_info["evento_id"]
        
        self.__check_subscriber(subscriber_email, subscriber_event_id)
        self.__insert_subscriber(subscriber_info)

        return self.__format_response(subscriber_info)
    
    def __check_subscriber(self, subscriber_email: str, subscriber_event_id: int) -> bool:
        response = self.__subscribers_repository.select_subscriber(subscriber_email, subscriber_event_id)
        if response: raise Exception("Subscriber already exists")

    def __insert_subscriber(self, subscriber_info: dict) -> None:
        self.__subscribers_repository.insert_subscriber(subscriber_info)
    
    def __format_response(self, subscriber_info: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "Subscriber",
                    "count": 1,
                    "attributes": subscriber_info
                }
            },
            status_code=201
         )
