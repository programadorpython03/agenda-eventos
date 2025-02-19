import pytest
from src.models.repositories.events_repository import EventosRepository

@pytest.mark.skip("skipping test_insert_events")
def test_insert_events():
    event_name = "Evento de teste 2"
    eventos_repository = EventosRepository()
    eventos_repository.insert_evento(event_name)

    assert eventos_repository.select_events(event_name).nome == event_name

@pytest.mark.skip("skipping test_select_events")
def test_select_events():
    event_name = "Evento de teste 2"
    eventos_repository = EventosRepository()

    event = eventos_repository.select_events(event_name)

    assert event.nome == event_name
