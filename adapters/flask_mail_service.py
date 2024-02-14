# adapters/flask_mail_service.py
from ports.email_service import EmailService
from flask_mail import Message

class FlaskMailService(EmailService):
    def __init__(self, mail):
        self.mail = mail
    
    def send_activation_email(self, email, activation_token):
        msg = Message('Activa tu cuenta', recipients=[email])
        msg.body = f'Por favor activa tu cuenta usando el siguiente token → {activation_token}'
        self.mail.send(msg)
