from flask import render_template, flash, redirect, url_for, jsonify, request
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.forms import LoginForm
from app.models.tables import User, Produtos

from base64 import b64encode
import requests
import os

"""
Endpoints
"""


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/"+str(b64encode(b"/home/")))# Decorator onde é passado a rota
def index():
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
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

@app.route("/storage/", methods=["GET"])
def storage():
    produtos = Produtos.query.all()
    res = {}
    for produto in produtos:
        res[produto.id] = {
            'produto': produto.nome_produto,
            'preco': str(produto.preco),
            'categoria': produto.categoria_produto
        }
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


