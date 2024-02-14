from domain.models import User

def test_user_creation():
    user = User(name="John", last_name="Doe", cellphone="1234567890", email="john@example.com", password="secret")
    assert user.email == "john@example.com"
