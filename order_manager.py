"""Управление заказами (новый модуль)."""
from typing import Dict, List, Optional
from models import Order, OrderStatus

class OrderManager:
    def __init__(self) -> None:
        self._next_id = 1
        self._orders: Dict[int, Order] = {}

    def create_order(self, client_name: str, description: str, amount: float) -> Order:
        if not description:
            raise ValueError("Описание заказа не может быть пустым")
        order = Order(self._next_id, client_name, description, amount)
        self._orders[self._next_id] = order
        self._next_id += 1
        return order

    def get_order(self, order_id: int) -> Optional[Order]:
        return self._orders.get(order_id)

    def get_orders_by_client(self, client_name: str) -> List[Order]:
        return [o for o in self._orders.values() if o.client_name == client_name]

    def update_order_status(self, order_id: int, new_status: OrderStatus) -> None:
        if order_id not in self._orders:
            raise KeyError(f"Заказ {order_id} не найден")
        self._orders[order_id].status = new_status

    def delete_order(self, order_id: int) -> None:
        self._orders.pop(order_id, None)

    def get_all_orders(self) -> List[Order]:
        return list(self._orders.values())
