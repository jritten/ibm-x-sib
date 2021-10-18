FROM python:3.8

# set work directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip ;\
    pip install -r requirements.txt

# copy project
COPY . /app/


EXPOSE 8080

CMD ["gunicorn","--bind=0.0.0.0:8080","--workers=2","--timeout","6000","consumer:app"]