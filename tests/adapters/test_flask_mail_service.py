import pytest
from adapters.flask_mail_service import FlaskMailService
from flask_mail import Mail
from unittest.mock import patch

@pytest.fixture
def email_service(app):
    mail = Mail(app)
    return FlaskMailService(mail)

@patch('flask_mail.Mail.send')
def test_send_activation_email(mock_send, email_service):
    email_service.send_activation_email("john@example.com", "token123")
    mock_send.assert_called_once()
