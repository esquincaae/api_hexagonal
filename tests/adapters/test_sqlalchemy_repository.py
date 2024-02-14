import pytest
from adapters.sqlalchemy_repository import SQLAlchemyUserRepository
from domain.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def user_repository():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()
    return SQLAlchemyUserRepository(session)

def test_save_user(user_repository):
    user = User(name="John", last_name="Doe", cellphone="1234567890", email="john@example.com", password="secret")
    user_repository.save(user)
    retrieved_user = user_repository.find_by_email("john@example.com")
    assert retrieved_user is not None
    assert retrieved_user.name == "John"
