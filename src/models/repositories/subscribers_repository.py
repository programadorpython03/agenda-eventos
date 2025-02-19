from sqlalchemy import func, desc
from src.models.configs.connection import DBConnectionHandler
from src.models.entities.inscritos import Inscritos
from src.models.interfaces.subscribers_repository_interface import SubscribersRepositoryInterface


class SubscribersRepository(SubscribersRepositoryInterface):
    def insert_subscriber(self, subscriber_infos: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscriber = Inscritos(
                        nome=subscriber_infos.get("nome"),
                        email=subscriber_infos.get("email"),
                        link=subscriber_infos.get("link"),
                        evento_id=subscriber_infos.get("evento_id")
                    )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(
                    Inscritos.email == email,
                    Inscritos.evento_id == evento_id
                )
                .one_or_none()
            )

            return data
        
    def select_subscriber_by_link(self, link: str, event_id: int) -> list:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(
                    Inscritos.link == link,
                    Inscritos.evento_id == event_id
                )
                .all()
            )

            return data
        
    def get_rank_subscriber(self, event_id: int) -> list:
        with DBConnectionHandler() as db:
            result = (
                db.session
                .query(
                    Inscritos.email,
                    func.count(Inscritos.id).label("Total de Inscritos")
                )
                .filter(
                    Inscritos.evento_id == event_id,
                    Inscritos.link != None
                )
                .group_by(Inscritos.link)
                .order_by(desc("Total de Inscritos"))
                .all()
            )

            return result

