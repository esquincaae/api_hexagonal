import pytest
from domain.use_cases import RegisterUser, ActivateUser
from unittest.mock import Mock

def test_register_user():
    user_repository = Mock()
    email_service = Mock()
    register_user = RegisterUser(user_repository, email_service)
    
    user = Mock()
    register_user.execute(user)
    
    user_repository.save.assert_called_with(user)
    email_service.send_activation_email.assert_called_with(user.email, user.activation_token)

def test_activate_user():
    user_repository = Mock()
    activate_user = ActivateUser(user_repository)
    
    token = "some_activation_token"
    activate_user.execute(token)
    
    user_repository.find_by_activation_token.assert_called_with(token)
    