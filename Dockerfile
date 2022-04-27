FROM python:3.9


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app