FROM python:3

ADD . /app_elastic
WORKDIR /app_elastic

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD [ "run.py" ]
