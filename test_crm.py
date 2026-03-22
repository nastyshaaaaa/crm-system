# test_crm.py
import pytest
from crm import ClientManager

def test_add_client():
    # Создаём менеджер клиентов
    manager = ClientManager()
    
    # Добавляем клиента
    manager.add_client("Иван Петров", "ivan@example.com")
    
    # Проверяем, что клиент появился в списке
    assert "Иван Петров" in manager.get_clients()
    
    # Проверяем, что email сохранился
    assert manager.get_client_email("Иван Петров") == "ivan@example.com"

def test_add_duplicate_client():
    # Проверяем, что при повторном добавлении возникает ошибка
    manager = ClientManager()
    manager.add_client("Иван Петров", "ivan@example.com")
    
    with pytest.raises(ValueError, match="Клиент Иван Петров уже существует"):
        manager.add_client("Иван Петров", "new@example.com")
