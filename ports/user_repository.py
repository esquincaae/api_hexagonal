from abc import ABC, abstractmethod
from typing import Optional
from domain.models import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        """
        Guarda un nuevo usuario o actualiza uno existente en el repositorio.
        
        :param user: La instancia del usuario a guardar o actualizar.
        """
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        """
        Busca un usuario por su correo electrónico.
        
        :param email: El correo electrónico del usuario a buscar.
        :return: Una instancia de User si se encuentra uno, de lo contrario None.
        """
        pass

    @abstractmethod
    def find_by_activation_token(self, token: str) -> Optional[User]:
        """
        Busca un usuario por su token de activación.
        
        :param token: El token de activación del usuario a buscar.
        :return: Una instancia de User si se encuentra uno, de lo contrario None.
        """
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        """
        Actualiza la información de un usuario existente en el repositorio.
        
        :param user: La instancia del usuario a actualizar.
        """
        pass

    @abstractmethod
    def generate_activation_token(self) -> str:
        """
        Genera un nuevo token de activación.
        """
        pass
 