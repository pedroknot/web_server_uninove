### web_server_elasctic

### apagando containers
docker container rm -f $(docker ps -qa)

### gerando imagem
docker build -t pedroknot/elastic_project .

### subindo container
docker run -d -p 5000:5000 --name elasitc_project_container pedroknot/elastic_project


# pip freeze > requirements.txt
# pip install -r requirements.txt
# python3 run.py runserver //inicia o servidor
# python3 run.py db init // cria pasta migrations
# python3 run.py db migrate // Pega oq tem no banco de dados e compara com o que já existe, ve o que precisa alterar
# python3 run.py db upgrade // sobe o banco de dados

toda vez que fizer uma alteração no banco de dados usar os comandos `migrate` e `upgrade`

https://jtemporal.com/deploy-flask-heroku/
http://pythonclub.com.br/publicando-seu-hello-world-no-heroku.html
https://drive.google.com/drive/u/1/folders/1l25mC670RQ6PYP_xd3B3EIY9noy1jMNV