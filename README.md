# DS Build Week scaffold

- [Big picture](#big-picture)
- [Tech stack](#tech-stack)
- [Getting started](#getting-started)
- [File structure](#file-structure)
- [More instructions](#more-instructions)
- [Deploying to Heroku](#deploying-to-heroku)
- [Example: Machine learning](#example-machine-learning)

## Big picture

Here's a template with starter code to deploy an API for your machine learning model and data visualizations.  You're encouraged (but not required) to use this template for your Build Week.

You can deploy on Heroku in 10 minutes. Here's the template deployed as-is: [https://ds-bw-test.herokuapp.com/](https://ds-bw-test.herokuapp.com/)

Instead of Flask, we'll use FastAPI. It's similar, but faster, with automatic interactive docs. For more comparison, see [FastAPI for Flask Users](https://amitness.com/2020/06/fastapi-vs-flask/).

## Tech stack
- [FastAPI](https://fastapi.tiangolo.com/): Web framework. Like Flask, but faster, with automatic interactive docs.
- [Flake8](https://flake8.pycqa.org/en/latest/): Linter, enforces PEP8 style guide.
- [Heroku](https://devcenter.heroku.com/): Platform as a service, hosts your API.
- [Pipenv](https://pipenv.pypa.io/en/latest/): Reproducible virtual environment, manages dependencies.
- [Plotly](https://plotly.com/python/): Visualization library, for Python & JavaScript.
- [Pytest](https://docs.pytest.org/en/stable/): Testing framework, runs your unit tests.

## Getting started

[Create a new repository from this template.](https://github.com/Lambda-School-Labs/ds-bw/generate)

Clone the repo
```
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPO-NAME.git

cd YOUR-REPO-NAME
```

Install dependencies
```
pipenv install --dev
```

Activate the virtual environment
```
pipenv shell
```

Launch the app
```
uvicorn app.main:app --reload
```

Go to `localhost:8000` in your browser.

![image](https://user-images.githubusercontent.com/7278219/87965040-c18ba300-ca80-11ea-894f-d51a69d52f8a.png)

You'll see your API documentation:

- Your app's title, "DS API"
- Your description, "Lorem ipsum"
- An endpoint for POST requests, `/predict`
- An endpoint for GET requests, `/viz/{statecode}`

Click the `/predict` endpoint's green button.

![image](https://user-images.githubusercontent.com/7278219/87965845-0532dc80-ca82-11ea-9690-b4c195a648d6.png)

You'll see the endpoint's documentation, including:

- Your function's docstring, """Make random baseline predictions for classification problem."""
- Request body example, as [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) (like a Python dictionary)
- A button, "Try it out"

Click the "Try it out" button.

![image](https://user-images.githubusercontent.com/7278219/87966677-39f36380-ca83-11ea-97f4-313bc11d3f19.png)

The request body becomes editable. 

Click the "Execute" button. Then scroll down.

![image](https://user-images.githubusercontent.com/7278219/87966896-948cbf80-ca83-11ea-9740-d0801148b1f3.png)

You'll see the server response, including:

- [Code 200](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200), which means the request was successful.
- The response body, as [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON), with random baseline predictions for a classification problem.

***Your job is to replace these random predictions with real predictions from your model.*** Use this starter code and documentation to deploy your model as an API!

## File structure

```
.
└── app
    ├── __init__.py
    ├── db.py
    ├── main.py
    ├── ml.py
    ├── viz.py
    └── tests
        ├── __init__.py
        ├── test_main.py
        └── test_predict.py
```

`app/main.py` is where you edit your app's title and description, which are displayed at the top of the your automatically generated documentation. This file also configures "Cross-Origin Resource Sharing", which you shouldn't need to edit. 

- [FastAPI docs - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI docs - Metadata](https://fastapi.tiangolo.com/tutorial/metadata/)
- [FastAPI docs - CORS](https://fastapi.tiangolo.com/tutorial/cors/)

`app/ml.py` defines the Machine Learning endpoint. `/predict` accepts POST requests and responds with random predictions. In a notebook, train your model and pickle it. Then in this source code file, unpickle your model and edit the `predict` function to return real predictions.

- [Scikit-learn docs - Model persistence](https://scikit-learn.org/stable/modules/model_persistence.html)
- [Keras docs - Serialization and saving](https://keras.io/guides/serialization_and_saving/)

When your API receives a POST request, FastAPI automatically parses and validates the request body JSON, using the `Item` class attributes and functions. Edit this class so it's consistent with the column names and types from your training dataframe. 

- [FastAPI docs - Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI docs - Field additional arguments](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#field-additional-arguments)
- [calmcode.io video - FastAPI - Json](https://calmcode.io/fastapi/json.html)
- [calmcode.io video - FastAPI - Type Validation](https://calmcode.io/fastapi/type-validation.html)
- [pydantic docs - Validators](https://pydantic-docs.helpmanual.io/usage/validators/)

`app/tests/test_*.py` is where you edit your pytest unit tests. 

- [FastAPI docs - Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [calmcode.io videos - FastAPI - Testing](https://calmcode.io/fastapi/testing-one.html)
- [calmcode.io videos - pytest](https://calmcode.io/pytest/introduction.html)

## More instructions

Activate the virtual environment
```
pipenv shell
```

Install additional packages
```
pipenv install PYPI-PACKAGE-NAME
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

[calmcode.io videos - flake8](https://calmcode.io/flake8/introduction.html)

## Deploying to Heroku

Prepare Heroku
```
heroku login

heroku create YOUR-APP-NAME-GOES-HERE

heroku git:remote -a YOUR-APP-NAME-GOES-HERE
```

Deploy to Heroku
```
git add --all

git add --force Pipfile.lock

git commit -m "Deploy to Heroku"

git push heroku main:master

heroku open
```

<small>(If you get a `Locking failed!` error when deploying to Heroku or running `pipenv install` then delete `Pipfile.lock` and try again, without `git add --force Pipfile.lock`)</small>

Deactivate the virtual environment
```
exit
```

## Example: Machine learning

Follow the [getting started](#getting-started) instructions.

Edit `app/main.py` to add your API `title` and `description`.

```python
app = FastAPI(
    title='House Price DS API',
    description='Predict house prices in California',
    docs_url='/',
)
```

Edit `app/ml.py` to add a docstring for your predict function and return a naive baseline. 

```python
@router.post('/predict')
async def predict(item: Item):
    """Predict house prices in California."""
    y_pred = 200000
    return {'predicted_price': y_pred}
```

In a notebook, explore your data. Make an educated guess of what features you'll use.

```python
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Load data
california = fetch_california_housing()
print(california.DESCR)
X = pd.DataFrame(california.data, columns=california.feature_names)
y = california.target

# Rename columns
X.columns = X.columns.str.lower()
X = X.rename(columns={'avebedrms': 'bedrooms', 'averooms': 'total_rooms', 'houseage': 'house_age'})

# Explore descriptive stats
X.describe()
```

```python
# Use these 3 features
features = ['bedrooms', 'total_rooms', 'house_age']
```

Edit the class in `app/ml.py` to use your features.

```python
class House(BaseModel):
    """Use this data model to parse the request body JSON."""
    bedrooms: int
    total_rooms: float
    house_age: float

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

@router.post('/predict')
async def predict(house: House):
    """Predict house prices in California."""
    X_new = house.to_df()
    y_pred = 200000
    return {'predicted_price': y_pred}
```

Test locally, then [deploy to Heroku](#deploying-to-heroku) with your work-in-progress. Get to this point by the middle of Build Week. (By Wednesday lunch for full-time cohorts. By end of week one for part-time cohorts.) Now your web teammates can make POST requests to your API endpoint.

In a notebook, train your pipeline and pickle it. See these docs:

- [Scikit-learn docs - Model persistence](https://scikit-learn.org/stable/modules/model_persistence.html)
- [Keras docs - Serialization and saving](https://keras.io/guides/serialization_and_saving/)

Get version numbers for every package you used in your pipeline. [Install the exact versions of these packages](#more-instructions) in your virtual environment.

Edit `app/ml.py` to unpickle your model and use it in your predict function. 

Now you are ready to re-deploy! 🚀
