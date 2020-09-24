## Project
Identify and rank negative commenters on Hacker News using sentiment analysis, and make their comments and rankings accessible. Then deploy an API for the machine learning model and data visualizations.

App here: https://salted-hacker-news.herokuapp.com/

## Getting started

Clone the repo
```
git clone https://github.com/Salty-Hackers/data-engineering.git
cd data-engineering
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

## File structure

```
.
|── data
├── app
|    ├── __init__.py
|    ├── main.py
|    ├── api
|    │   ├── __init__.py
|    │   ├── estimate.py
|    │   └── viz.py    
|    └── tests
|        ├── __init__.py
|        ├── test_main.py
|        ├── test_estimate.py
|        └── test_viz.py
├── notebooks
    ├── hn_preprocessing_and_sentiment_analysis.ipynb
```

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

## Data Source
[Google BigQuery](https://console.cloud.google.com/marketplace/product/y-combinator/hacker-news)

## Data Dictionaries

### Raw dataset
This dataset contains all stories and comments from Hacker News from its launch in 2006 to present.

Field | Type | Description
------|--------|----------
**id** | Integer | The item's unique id.
`by` | String | The username of the item's author.
`author` | String | The username of the item's author.
`time` | Integer | Creation date of the item, in [Unix Time](http://en.wikipedia.org/wiki/Unix_time).
`time_ts` | Datetime | The full date and time of the comment, including microseconds.
`text` | String | The comment, story or poll text. HTML.
`parent` | Integer | The comment's parent's id: either another comment or the relevant story.
`deleted` | Boolean | `true` if the item is deleted.
`dead` | Boolean | `true` if the item is dead.
`ranking` | Integer | The story's score, or the votes for a pollopt.


### Processed datasets

#### hn_comments

Field | Type | Description
------|--------|----------
`comment` | String | The comment text.
`user` | String | The username of the comment's author.
`date_time` | Datetime | The full date and time of the comment, excluding microseconds.
`sentiment_score` | Float | [Vader's normalized composite sentiment score](https://github.com/cjhutto/vaderSentiment#about-the-scoring). -1  is most extreme negative, +1 is most extreme positive.
`sentiment` | String | The overall sentiment of the comment based on the `sentiment_score`.

#### hn_users

Field | Type | Description
------|--------|----------
`user` | String | The username of the Hacker News commenter.
`avg_sentiment_score`| Float | The arithmetic mean of the sentiment of user's comments, from -1 to 1.
`num_comments` | Integer | The total number of comments by a user.
`sentiment_ranking` | Integer | Users ordered by their.`avg_sentiment_score`, from saltiest to sweetest.