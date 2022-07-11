# Fast api tut

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
