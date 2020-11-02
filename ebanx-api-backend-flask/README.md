# ebanx-api-backend-flask

## Setup

- Is highly recommended using a virtual environment. Feel free to choose how can you create an env:
  - conda
  - virtualenv
  - virtualenvwrapper
- Install `requirements.txt`.

  ```bash
  pip install -r requirements.txt
  ```

- Export environment variables

  ```bash
  export FLASK_APP=app
  # Set environment to development.
  # To run production set FLASK_ENV=production
  export FLASK_ENV=development
  ```

- Execute flask

  ```bash
  flask run -h 0.0.0.0
  ```

## Test

The API implements tests using `pytest` python module. Everything is set and, to run, simply execute

``` bash
pytest
```

this command will search for `conftest.py` to get all the basic configurations (fixtures, for example) and, after configured, search for all files with pattern `test_<filename>.py`.