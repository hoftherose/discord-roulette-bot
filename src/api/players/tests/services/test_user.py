from src.services import users


def test_get_all_users():
    assert users.get_all_users()
