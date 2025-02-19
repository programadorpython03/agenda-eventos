from src.models.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Eventos_link(Base):
    __tablename__ = "Eventos_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer, ForeignKey("Eventos.id"), nullable=False)
    inscrito_id = Column(Integer, ForeignKey("Inscritos.id"), nullable=False)
    link = Column(String, max_length=100, nullable=False)

    def __repr__(self):
        return f"Eventos_link(id={self.id}, evento_id={self.evento_id}, inscrito_id={self.inscrito_id}, link={self.link})"
