from abc import ABC, abstractmethod

class EmailService(ABC):
    @abstractmethod
    def send_activation_email(self, email: str, activation_token: str) -> None:
        """
        Envía un correo electrónico de activación a un usuario con un enlace para activar su cuenta.
        
        :param email: Dirección de correo electrónico del destinatario.
        :param activation_token: Token de activación que se incluirá en el enlace de activación.
        """
        pass
