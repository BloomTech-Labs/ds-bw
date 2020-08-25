import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
from .spotify import *

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    x1: float = Field(..., example=3.14)
    x2: int = Field(..., example=-42)
    x3: str = Field(..., example='banjo')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('x1')
    def x1_must_be_positive(cls, value):
        """Validate that x1 is a positive number."""
        assert value > 0, f'x1 == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(item: Item):

    keys = ['acousticness',
        'danceability',
        'duration_ms',
        'energy',
        'instrumentalness',
        'key',
        'liveness',
        'loudness',
        'mode',
        'speechiness',
        'tempo',
        'time_signature',
        'valence']

    spotify = SpotifyAPI(client_id, client_secret)
    track1 = spotify.search(enter_song_here, search_type="track")
    songID = track1["tracks"]["items"][0]["id"]
    features = spotify.get_features(songID)
    name = track1["tracks"]["items"][0]["name"]
    artist = spotify.artist_from_track_id(songID)
    artistname = artist["album"]["artists"][0]["name"]
    select_features = {x:features[x] for x in keys}

    return {
        'name': name,
        'artist_name': artistname,
        'features': select_features
    }



