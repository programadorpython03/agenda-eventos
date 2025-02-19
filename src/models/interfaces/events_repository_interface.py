from src.models.entities.eventos import Eventos
from abc import ABC, abstractmethod

class EventsRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_event(self, nome: str) -> None: pass
    
    @abstractmethod
    def select_events(self, name: str) -> Eventos: pass