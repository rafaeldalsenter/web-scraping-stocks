# web-scraping-stocks
💸 Stock information scraping app

Python application that makes scrapes on WebPages to collect information of stocks and insert in MongoDB database. The capture is made through a schedule.

A Docker image of the application has been created, it's available on the [Docker Hub](https://hub.docker.com/repository/docker/rafaeldalsenter/web-scraping-stocks). There are instructions on how to use the parameters.

There is an example docker-compose file to upload the environment, it will upload the application (passing the stocks by parameter) and MongoDB database, just run :)

```
docker-compose up --build -d
``` 

| CodeFactor |
|:---:|
|[![CodeFactor](https://www.codefactor.io/repository/github/rafaeldalsenter/web-scraping-stocks/badge)](https://www.codefactor.io/repository/github/rafaeldalsenter/web-scraping-stocks)|
