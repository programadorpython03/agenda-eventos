from src.model.entities.eventos import Eventos
from abc import ABC, abstractmethod

class EventosRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_evento(self, nome: str) -> None: pass
    
    @abstractmethod
    def select_events(self, name: str) -> Eventos: pass