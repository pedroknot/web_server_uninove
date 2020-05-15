import os
# Caminho absoluto deste diretório
basedir = os.path.abspath(os.path.dirname(__file__))
"""
Arquivo de configurações
"""

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "CHAVE_SEGURANÇA"