SoftDesk
========

# Installation

## Requirements

You must have some tools installed on your laptop
* Poetry (see https://python-poetry.org/docs/)
* Pyenv (see https://github.com/pyenv/pyenv#installation)

## Project

Clone the repository the way you prefer.

Run the following command in the project root directory
```shell
poetry install
```

It will install all the project dependencies

# Usage

## Apply migrations

```shell
poetry run python manage.py migrate
```

## Run

```shell
poetry run python manage.py runserver
```

# Contributing

## Develop

Fork the repo, write your code, add some tests and create a pull request.

## Create migration

```shell
poetry run python manage.py makemigrations
# Don't forget to apply them
poetry run python manage.py migrate
```
