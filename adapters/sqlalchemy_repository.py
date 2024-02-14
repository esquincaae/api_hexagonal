# adapters/sqlalchemy_repository.py
from domain.models import User
from ports.user_repository import UserRepository
import uuid

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db_session):
        self.db_session = db_session
    
    def save(self, user):
        self.db_session.add(user)
        self.db_session.commit()
    
    def find_by_activation_token(self, token):
        return self.db_session.query(User).filter_by(activation_token=token).first()
    
    def update(self, user):
        self.db_session.commit()
    
    def generate_activation_token(self):
        return str(uuid.uuid4())

    def find_by_email(self, email: str) -> User:
        return self.db_session.query(User).filter_by(email=email).first()
