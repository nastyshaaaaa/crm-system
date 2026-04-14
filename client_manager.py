"""Управление клиентами (рефакторинг старого crm.py)."""
from typing import Dict, List, Optional
from models import Client

class ClientManager:
    def __init__(self) -> None:
        self._clients: Dict[str, Client] = {}

    def add_client(self, name: str, email: str) -> None:
        if name in self._clients:
            raise ValueError(f"Клиент '{name}' уже существует")
        self._clients[name] = Client(name, email)

    def get_client(self, name: str) -> Optional[Client]:
        return self._clients.get(name)

    def get_client_email(self, name: str) -> str:
        if name not in self._clients:
            raise KeyError(f"Клиент '{name}' не найден")
        return self._clients[name].email

    def get_all_clients(self) -> List[Client]:
        return list(self._clients.values())

    def get_client_names(self) -> List[str]:
        return list(self._clients.keys())

    def update_client(self, name: str, new_email: Optional[str] = None) -> None:
        if name not in self._clients:
            raise KeyError(f"Клиент '{name}' не найден")
        if new_email is not None:
            self._clients[name].email = new_email

    def delete_client(self, name: str) -> None:
        if name not in self._clients:
            raise KeyError(f"Клиент '{name}' не найден")
        del self._clients[name]
