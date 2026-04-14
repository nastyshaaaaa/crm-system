import pytest
from client_manager import ClientManager
from order_manager import OrderManager

@pytest.fixture
def client_manager():
    """Фикстура: пустой ClientManager."""
    return ClientManager()

@pytest.fixture
def order_manager():
    """Фикстура: пустой OrderManager."""
    return OrderManager()

@pytest.fixture
def manager_with_one_client(client_manager):
    """ClientManager с одним клиентом."""
    client_manager.add_client("Иван Петров", "ivan@example.com")
    return client_manager
