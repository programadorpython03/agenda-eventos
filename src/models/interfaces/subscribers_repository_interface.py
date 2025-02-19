from abc import ABC, abstractmethod
from src.models.entities.inscritos import Inscritos

class SubscribersRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_subscriber(self, subscriber_info: dict) -> None: pass
    
    @abstractmethod
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos: pass