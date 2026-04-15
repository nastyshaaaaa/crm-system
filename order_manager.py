# order_manager.py (фрагмент)
from typing import Dict, List, Optional
from models import Order, OrderStatus

class OrderManager:
    def __init__(self):
        self._next_id = 1
        self._orders: Dict[int, Order] = {}

    def create_order(self, owner_id: str, client_name: str, description: str, amount: float) -> Order:
        if not description:
            raise ValueError("Описание не может быть пустым")
        order = Order(self._next_id, client_name, description, amount, owner_id=owner_id)
        self._orders[self._next_id] = order
        self._next_id += 1
        return order

    def get_orders_by_owner(self, owner_id: str) -> List[Order]:
        return [o for o in self._orders.values() if o.owner_id == owner_id]

    def get_order(self, order_id: int, owner_id: str) -> Optional[Order]:
        order = self._orders.get(order_id)
        if order and order.owner_id == owner_id:
            return order
        return None

    def update_order_status(self, order_id: int, owner_id: str, new_status: OrderStatus) -> None:
        order = self.get_order(order_id, owner_id)
        if not order:
            raise KeyError(f"Заказ {order_id} не найден или доступ запрещён")
        order.status = new_status

    def delete_order(self, order_id: int, owner_id: str) -> None:
        order = self.get_order(order_id, owner_id)
        if order:
            del self._orders[order_id]
