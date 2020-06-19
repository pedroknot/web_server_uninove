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

# @app.route("/"+str(b64encode(b"/produtos")))
# def produtos():
#     port = int(os.environ.get("PORT", 5000))
#     produtos = requests.get(f"http://0.0.0.0:{port}/storage/").json()
#     return render_template('produtos.html',
#                             produtos=produtos)

@app.route("/"+str(b64encode(b"/produtos")))
def produtos():
    port = int(os.environ.get("PORT", 5000))
    produtos = requests.get(f"http://0.0.0.0:{port}/get_produtos/").json()
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

@app.route("/get_produtos/", methods=["GET", "POST"])
def get_produtos():

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


@app.route("/produtos/", methods=["GET", "POST"])
def produtos_insert():

    produtos = request.get_json()
    id_produto = produtos['id_produto']
    id_empresa = produtos['id_empresa']
    nome_produto = produtos['nome_produto']
    descricao = produtos['descricao']
    imagem = produtos['imagem']
    preco = produtos['preco']
    quantidade = produtos['quantidade']
    promocao = produtos['promocao']

    data = [{'id_empresa':id_empresa, 'id_produto':id_produto, 'nome_produto':nome_produto, 'type':produtos['type'],
            'descricao':descricao, 'imagem':imagem, 'preco':preco, 'quantidade':quantidade, 'promocao':promocao }]

    if produtos['type'] == "insert":
        try:
            insert = ProdutosApk(nome_produto, descricao, imagem, preco, quantidade, promocao, id_empresa)
            db.session.add(insert)
            db.session.commit()

            return jsonify(data)
        except Exception as ex:
            return f"ERRO: {ex}" 
    
    elif produtos['type'] == "update":
        try:
            ProdutosApk.query.filter_by(id_produto=id_produto).update(dict(nome_produto=nome_produto, descricao=descricao, 
            imagem=imagem, quantidade=quantidade, promocao=promocao, id_empresa=id_empresa))

            db.session.commit()

            return jsonify(data)
        except Exception as ex:
            return f"ERRO: {ex}"
        
    elif produtos['type'] == "delete":
        try:
            ProdutosApk.query.filter_by(id_produto=id_produto).delete()
            db.session.commit()

            return jsonify(data)
        except Exception as ex:
            return f"ERRO: {ex}"        


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



@app.route("/empresas/", methods=["GET", "POST"])
def empresas():
    empresa = request.get_json()
    id_empresa = empresa['id_empresa']
    nome_empresa = empresa['nome_empresa']
    cnpj = empresa['cnpj']
    email = empresa['email']


    data = [{'id_empresa':id_empresa, 'nome_empresa':nome_empresa, 'cnpj':cnpj, 'type':empresa['type'],
            'email':email }]

    if empresa['type'] == "insert":
        try:
            insert = Empresa(nome_empresa, cnpj, email)
            db.session.add(insert)
            db.session.commit()

            return jsonify(data)
        except Exception as ex:
            return f"ERRO: {ex}" 

    elif empresa['type'] == "update":
        try:
            Empresa.query.filter_by(id_empresa=id_empresa).update(dict(nome_empresa=nome_empresa, cnpj=cnpj, 
            email=email))
            db.session.commit()
            return jsonify(data)

        except Exception as ex:
            return f"ERRO: {ex}"
        
    elif empresa['type'] == "delete":
        try:
            Empresa.query.filter_by(id_empresa=id_empresa).delete()
            db.session.commit()

            return jsonify(data)
        except Exception as ex:
            return f"ERRO: {ex}"



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
                'cidade': usuario.cidade,
                'celular': usuario.celular,
                'email': usuario.email,
                'instagram': usuario.instagram,
                'facebook': usuario.facebook,
                'whatsapp': usuario.whatsapp,
                'senha': usuario.senha,
                'numero': usuario.numero
            })
        return jsonify(res)


