import pytest
from src.model.repositories.subscribers_repository import SubscribersRepository

@pytest.mark.skip("skipping test_insert_subscriber")
def test_insert_subscriber():
    subscriber_info = {
        'nome': 'João da Silva',
        'email': 'joao.silva@example.com',
        'evento_id': 1
    }

    subscribers_repository = SubscribersRepository()
    subscribers_repository.insert_subscriber(subscriber_info)

    assert subscribers_repository.select_subscriber(subscriber_info['email'], subscriber_info['evento_id']) == subscriber_info['email']

@pytest.mark.skip("skipping test_select_subscriber")
def test_select_subscriber():
    email = 'joao.silva@example.com'
    evento_id = 1

    subscribers_repository = SubscribersRepository()
    subscriber = subscribers_repository.select_subscriber(email, evento_id)
    print(subscriber.nome)
    
    assert subscriber.email == email
