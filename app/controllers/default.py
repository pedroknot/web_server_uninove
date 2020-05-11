from app import app

"""
Endpoints
"""

@app.route("/") # Decorator onde é passado a rota
def index():
    return "Hello world!"


@app.route("/test/", defaults={'name': None}, methods=['GET'])
@app.route("/test/<name>")
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, usuário"