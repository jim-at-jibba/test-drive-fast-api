# Fast api tut

![Continuous Integration and Delivery](https://github.com/jim-at-jibba/test-drive-fast-api/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=main)

[Testdriven - FastAPI and docker](https://testdriven.io/courses/tdd-fastapi/)

## Peotry

- To enter the virtenv `poetry shell`
- To exit the virtenv `poetry shell --exit`
- To add a dependency `poetry add <package>`

## FastAPI

- using `uvicorn` to run the app
- from *fast_api* directory, run `uvicorn app.main:app`
- to hot reload `uvicorn app.main:app --reload`
- Settings are all configured in `config.py`

```bash
(env)$ export ENVIRONMENT=prod
(env)$ export TESTING=1
```

- This will set the `ENVIRONMENT` and `TESTING` variables to `prod` and `1`
- We are caching the result of the `get_settings` using `lru_cache` with the `@lru_cache()` decorator

## Docker and Poetry

- Had some issues using Poetry in docker. Could not get it to install the deps.
- Using poetry to create requirements.txt. This seems a little jank so need to do some more research,
`poetry export --no-interaction --no-ansi --without-hashes --format requirements.txt --dev --output ./fast_api/requirements.dev.txt`
- [This was helpful](https://stackoverflow.com/questions/57331667/cant-install-dependencies-in-docker-container/57374374#57374374)
- [Maybe try this next time](https://medium.com/@harpalsahota/dockerizing-python-poetry-applications-1aa3acb76287)

## DB

- `docker compose exec web-db psql -U postgres` - connect to db
- `docker-compose exec web aerich init-db` - creates first migration with aerich

## Tests

- `docker compose exec web python -m pytest` - run the tests

```bash
# normal run
$ docker-compose exec web python -m pytest

# with coverage
docker-compose exec web python -m pytest --cov="."

# with coverage html
docker-compose exec web python -m pytest --cov="." --cov-report html

# disable warnings
$ docker-compose exec web python -m pytest -p no:warnings

# run only the last failed tests
$ docker-compose exec web python -m pytest --lf

# run only the tests with names that match the string expression
$ docker-compose exec web python -m pytest -k "summary and not test_read_summary"

# stop the test session after the first failure
$ docker-compose exec web python -m pytest -x

# enter PDB after first failure then end the test session
$ docker-compose exec web python -m pytest -x --pdb

# stop the test run after two failures
$ docker-compose exec web python -m pytest --maxfail=2

# show local variables in tracebacks
$ docker-compose exec web python -m pytest -l

# list the 2 slowest tests
$ docker-compose exec web python -m pytest --durations=2
```

# Code quality

```bash
# FLAKE8
# check
docker-compose exec web flake8 .

# BLACK
# dry run
docker-compose exec web black . --check

# diff of changes
docker-compose exec web black . --diff

# do it
docker-compose exec web black .

# ISORT
# check
$ docker-compose exec web isort . --check-only

# diff
$ docker-compose exec web isort . --diff

#do it
$ docker-compose exec web isort .
```
