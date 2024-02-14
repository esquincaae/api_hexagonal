# config/settings.py
import os

# Configuraciones básicas
SECRET_KEY = os.getenv('SECRET_KEY', 'tu_clave_secreta_aquí')

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')

# Configuraciones de correo electrónico
MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.example.com')
MAIL_PORT = int(os.getenv('MAIL_PORT', 465))
MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'False').lower() in ('true', '1', 't')
MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'True').lower() in ('true', '1', 't')
MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'your_email@example.com')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'your_password')

# JWT Configurations
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'otra_clave_secreta_aquí')

# Intenta cargar configuraciones locales que pueden sobrescribir las predeterminadas
try:
    from .settings_local import *
except ImportError:
    pass
