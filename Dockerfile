#create a dockerfile that will execute pytest tests. copy requirements.txt file to the dockerfile. Use selenium as instructed in the docker-compose.yml file.
FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
WORKDIR /spaceship
COPY . .
CMD ["pytest", "-v"]