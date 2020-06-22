# DS Build Week 

Starter code to deploy your machine learning model as an API on Heroku.

## Tech stack
- [FastAPI](https://fastapi.tiangolo.com/): Web framework. Like Flask, but faster, with automatic interactive docs.
- [Flake8](https://flake8.pycqa.org/en/latest/): Linter, enforces PEP8 style guide.
- [Heroku](https://devcenter.heroku.com/): Platform as a service, hosts your API.
- [Pipenv](https://pipenv.pypa.io/en/latest/): Reproducible virtual environment, manages dependencies.
- [Pytest](https://docs.pytest.org/en/stable/): Testing framework, runs your unit tests.

## Instructions

Fork the repo, then clone it
```
git clone https://github.com/YOUR-GITHUB-USERNAME/ds-bw.git

cd ds-bw
```

Install dependencies
```
pipenv install --dev

git add Pipfile.lock

git commit -m "Add Pipfile.lock"
```

Install additional package
```
pipenv install PYPI-PACKAGE-NAME
```

Activate the virtual environment
```
pipenv shell
```

Launch the app
```
uvicorn app.main:app --reload
```

Launch a Jupyter notebook
```
jupyter notebook
```

Run tests
```
pytest
```

Run linter
```
flake8
```

Prepare Heroku
```
heroku login

heroku create YOUR-APP-NAME-GOES-HERE

heroku git:remote -a YOUR-APP-NAME-GOES-HERE
```

Deploy to Heroku
```
git add --all

git commit -m "Deploy to Heroku"

git push heroku main:master

heroku open
```

Deactivate the virtual environment
```
exit
```
