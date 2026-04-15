# client_manager.py (фрагмент изменений)
from typing import Dict, List, Optional
from models import Client

class ClientManager:
    def __init__(self):
        # ключ: (owner_id, client_name) -> Client
        self._clients: Dict[tuple, Client] = {}

    def add_client(self, owner_id: str, name: str, email: str) -> None:
        key = (owner_id, name)
        if key in self._clients:
            raise ValueError(f"Клиент '{name}' уже существует для этого пользователя")
        self._clients[key] = Client(name, email)

    def get_clients_by_owner(self, owner_id: str) -> List[Client]:
        return [client for (oid, _), client in self._clients.items() if oid == owner_id]

    def get_client_email(self, owner_id: str, name: str) -> str:
        key = (owner_id, name)
        if key not in self._clients:
            raise KeyError(f"Клиент '{name}' не найден")
        return self._clients[key].email

    def delete_client(self, owner_id: str, name: str) -> None:
        key = (owner_id, name)
        if key not in self._clients:
            raise KeyError(f"Клиент '{name}' не найден")
        del self._clients[key]
