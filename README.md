### web_server_elasctic

### apagando containers
docker container rm -f $(docker ps -qa)

### gerando imagem
docker build -t pedroknot/elastic_project .

### subindo container
docker run -d -p 5000:5000 --name elasitc_project_container pedroknot/elastic_project

### Testando base
curl -H "Content-Type: application/json" -X GET http://localhost:5000/storage/
r = requests.post('http://localhost:5000/search', data={'keyword': 'mustangue'})



### pip freeze > requirements.txt
### pip install -r requirements.txt
### python3 run.py runserver //inicia o servidor
### python3 run.py db init // cria pasta migrations
### python3 run.py db migrate // Pega oq tem no banco de dados e compara com o que já existe, ve o que precisa alterar
### python3 run.py db upgrade // sobe o banco de dados

toda vez que fizer uma alteração na estrutura do banco de dados usar os comandos `migrate` e `upgrade`

### Fontes
https://jtemporal.com/deploy-flask-heroku/
http://pythonclub.com.br/publicando-seu-hello-world-no-heroku.html
https://drive.google.com/drive/u/1/folders/1l25mC670RQ6PYP_xd3B3EIY9noy1jMNV

### Fonte elasticsearch
https://dev.to/aligoren/using-elasticsearch-with-python-and-flask-2i0e