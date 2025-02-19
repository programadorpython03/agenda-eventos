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

def test_select_events_link():
    events_links_repository = EventsLinksRepository()
    event_id = 1
    subscriber_id = 1
    link = events_links_repository.select_events_link(event_id, subscriber_id)

    assert link is not None
    assert link.evento_id == event_id
    assert link.inscrito_id == subscriber_id
    assert len(link.link) == 7
  