FROM python:3.8.5-slim-buster

# set work directory
WORKDIR /usr/src/app

# install psycopg2 dependencies
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
EXPOSE 8000
CMD ["python3", "manage.py", "runserver"]
