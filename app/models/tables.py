from app import db

"""
Classes representando tabelas
"""

db.create_all()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    #flaskLogin
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
    
    def __repr__(self):
        return "<User %r>" % self.username


# class Post(db.Model):
#     __tablename__ = "posts"

#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     user = db.relationship('User', foreign_keys=user_id)

#     def __init__(self, content, user_id):
#         self.content = content
#         self.user_id = user_id

#     def __repr__(self):
#         return "<Post %r>" % self.id


# class Follow(db.Model):
#     tablename = "follow"

#     id = db.Column(db.Integer, primary_key=True)
#     id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
#     follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     user = db.relationship('User', foreign_keys=follower_id)


class Produtos(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.Text)
    preco = db.Column(db.Float)
    categoria_produto = db.Column(db.Text)

    def __init__(self, nome_produto, preco, categoria_produto):
        self.nome_produto = nome_produto
        self.preco = preco
        self.categoria_produto = categoria_produto

    def __repr__(self):
        return "<Produto %r>" % self.id