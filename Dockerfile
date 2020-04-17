FROM python:3.8

WORKDIR /app

COPY /src /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD [ "python", "__init__.py" ]