from src.model.entities.inscritos import Inscritos
from src.model.configs.connection import DBConnectionHandler

class SubscribersRepository:
    def insert_subscriber(self, subscriber_info: dict) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_subscriber = Inscritos(
                    nome=subscriber_info['nome'],
                    email=subscriber_info['email'],
                    evento_id=subscriber_info['evento_id']
                )
                db_connection.session.add(new_subscriber)
                db_connection.session.commit()
            except Exception as e:
                db_connection.session.rollback()
                raise Exception(e)
            
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
        with DBConnectionHandler() as db_connection:
            try:
                '''
                data = (
                    db_connection.session
                    .query(Inscritos)
                    .filter(
                      Inscritos.email == email,
                      Inscritos.evento_id == evento_id
                    )
                    .one_or_none()
                )
                '''
                subscriber = db_connection.session.query(Inscritos).filter(Inscritos.email == email, Inscritos.evento_id == evento_id).first()
                return subscriber
            except Exception as e:
                raise Exception(e)