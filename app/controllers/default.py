from flask import render_template, flash, redirect, url_for, jsonify, request
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.forms import LoginForm
from app.models.tables import User, Produtos, ProdutosApk, Empresa, UsersApk, Cargos

from base64 import b64encode
import requests
import flask
import os

"""
Endpoints
"""


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/")# Decorator onde é passado a rota
def index():
    return render_template('index.html')

@app.route("/home/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
        else:
            flash("Invalid login.")
    else:
        print('ERROR')
    return render_template('login.html',
                            form=form)

@app.route("/"+str(b64encode(b"/logout")))
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("login"))

@app.route("/"+str(b64encode(b"/produtos")))
def produtos():
    port = int(os.environ.get("PORT", 5000))
    produtos = requests.get(f"http://0.0.0.0:{port}/storage/").json()
    return render_template('produtos.html',
                            produtos=produtos)

@app.route("/"+str(b64encode(b"/contato")))
def contato():
    return render_template('contato.html')

@app.route("/"+str(b64encode(b"/sobre")))
def sobre():
    return render_template('sobre.html')

@app.route("/"+str(b64encode(b"/download_app")))
def download_app():
    return render_template('download_app.html')

@app.route("/"+str(b64encode(b"/promocoes")))
def promocoes():
    return render_template('promocoes.html')

@app.route("/storage/", methods=["GET","POST"])
def storage():
    nome_produto = request.form.get('nome')
    preco = request.form.get('preco')
    categoria_produto = request.form.get('categoria')
    if nome_produto or preco or categoria_produto != None:
        i = Produtos(nome_produto, preco, categoria_produto)
        db.session.add(i)
        db.session.commit()
        return redirect(url_for("storage"))
    produtos = Produtos.query.all()
    res = {}
    for produto in produtos:
        res[produto.id] = {
            'produto': produto.nome_produto,
            'preco': str(produto.preco),
            'categoria': produto.categoria_produto
        }
    return jsonify(res)

@app.route("/storage_item/", methods=["GET", "POST"])
def storage_item():
    produtos = {"id_produto":"1", "id_empresa":"1", "nome_produto":"TV 60", "descricao":"Tela plana HBO","imagem":"0", "preco":"2332", "quantidade":"10", "promocao":"0"}
    return jsonify(produtos)

@app.route("/storage_itens/", methods=["GET", "POST"])
def storage_itens():
    produto_um = {"id_produto":"1", "id_empresa":"1", "nome_produto":"TV 60", "descricao":"Tela plana HBO","imagem":"0", "preco":"2332", "quantidade":"10", "promocao":"0"}
    produto_dois = {"id_produto":"2", "id_empresa":"2", "nome_produto":"CARRO", "descricao":"Tela plana HBO","imagem":"0", "preco":"2332", "quantidade":"10", "promocao":"0"}
    produto_tres = {"id_produto":"3", "id_empresa":"3", "nome_produto":"CASA", "descricao":"Tela plana HBO","imagem":"0", "preco":"2332", "quantidade":"10", "promocao":"0"}

    

    return jsonify(produto_um, produto_dois, produto_tres) 
        
@app.route("/get_produtos/", methods=["GET", "POST"])
def get_produtos():
    if flask.request.method == 'POST':
        try:
            id_empresa = request.form.get('id_empresa')
            nome_produto = request.form.get('nome_produto')
            descricao = request.form.get('descricao')
            imagem = request.form.get('imagem')
            preco = request.form.get('preco')
            quantidade = request.form.get('quantidade')
            promocao = request.form.get('promocao')

            insert = ProdutosApk(nome_produto, descricao, imagem, preco, quantidade, promocao, id_empresa)
            db.session.add(insert)
            db.session.commit()
            return "Produto inserido com sucesso!"
        except Exception as ex:
            return f"Erro: {ex}"        

    else:
        produtos = ProdutosApk.query.all()
        res = []
        for produto in produtos:
            res.append({
                'id_produto': produto.id_produto,
                'id_empresa': produto.id_empresa,
                'nome_produto': produto.nome_produto,
                'descricao': produto.descricao,
                'imagem': produto.imagem,
                'preco': produto.preco,
                'quantidade': produto.quantidade,
                'promocao': produto.promocao
            })
        return jsonify(res)


@app.route("/get_empresas/", methods=["GET", "POST"])
def get_empresas():
    empresas = Empresa.query.all()
    res = []
    for empresa in empresas:
        res.append({
            'id_empresa': empresa.id_empresa,
            'nome_empresa': empresa.nome_empresa,
            'cnpj': empresa.cnpj,
            'email': empresa.email
        })
    return jsonify(res)


@app.route("/get_usuarios/", methods=["GET", "POST"])
def get_usuarios():
    usuarios = UsersApk.query.all()
    res = []
    for usuario in usuarios:
        res.append({
            'id_usuario': usuario.id_usuario,
            'id_cargo': usuario.id_cargo,
            'id_empresa': usuario.id_empresa,
            'nome_cliente': usuario.nome_cliente,
            'cpf': usuario.cpf,
            'estado': usuario.estado,
            'pais': usuario.pais,
            'data_nascimento': usuario.data_nascimento,
            'celular': usuario.celular,
            'email': usuario.email,
            'instagram': usuario.instagram,
            'facebook': usuario.facebook,
            'whatsapp': usuario.whatsapp,
            'senha': usuario.senha
        })
    return jsonify(res)


@app.route("/get_cargos/", methods=["GET", "POST"])
def get_cargos():
    cargos = Cargos.query.all()
    res = []
    for cargo in cargos:
        res.append({
            'id_cargo': cargo.id_cargo,
            'id_empresa': cargo.id_empresa,
            'nome_cargo': cargo.nome_cargo
        })
    return jsonify(res)


# @app.route("/teste/<info>")
# @app.route("/teste", defaults={"info":None})
# def teste(info):
    # insert
    # i = User("Pedro","1234", "Pedro H","pedroknots@lalala")
    # db.session.add(i)
    # db.session.commit()

    # update
    # r = User.query.filter_by(username="Pedro").first()
    # r.name = "Pedro Henrique"
    # db.session.add(r)
    # db.session.commit()
    # print(r.name)

    # delete
    # r = User.query.filter_by(username="Pedro").first()
    # db.session.delete(r)
    # db.session.commit()
    # return "OK"


