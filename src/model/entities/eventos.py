from src.model.configs.base import Base
from sqlalchemy import Column, Integer, String

class Eventos(Base):
    __tablename__ = "Eventos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    def __repr__(self):
        return f"Eventos(id={self.id}, nome={self.nome})"
