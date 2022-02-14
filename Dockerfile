FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip3 install pipenv

RUN pipenv install --system --deploy

EXPOSE 5000

CMD [ "pipenv", "run", "app" ]