# News Board API
News Board Rest Framework with  Celery, Redis, Docker, Postgresql 

---
## Postman collection link
[Get collection](https://www.getpostman.com/collections/211cc39eae3eaa9937f6)


## How to run API?
```
git clone https://github.com/madatbay/drf-board.git
cd drf-board/
chmod +x docker-entrypoint.sh
docker-compose up
```

## Test Server
In this project I'm using Django + Postgresql, DRF, Celery, `django-celery-beat`, Redis as a message broker. So, if we run project we are going to start 5 containers. Though we can use Redis and Postgresql as `add-on` on Heroku, it's not convinient to work with multiple containers. At the end, I have deployed my project in VPS for testing purposes (that's why I didn't used `NGINX` container to not extend container quantity and not configured some production settings - like static files, .env variables and so on)

[Visit](http://65.21.154.97/)

## Run a recurring job
You can run any recurring job with the help of `Celery` by either manually adding task into `tasks.py` or creating job from `admin`. To create job from Django admin you need to create superuser:
```
docker exec django python manage.py createsuperuser
...
..
.
```
*Note: If you are using test server I deployed, you can use default admin user*
```
username: admin
password: admin
```

After `admin` login you need to add `Periodic task` to create recurring job