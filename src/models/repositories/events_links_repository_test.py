import pytest
from src.models.repositories.events_links_repository import EventsLinksRepository

@pytest.mark.skip("Insert event link is not implemented")
def test_insert_event_link():
    events_links_repository = EventsLinksRepository()
    event_id = 1
    subscriber_id = 1
    link = events_links_repository.insert_event_link(event_id, subscriber_id)
    assert link is not None
    assert len(link) == 7

@pytest.mark.skip("Get rank subscriber is not implemented")
def test_rank_subscriber():
    events_links_repository = EventsLinksRepository()
    event_id = 1
    result = events_links_repository.get_rank_subscriber(event_id)
    print()

    for row in result:
        print(f'Link: {row.link} - Total de Inscritos: {row.Total_de_Inscritos}')
