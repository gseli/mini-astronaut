#create a docker file to run pytest in a container
FROM python:3.9
#This could be any name
WORKDIR /app
#copy the requirements.txt file to the container
COPY requirements.txt .
#install the requirements
RUN pip install -r requirements.txt
#copy the rest of the files to the container
COPY . .
#run the pytest command

CMD ["pytest", "-v", "--junitxml=report.xml", "--cov=app", "--cov-report=xml"]