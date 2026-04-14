import pytest
from order_manager import OrderManager
from models import OrderStatus

def test_create_order(order_manager):
    order = order_manager.create_order("Иван", "Ноутбук", 50000)
    assert order.id == 1
    assert order.client_name == "Иван"
    assert order.status == OrderStatus.PENDING

def test_create_order_negative_amount(order_manager):
    with pytest.raises(ValueError, match="Сумма заказа должна быть положительной"):
        order_manager.create_order("Иван", "Мышь", -100)

def test_orders_by_client(order_manager):
    order_manager.create_order("Анна", "Книга", 1000)
    order_manager.create_order("Анна", "Ручка", 200)
    order_manager.create_order("Петр", "Стол", 8000)
    assert len(order_manager.get_orders_by_client("Анна")) == 2
    assert len(order_manager.get_orders_by_client("Петр")) == 1

def test_update_status(order_manager):
    order = order_manager.create_order("Ольга", "Телефон", 30000)
    order_manager.update_order_status(order.id, OrderStatus.COMPLETED)
    updated = order_manager.get_order(order.id)
    assert updated.status == OrderStatus.COMPLETED

def test_delete_order(order_manager):
    order = order_manager.create_order("Кирилл", "Наушники", 5000)
    order_manager.delete_order(order.id)
    assert order_manager.get_order(order.id) is None
