from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
from .spotify import *
router = APIRouter()


@router.get('/features/{enter_song_here}')
async def features(enter_song_here: str):
    """
    Type in Song below to get back features
    
    ### Path Parameter
    `enter_song_here`: Type in song name exactly as it appears on the album
    
    ### Response
    JSON string to render with [react-plotly.js](https://plotly.com/javascript/react/)
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
        'song_name': name,
        'artist_name': artistname,
        'features': select_features
    }
