import random
import string
from src.models.entities.eventos_link import Eventos_link
from src.models.configs.connection import DBConnectionHandler
from src.models.interfaces.events_links_interface import EventsLinksRepositoryInterface

class EventsLinksRepository(EventsLinksRepositoryInterface):
    def insert_event_link(self, event_id: int, subscriber_id: int) -> str:
        with DBConnectionHandler() as db_connection:
            try:
                final_link = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
                formated_link = f'evento-{event_id}-inscrito-{subscriber_id}-{final_link}'

                new_event_link = Eventos_link(evento_id=event_id, inscrito_id=subscriber_id, link=formated_link)

                db_connection.session.add(new_event_link)
                db_connection.session.commit()
                return formated_link
            except Exception as e:
                db_connection.session.rollback()
                raise Exception(e)
    
    def select_events_link(self, event_id: int, subscriber_id: int) -> Eventos_link:
        with DBConnectionHandler() as db_connection:
            try:
                query = db_connection.session.query(Eventos_link).filter(Eventos_link.evento_id == event_id, Eventos_link.inscrito_id == subscriber_id).one_or_none()
                return query
            except Exception as e:
                raise Exception(e)