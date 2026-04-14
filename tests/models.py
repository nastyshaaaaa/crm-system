"""Модели данных для CRM-системы."""
from dataclasses import dataclass
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

@dataclass
class Client:
    name: str
    email: str

    def __post_init__(self):
        if not self.name or not self.email:
            raise ValueError("Имя и email не могут быть пустыми")

@dataclass
class Order:
    id: int
    client_name: str
    description: str
    amount: float
    status: OrderStatus = OrderStatus.PENDING

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Сумма заказа должна быть положительной")
