"""Управление пользователями и аутентификация."""
from typing import Dict, Optional
from models import User

class UserManager:
    def __init__(self):
        self._users: Dict[str, User] = {}  # username -> User

    def register(self, username: str, email: str, password: str) -> User:
        """Регистрация нового пользователя."""
        if username in self._users:
            raise ValueError(f"Пользователь {username} уже существует")
        if not username or not email or not password:
            raise ValueError("Все поля обязательны")
        user = User(username, email, User.hash_password(password))
        self._users[username] = user
        return user

    def authenticate(self, username: str, password: str) -> Optional[User]:
        """Проверяет логин и пароль. Возвращает пользователя или None."""
        user = self._users.get(username)
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, username: str) -> Optional[User]:
        return self._users.get(username)
