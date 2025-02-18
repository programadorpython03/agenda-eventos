from src.model.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Inscritos(Base):
    __tablename__ = "Inscritos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer, ForeignKey("Eventos.id"), nullable=False)
    nome = Column(String, nullable=False, max_length=100)
    email = Column(String, nullable=False, max_length=100)
    link = Column(String, max_length=255)

    def __repr__(self):
        return f"Inscritos(id={self.id}, nome={self.nome}, email={self.email}, link={self.link}, evento_id={self.evento_id})"
  