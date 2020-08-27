import logging
import random
import pandas
import numpy as np
import os
print(os.getcwd())
from .spotify import *

from sklearn.neighbors import NearestNeighbors
import keras
x = keras.models.load_model(f'{os.getcwd()}/app/api/encoder_model.mdl')

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()

keys = ['acousticness',
    'danceability',
    'energy',
    'instrumentalness',
    'key',
    'liveness',
    'loudness',
    'mode',
    'speechiness',
    'tempo',
    'valence']


df = pd.read_csv('https://raw.githubusercontent.com/VegaSera/spotify_song_suggester/master/SpotifyAudioFeaturesApril2019.csv')

df2 = df.drop(columns=['artist_name', 'track_id', 'track_name', 'duration_ms', 'time_signature'])

encoded = x.predict(df2)

df3 = pd.DataFrame(x.predict(df2))

nn = NearestNeighbors(n_neighbors=11)
nn.fit(encoded)

def get_recommendations(input):
    # Get track features
    spotify = SpotifyAPI(client_id, client_secret)
    features = spotify.get_features(input)
    select_features = {x:features[x] for x in keys}
    select_features['popularity'] = 0
    # Convert track features to pd.Series in line with df2
    # Pass input through autoencoder
    test_input = pd.Series(select_features)
    encoded_song = x.predict(np.array([test_input]))
    # Pass the encoded input to the nearest neighbors model
    neighbors = nn.kneighbors(encoded_song)[1][0][1:]
    # Get the track IDs from neighbors and return
    return df.iloc[neighbors]['track_id'].tolist(), neighbors


class Item(BaseModel):
    """(Place Holder Example Code) 
    Use this data model to parse the request body JSON."""

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
async def predict(item: str):
    """
    Make random baseline predictions for classification problem 🔮
    ### Request Body
    - `item`: song id
    ### Response
    - `recommendations`: returns ten song id's similar to the input item song id.
    """

    # X_new = item.to_df()
    # log.info(X_new)
    # y_pred = random.choice([True, False])
    # y_pred_proba = random.random() / 2 + 0.5

   

    recommendations, _ = get_recommendations(item)
    return {
        'recommendations' : recommendations
    }


