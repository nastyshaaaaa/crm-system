import pytest
from client_manager import ClientManager

def test_add_client(client_manager):
    client_manager.add_client("Иван", "i@i.ru")
    assert "Иван" in client_manager.get_client_names()
    assert client_manager.get_client_email("Иван") == "i@i.ru"

def test_add_duplicate_client(client_manager):
    client_manager.add_client("Иван", "i@i.ru")
    with pytest.raises(ValueError, match="Клиент 'Иван' уже существует"):
        client_manager.add_client("Иван", "new@mail.ru")

def test_get_client_email_missing(client_manager):
    with pytest.raises(KeyError, match="Клиент 'Неизвестный' не найден"):
        client_manager.get_client_email("Неизвестный")

def test_update_client(client_manager):
    client_manager.add_client("Петр", "petr@old.com")
    client_manager.update_client("Петр", new_email="petr@new.com")
    assert client_manager.get_client_email("Петр") == "petr@new.com"

def test_delete_client(client_manager):
    client_manager.add_client("Анна", "anna@ex.com")
    client_manager.delete_client("Анна")
    assert "Анна" not in client_manager.get_client_names()
