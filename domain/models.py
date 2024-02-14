# domain/models.py
class User:
    def __init__(self, name, last_name, cellphone, email, password):
        self.name = name
        self.last_name = last_name
        self.cellphone = cellphone
        self.email = email
        self.password = password
        self.activation_token = None
        self.verified_at = None