@app.route("/usuarios/", methods=["GET", "POST"])
def usuarios():

    usuarios = request.get_json()
    id_usuario = usuarios['id_usuario']
    id_cargo = usuarios['id_cargo']
    id_empresa = usuarios['id_empresa']
    nome_cliente = usuarios['nome_cliente']
    cpf = usuarios['cpf']
    estado = usuarios['estado']
    cidade = usuarios['cidade'],"MG"
    pais = usuarios['pais']
    data_nascimento = usuarios['data_nascimento']
    celular = usuarios['celular']
    numero = usuarios['numero']
    email = usuarios['email']
    instagram = usuarios['instagram']
    facebook = usuarios['facebook']
    whatsapp = usuarios['whatsapp']
    senha = usuarios['senha']

    data = [{'id_usuario':id_usuario, 'id_cargo':id_cargo, 'cidade':cidade,'type':usuarios['type'],
            'id_empresa':id_empresa, 'nome_cliente':nome_cliente,'cpf':cpf,'estado':estado,
            'pais':pais, 'data_nascimento':data_nascimento,'celular':celular, 'email':email, 'instagram':instagram,
            'facebook':facebook, 'whatsapp':whatsapp, 'senha':senha}]

    if usuarios['type'] == "insert":
        try:
            insert = UsersApk(nome_cliente, cpf, cidade, estado, pais, numero, data_nascimento, celular, 
            email, instagram, facebook, whatsapp, senha, id_empresa, id_cargo)
            db.session.add(insert)
            db.session.commit()

            return jsonify(data)
        except Exception as ex:
            return f"ERRO: {ex}" 
    
    elif usuarios['type'] == "update":
        try:
            UsersApk.query.filter_by(id_usuario=id_usuario).update(dict(nome_cliente=nome_cliente, cpf=cpf, 
            cidade=cidade, estado=estado, pais=pais, numero=numero, data_nascimento=data_nascimento, celular=celular,
            email=email, instagram=instagram, facebook=facebook, whatsapp=whatsapp, senha=senha, id_empresa=id_empresa,
            id_cargo=id_cargo))

            db.session.commit()

            return jsonify(data)
        except Exception as ex:
            return f"ERRO: {ex}"
        
    elif usuarios['type'] == "delete":
        try:
            UsersApk.query.filter_by(id_usuario=id_usuario).delete()
            db.session.commit()

            return jsonify(data)
        except Exception as ex:
            return f"ERRO: {ex}"
    

    elif usuarios['type'] == "login":
        try:
            user = UsersApk.query.filter_by(id_usuario=id_usuario).first()
            print(user)
            data_login = [{"id_usuario":user.id_usuario, "id_cargo":user.id_cargo, "type":usuarios['type'],
                    "id_empresa":user.id_empresa, "nome_cliente":user.nome_cliente,"cpf":user.cpf,"estado":user.estado,
                    "pais":user.pais, "data_nascimento":user.data_nascimento,"celular":user.celular, "email":user.email, "instagram":user.instagram,
                    "facebook":user.facebook, "whatsapp":user.whatsapp, "senha":user.senha, "cidade":user.cidade}]
            return jsonify(data_login)
        except Exception as ex:
            return f"ERRO: {ex}"   



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


@app.route("/cargos/", methods=["GET", "POST"])
def cargos():

    cargos = request.get_json()
    id_cargo = cargos['id_cargo']
    id_empresa = cargos['id_empresa']
    nome_cargo = cargos['nome_cargo']

    data = [{'id_cargo':id_cargo, 'id_empresa':id_empresa, 'nome_cargo':nome_cargo}]

    if cargos['type'] == "insert":
        try:
            insert = Cargos(nome_cargo, id_empresa)
            db.session.add(insert)
            db.session.commit()

            return jsonify(data)
        except Exception as ex:
            return f"ERRO: {ex}" 

    elif cargos['type'] == "update":
        try:
            Cargos.query.filter_by(id_cargo=id_cargo).update(dict(nome_cargo=nome_cargo, id_empresa=id_empresa))
            db.session.commit()
            return jsonify(data)

        except Exception as ex:
            return f"ERRO: {ex}"
        
    elif cargos['type'] == "delete":
        try:
            Cargos.query.filter_by(id_cargo=id_cargo).delete()
            db.session.commit()

            return jsonify(data)
        except Exception as ex:
            return f"ERRO: {ex}"





