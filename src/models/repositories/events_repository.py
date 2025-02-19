from src.models.entities.eventos import Eventos
from src.models.configs.connection import DBConnectionHandler
from src.models.interfaces.events_repository_interface import EventsRepositoryInterface

class EventsRepository(EventsRepositoryInterface):
    def insert_event(self, nome: str) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_evento = Eventos(nome=nome)
                db_connection.session.add(new_evento)
                db_connection.session.commit()
            except Exception as e:
                db_connection.session.rollback()
                raise Exception(e)
    
    def select_events(self, name: str) -> Eventos:
        with DBConnectionHandler() as db_connection:
            try:
                '''
                data = (
                    db_connection.session
                    .query(Eventos)
                    .filter(Eventos.nome == name)
                    .one_or_none()
                )
                '''
                query = db_connection.session.query(Eventos).filter(Eventos.nome == name).first()
                return query
            except Exception as e:
                raise Exception(e)