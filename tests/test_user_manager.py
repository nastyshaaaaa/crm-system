import pytest
from user_manager import UserManager

def test_register():
    um = UserManager()
    user = um.register("alice", "alice@example.com", "pass123")
    assert user.username == "alice"
    assert user.check_password("pass123") is True

def test_register_duplicate():
    um = UserManager()
    um.register("bob", "bob@ex.com", "123")
    with pytest.raises(ValueError, match="Пользователь bob уже существует"):
        um.register("bob", "b2@ex.com", "456")

def test_authenticate_success():
    um = UserManager()
    um.register("carol", "carol@ex.com", "secret")
    user = um.authenticate("carol", "secret")
    assert user is not None
    assert user.username == "carol"

def test_authenticate_wrong_password():
    um = UserManager()
    um.register("dave", "dave@ex.com", "pass")
    assert um.authenticate("dave", "wrong") is None

def test_authenticate_nonexistent():
    um = UserManager()
    assert um.authenticate("unknown", "pass") is None
