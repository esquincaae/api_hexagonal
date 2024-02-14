# domain/use_cases.py
from datetime import datetime

class RegisterUser:
    def __init__(self, user_repository, email_service):
        self.user_repository = user_repository
        self.email_service = email_service
    
    def execute(self, user):
        user.activation_token = self.user_repository.generate_activation_token()
        self.user_repository.save(user)
        self.email_service.send_activation_email(user.email, user.activation_token)

class ActivateUser:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def execute(self, activation_token):
        user = self.user_repository.find_by_activation_token(activation_token)
        if user:
            user.verified_at = datetime.utcnow()
            self.user_repository.update(user)
            return True
        return False
