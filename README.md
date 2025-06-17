#  Pizza Restaurant API

This project is a simple RESTful API built with Flask, following the MVC architecture. It manages restaurants, pizzas, and their associations. No frontend istesting is done via Postman.

---

## Getting Started

### 1. Clone & Install


git clone <https://github.com/guyn126/pizza-api-challenge>
cd pizza-api-challenge
pipenv install
pipenv shell


### Install dependencies
pipenv install flask flask_sqlalchemy flask_migrate
pipenv install flask-migrate
pipenv shell


### Seed the database
python -m server.seed


### Set Flask environment variables
export FLASK_APP=server.app:create_app
export FLASK_ENV=development


### Run the server
flask run
