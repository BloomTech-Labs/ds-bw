# DS Build Week starter code

Fork the repo, then clone it
```
git clone https://github.com/your-github-username/ds-bw.git

cd ds-bw
```

Install dependencies
```
pipenv install --dev

git add Pipfile.lock

git commit -m "Add Pipfile.lock"
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

heroku create your-app-name-goes-here

heroku git:remote -a your-app-name-goes-here
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
