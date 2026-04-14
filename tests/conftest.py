import pytest
from client_manager import ClientManager   # пока нет, напишем позже

@pytest.fixture
def client_manager():
    """Фикстура, возвращающая пустой ClientManager."""
    return ClientManager()

@pytest.fixture
def manager_with_one_client(client_manager):
    """Фикстура с одним предзаполненным клиентом."""
    client_manager.add_client("Иван Петров", "ivan@example.com")
    return client_manager
