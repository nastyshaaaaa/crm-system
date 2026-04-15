from dataclasses import dataclass
from enum import Enum
import bcrypt

@dataclass
class User:
    username: str
    email: str
    password_hash: str

    @staticmethod
    def hash_password(password: str) -> str:
        """Хеширует пароль с помощью bcrypt."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password: str) -> bool:
        """Проверяет пароль."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
