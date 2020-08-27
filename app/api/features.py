from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
from .spotify import *
router = APIRouter()


@router.get('/features/{enter_song_here}')
async def features(enter_song_here: str):
    """
    ## How to use -
    * First click on "try it out."
    * Type in a Favorite Song Title of yours below to get back that song's ID and features.  
    * For instance "Piano Man" (minus the quotes).
    * (Some songs have the same name so you might get back another artist who wrote a song with the same title).
    * Then copy that song ID (without quotes) to enter into the predict input below. 
    * Predict will then use your ID to recommend 10 similar songs.
    
    ## Path Parameter -
    * `enter_song_here`: Type in song by name here. 
    
    """
    
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
        'song_id': songID,
        'song_name': name,
        'artist_name': artistname,
        'features': select_features
    }
