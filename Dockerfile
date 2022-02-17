FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip3 install pipenv

RUN pipenv lock --keep-outdated --requirements > requirements.txt

RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py" ]