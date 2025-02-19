from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.interfaces.subscribers_repository_interface import SubscribersRepositoryInterface

class SubscribersManager:
    def __init__(self, subscribers_repository: SubscribersRepositoryInterface):
        self.__subscribers_repository = subscribers_repository

    def get_subscriber_by_link(self, http_request: HttpRequest) -> HttpResponse:
        link = http_request.query_params["link"]
        event_id = http_request.query_params["event_id"]
        subscriber = self.__subscribers_repository.select_subscriber_by_link(link, event_id)
        return self.__format_response(subscriber)
    
    def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.query_params["event_id"]
        ranking = self.__subscribers_repository.get_event_ranking(event_id)
        return self.__format_ranking_response(ranking)
    
    def __format_ranking_response(self, event_ranking: list) -> HttpResponse:
        formatted_ranking = []
        for position in event_ranking:
            formatted_ranking.append({
                "email": position.email,
                "total": position.total,
            })

        return HttpResponse(
            body = {
                "data": {
                    "type": "Ranking",
                    "count": len(formatted_ranking),
                    "ranking": formatted_ranking
                }
            },
            status_code=200
        )
    
    def __format_response(self, subscribers: list) -> HttpResponse:
        formatted_subscriber = []
        for subscriber in subscribers:
            formatted_subscriber.append({
                "name": subscriber["name"],
                "email": subscriber["email"]
            })

        return HttpResponse(
            body = {
                "data": {
                    "type": "Subscribers",
                    "count": len(subscribers),
                    "subscribers": formatted_subscriber
                }
            },
            status_code=200
        )
