from flask import render_template, flash, redirect, url_for # Renderizar os templates
from flask_login import login_user, logout_user
from app import app, db, lm


from app.models.forms import LoginForm
from app.models.tables import User
"""
Endpoints
"""

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/home/") # Decorator onde é passado a rota
@app.route("/home")
def index():
    return render_template('index.html')


@app.route("/index/", methods=["GET", "POST"])
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

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("login"))

@app.route("/produtos")
def produtos():
    return render_template('produtos.html')

# @app.route("/teste/<info>")
# @app.route("/teste", defaults={"info":None})
# def teste(info):
#     # insert
#     # i = User("Pedro","1234", "Pedro H","pedroknots@lalala")
#     # db.session.add(i)
#     # db.session.commit()

#     # update
#     # r = User.query.filter_by(username="Pedro").first()
#     # r.name = "Pedro Henrique"
#     # db.session.add(r)
#     # db.session.commit()
#     # print(r.name)

#     # delete
#     # r = User.query.filter_by(username="Pedro").first()
#     # db.session.delete(r)
#     # db.session.commit()
#     return "OK"



# @app.route("/index/<user>") # Decorator onde é passado a rota
# @app.route("/", defaults={"user":None})
# @app.route("/index/", defaults={"user":None})
# def index(user):
#     return render_template('index.html',
#                             user=user)


# @app.route("/test/", defaults={'name': None}, methods=['GET'])
# @app.route("/test/<name>")
# def test(name):
#     if name:
#         return "Olá, %s!" % name
#     else:
#         return "Olá, usuário"