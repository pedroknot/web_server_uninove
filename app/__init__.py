from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Banco de dados
from flask_script import Manager # Controle de informações que são passadas na execução
from flask_migrate import Migrate, MigrateCommand # Cuida das informações


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db) # Recebe a aplicação e o banco de dados

manager = Manager(app) # Cuida dos comandos para inicializar a aplicação
manager.add_command('db', MigrateCommand)

from app.controllers import default

