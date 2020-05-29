from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Banco de dados
from flask_script import Manager # Controle de informações que são passadas na execução
from flask_migrate import Migrate, MigrateCommand # Cuida das informações
from flask_login import LoginManager

from elasticsearch import Elasticsearch

es = Elasticsearch()
app = Flask(__name__)
app.config.from_object('config') # Passando configurações para o Flask

db = SQLAlchemy(app)
migrate = Migrate(app, db) # Recebe a aplicação e o banco de dados

manager = Manager(app) # Cuida dos comandos para inicializar a aplicação
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)



from app.models import tables, forms
from app.controllers import default

