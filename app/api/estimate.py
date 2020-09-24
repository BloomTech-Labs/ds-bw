import re
import sqlite3
import pandas as pd
from typing import Dict
from fastapi import APIRouter
from pydantic import BaseModel, Field, validator

router = APIRouter()


class User(BaseModel):
    """Data model to parse the request body JSON."""

    username: str = Field(..., example='seviuqyelsdnirb')

    def to_df(self):
        """Convert JSON request to pandas DataFrame."""
        return pd.DataFrame([dict(self)])

    @validator('username')
    def check_username_character_range(cls, value):
        """Validate that username is of proper length."""
        assert 2 <= len(value) <= 15, f'username = {value}, must be \
between 2 and 15 characters long.'
        return value

    @validator('username')
    def check_username_acceptable_characters(cls, value):
        """Validate that user has no forbidden characters."""
        assert bool(re.search('^[a-zA-Z0-9_-]*$', value)), \
            f'username = {value}, must contain only letters digits, \
dashes or underscores'
        return value


@router.post('/saltiest-hackers')
async def get_saltiest_hackers(num_hackers: int = 100,
                               min_comments: int = 1) -> Dict[str, int]:
    """
    Return 'saltiest' Hacker News commenters.

    # Parameters
    - `num_hackers`: positive integer, number of users(hackers) to return.

    - `min_comments`: positive integer, minimum number of comments a user
    must have to be considered.

    # Response
    - `username`: string between 2 and 15 characters long containing only
    letters, digits, dashes, and underscores

    - `sentiment_score`: float between - 1 and 1 rounded to four decimal
    places. Negative numbers correspond to negative sentiment.

    """
    conn = sqlite3.connect(database='hn.db')
    curs = conn.cursor()

    sentiment_query = (f"""
    SELECT user, avg_sentiment_score
    FROM hn_users
    WHERE num_comments >= {min_comments}
    ORDER BY avg_sentiment_score
    LIMIT {num_hackers};
    """)

    results = curs.execute(sentiment_query)
    return {k + 1: (v[0], round(v[1], 4)) for k, v in enumerate(results)}


@router.post('/comments')
async def get_comments(user: User,
                       num_comments: int = 1) -> Dict[int, str]:
    """
    Return saltiest Hacker News comments of a given Hacker News user.

    # Request Body
    - `username`: str between 2 and 15 characters long containing only
    letters, digits, dashes, and underscores

    # Parameters
    - `num_comments`: int of the number of comments to return. A negative
    value returns all comments by a user

    # Response
    - `comment`: str of the Hacker News comment(s)
    """
    conn = sqlite3.connect(database='hn.db')
    curs = conn.cursor()

    comments_query = (f"""
    SELECT comment
    FROM hn_comments
    WHERE user = '{user.username}'
    ORDER BY sentiment_score
    LIMIT {num_comments};
    """)

    comments = curs.execute(comments_query)
    return {k + 1: v[0] for k, v in enumerate(comments)}


@router.post('/estimate-salt')
async def get_sentiment(user: User
                        ) -> Dict[float, int]:
    """
    Use Valence Aware Dictionary and sEntiment Reasoner(VADER) \
    to estimate sentiment score of a given Hacker News user.

    # Request Body
    - `username`: string between 2 and 15 characters long containing only
    letters, digits, dashes, and underscores

    # Response
    - `avg_sentiment_score`: float between - 1 and 1, rounded to four
    decimal places, of the average sentiment of that user's comments.
    Negative numbers correspond to negative sentiment.

    - `sentiment_ranking`: positive integer
    """
    conn = sqlite3.connect(database='hn.db')
    curs = conn.cursor()

    sentiment_query = (f"""
    SELECT avg_sentiment_score, sentiment_ranking
    FROM hn_users
    WHERE user = '{user.username}'
    LIMIT 1;
    """)

    results = curs.execute(sentiment_query).fetchone()

    return {
        'avg_sentiment_score': round(results[0], 4),
        'sentiment_ranking': results[1]
    }
