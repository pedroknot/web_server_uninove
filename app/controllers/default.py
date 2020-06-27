from flask import render_template, flash, redirect, url_for, jsonify, request
from flask_login import login_user, logout_user
from app import app, db, lm, es
from app.controllers.elastic_data import produtos_query

from app.models.forms import LoginForm
from app.models.tables import User

from base64 import b64encode
import requests
import os
import json

"""
Endpoints
"""


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("produtos"))
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


@app.route("/produtos")
def produtos():
    produtos = produtos_query()
    return render_template('produtos.html',
                            produtos=produtos)

# @app.route("/produtos")
# def produtos():
#     body = {
#         "size":100,
#         "query": {
#             "match_all":{}
#         }
#     }

#     res = es.search(index="produto", body=body)

#     resp = []
#     for produtos in res['hits']['hits']:
#         resp.append(produtos['_source'])
#     return jsonify(resp)


# @app.route("/storage/", methods=["GET","POST"])
# def storage():
#     nome_produto = request.form.get('nome')
#     preco = request.form.get('preco')
#     categoria_produto = request.form.get('categoria')
#     if nome_produto or preco or categoria_produto != None:
#         i = Produtos(nome_produto, preco, categoria_produto)
#         db.session.add(i)
#         db.session.commit()
#         return redirect(url_for("storage"))
#     produtos = Produtos.query.all()
#     res = {}
#     for produto in produtos:
#         res[produto.id] = {
#             'produto': produto.nome_produto,
#             'preco': str(produto.preco),
#             'categoria': produto.categoria_produto
#         }
#     return jsonify(res)



@app.route('/search', methods=['GET'])
def search():

    body = {
        "query": {
            "match_all":{}
        }
    }

    res = es.search(index="mercado", body=body)

    resp = []
    for produtos in res['hits']['hits']:
        resp.append(produtos['_source'])
    return jsonify(resp)



@app.route('/search_term', methods=['GET'])
def search_term():

    body ={
          "size": 0,
  "aggs": {
    "categorias": {
      "terms": {
        "field": "categoriaNome.keyword",
        "size": 999
      }
    }
  }

    }
    res = es.search(index="produto", body=body)
    
    return jsonify(res['aggregations']['categorias']['buckets'])



