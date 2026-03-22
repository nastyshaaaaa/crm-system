# test_crm.py
import pytest
from crm import ClientManager   # импортируйте ваш класс/функцию

def test_add_client():
    # создаём менеджер клиентов
    manager = ClientManager()
    
    # добавляем клиента
    manager.add_client("Иван Петров", "ivan@example.com")
    
    # проверяем, что клиент появился в списке
    assert "Иван Петров" in manager.get_clients()
    assert manager.get_client_email("Иван Петров") == "ivan@example.com"
