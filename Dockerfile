FROM python:3.7.1

LABEL Author="Rishabh Raj Sharma"
LABEL E-mail="rishabhrajshrm00@gmail.com"
LABEL version="0.0.1"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "url_shortner"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0