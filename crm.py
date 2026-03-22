# crm.py - простая CRM-система

class ClientManager:
    def __init__(self):
        self.clients = {}   # словарь: имя -> email

    def add_client(self, name, email):
        """Добавляет клиента. Если клиент уже есть, вызывает ошибку."""
        if name in self.clients:
            raise ValueError(f"Клиент {name} уже существует")
        self.clients[name] = email

    def get_clients(self):
        """Возвращает список имён клиентов."""
        return list(self.clients.keys())

    def get_client_email(self, name):
        """Возвращает email клиента по имени."""
        return self.clients.get(name)
