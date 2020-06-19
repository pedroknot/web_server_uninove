# web_server_uninove
Projeto uninove 2020

Instalar libs no arquivo requirements.txt

para subir api:
rodar comando python3 run.py

Estrutura formada no padrão MVC
.
├── controllers
│   ├── default.py
│   └── __init__.py
├── __init__.py
├── models
│   ├── forms.py
│   ├── __init__.py
│   └── tables.py
|
│ 
│  
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap.min.css.map
│   │   └── style.css
│   ├── img
│   │   ├── app.jpeg
│   │   ├── foto1.PNG
│   │   ├── foto2.PNG
│   │   ├── foto3.PNG
│   │   ├── fundo8.gif
│   │   ├── índice1.jpeg
│   │   ├── índice2.jpeg
│   │   ├── índice3.jpeg
│   │   ├── logo.jpeg
│   │   ├── promo2.jpeg
│   │   ├── promo3.jpeg
│   │   ├── promo4.jpeg
│   │   ├── promo5.jpeg
│   │   ├── promo6.jpeg
│   │   ├── promo7.jpeg
│   │   ├── promo8.jpeg
│   │   ├── promo.jpeg
│   │   ├── sobre2.jpg
│   │   └── sobre4.jpg
│   └── js
│       └── bootstrap.min.js.map
├── storage.db
└── templates
    ├── base.html
    ├── contato.html
    ├── download_app.html
    ├── index.html
    ├── login.html
    ├── produtos.html
    ├── promocoes.html
    └── sobre.html





INFORMAÇÕES DE MANUTENÇÃO

### python3 run.py runserver //inicia o servidor
### python3 run.py db init // cria pasta migrations
### python3 run.py db migrate // Pega oq tem no banco de dados e compara com o que já existe, ve o que precisa alterar
### python3 run.py db upgrade // sobe o banco de dados

toda vez que fizer uma alteração no banco de dados usar os comandos `migrate` e `upgrade`

### Fontes
https://jtemporal.com/deploy-flask-heroku/

http://pythonclub.com.br/publicando-seu-hello-world-no-heroku.html

https://drive.google.com/drive/u/1/folders/1l25mC670RQ6PYP_xd3B3EIY9noy1jMNV