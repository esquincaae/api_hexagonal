# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from domain.models import User
from domain.use_cases import RegisterUser, ActivateUser
from adapters.sqlalchemy_repository import SQLAlchemyUserRepository
from adapters.flask_mail_service import FlaskMailService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'aec8e2a2f4b692e211ca3ceaabb39dd0ba3e35ff923973e3'
db = SQLAlchemy(app)
mail = Mail(app)

user_repository = SQLAlchemyUserRepository(db.session)
email_service = FlaskMailService(mail)

@app.route('/users/register', methods=['POST'])
def register():
    data = request.json
    user = User(name=data['name'], last_name=data['last_name'], cellphone=data['cellphone'], email=data['email'], password=data['password'])
    register_user_case = RegisterUser(user_repository, email_service)
    register_user_case.execute(user)
    return jsonify({'message': 'Usuario registrado satisfatoriamente. Por favor revise su email para activar su cuenta.'}), 201

@app.route('/users/activate/<token>', methods=['GET'])
def activate(token):
    activate_user_case = ActivateUser(user_repository)
    if activate_user_case.execute(token):
        return jsonify({'message': 'Usuario activado satisfatoriamente.'}), 200
    return jsonify({'message': 'Activacion fallida.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
