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


class ProdutosApk(db.Model):
    __tablename__ = "produtosApk"

    id_produto = db.Column(db.Integer, primary_key=True)
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresa.id_empresa'))
    nome_produto = db.Column(db.Text, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    imagem = db.Column(db.Text, nullable=False)
    preco = db.Column(db.Text, nullable=False)
    quantidade = db.Column(db.Text, nullable=False)
    promocao = db.Column(db.Text, nullable=False)

    empresa = db.relationship('Empresa', foreign_keys=id_empresa)

    def __init__(self, nome_produto, descricao, imagem, preco, quantidade, promocao, id_empresa):
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.imagem = imagem
        self.preco = preco
        self.quantidade = quantidade
        self.promocao = promocao
        self.id_empresa = id_empresa

    def __repr__(self):
        return "<ProdutosApk %r>" % self.id_produto
    

class Empresa(db.Model):
    __tablename__ = "empresa"

    id_empresa = db.Column(db.Integer, primary_key=True)
    nome_empresa = db.Column(db.Text, nullable=False)
    cnpj = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)

    def __init__(self, nome_empresa, cnpj, email):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.email = email

    def __repr__(self):
        return "<Empresa %r>" % self.id_empresa


class UsersApk(db.Model):
    __tablename__ = "usersApk"

    id_usuario = db.Column(db.Integer, primary_key=True)
    id_cargo = db.Column(db.Integer, db.ForeignKey('cargos.id_cargo'))
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresa.id_empresa'))
    nome_cliente = db.Column(db.Text, nullable=False)
    cpf = db.Column(db.Text, nullable=False)
    cidade = db.Column(db.Text, nullable=True)
    estado = db.Column(db.Text, nullable=False)
    pais = db.Column(db.Text, nullable=False)
    numero = db.Column(db.Text, nullable=False)
    data_nascimento = db.Column(db.Text, nullable=False)
    celular = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    instagram = db.Column(db.Text, nullable=False)
    facebook = db.Column(db.Text, nullable=False)
    whatsapp = db.Column(db.Text, nullable=False)
    senha = db.Column(db.Text, nullable=False)

    empresa = db.relationship('Empresa', foreign_keys=id_empresa)
    cargo = db.relationship('Cargos', foreign_keys=id_cargo)

    def __init__(self, nome_cliente, cpf, cidade, estado, pais, numero, data_nascimento, celular, 
                email, instagram, facebook, whatsapp, senha, id_empresa, id_cargo):
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.estado = estado
        self.pais = pais
        self.numero = numero
        self.data_nascimento = data_nascimento
        self.celular = celular
        self.email = email
        self.instagram = instagram
        self.facebook = facebook
        self.whatsapp = whatsapp
        self.senha = senha
        self.id_empresa = id_empresa
        self.id_cargo = id_cargo

    def __repr__(self):
        return "<UsersApk %r>" % self.id_usuario


class Cargos(db.Model):
    __tablename__ = "cargos"

    id_cargo= db.Column(db.Integer, primary_key=True)
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresa.id_empresa'))
    nome_cargo = db.Column(db.Text, nullable=False)

    empresa = db.relationship('Empresa', foreign_keys=id_empresa)

    def __init__(self, nome_cargo, id_empresa):
        self.nome_cargo = nome_cargo
        self.id_empresa = id_empresa


    def __repr__(self):
        return "<Cargos %r>" % self.id_cargo
    


        """
             CREATE TABLE IF NOT EXISTS TB_CARGOS(" +
                "ID_CARGO INTEGER primary key," +
                "ID_EMPRESA INTEGER NOT NULL," +
                "NOME_CARGO varchar NOT NULL);";


             "CREATE TABLE IF NOT EXISTS " + tabelaUsuario() + "(" +
                "ID_USUARIO INTEGER primary key," +
                "ID_CARGO INTEGER ," +
                "ID_EMPRESA INTEGER ," +
                "NOME_CLIENTE varchar NOT NULL," +
                "CPF varchar NOT NULL," +
                "CIDADE varchar NOT NULL," +
                "ESTADO varchar NOT NULL," +
                "PAIS varchar NOT NULL," +
                "NUMERO varchar NOT NULL," +
                "DATA_NASCIMENTO varchar NOT NULL," +
                "CELULAR varchar NOT NULL," +
                "EMAIL varchar NOT NULL," +
                "Instagram varchar NOT NULL," +
                "Facebook varchar NOT NULL," +
                "whatsapp varchar NOT NULL," +
                "SENHA varchar NOT NULL);";


            "CREATE TABLE IF NOT EXISTS " + getTb_empresa() + "(" +
                "ID_EMPRESA INTEGER primary key," +
                "NOME_EMPRESA varchar NOT NULL," +
                "CNPJ varchar NOT NULL," +
                "EMAIL varchar NOT NULL);";


            "CREATE TABLE IF NOT EXISTS " + getTb_produtos() + "(" +
                "ID_PRODUTO INTEGER primary key," +
                "ID_EMPRESA INTEGER," +
                "NOME_PRODUTO varchar NOT NULL," +
                "DESCRICAO varchar NOT NULL," +
                "IMAGEM varchar NOT NULL," +
                "PRECO varchar NOT NULL," +
                "QUANTIDADE varchar NOT NULL," +
                "PROMOCAO varchar NOT NULL);";
        """