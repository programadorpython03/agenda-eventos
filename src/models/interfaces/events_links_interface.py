from src.models.entities.eventos_link import Eventos_link
from abc import ABC, abstractmethod

class EventsLinksRepositoryInterface(ABC):
    @abstractmethod
    def insert_event_link(self, event_id: int, subscriber_id: int) -> str:
        pass

    def select_events_link(self, event_id: int, subscriber_id: int) -> Eventos_link:
        pass  