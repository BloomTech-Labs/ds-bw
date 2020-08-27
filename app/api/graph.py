from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .spotify import *

router = APIRouter()

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/VegaSera/spotify_song_suggester/master/SpotifyAudioFeaturesApril2019.csv')

df2 = df.drop(columns=['artist_name', 'track_id', 'track_name', 'duration_ms', 'time_signature'])

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

def get_graph_features(song_id_str):
      # Get track features
      spotify = SpotifyAPI(client_id, client_secret)
      features = spotify.get_features(song_id_str)
      select_features = {x:features[x] for x in keys}
      select_features['popularity'] = 0
      test_input = pd.Series(select_features)
      cols = (test_input.index.tolist())
      vals = (test_input.values.tolist())
      return cols, vals

def graph_two_songs(songid_1, songid_2):
      cols, vals = get_graph_features(songid_1)
      _, vals2 = get_graph_features(songid_2)

      fig = go.Figure()

      fig.add_trace(go.Scatterpolar(
            r=vals,
            theta=cols,
            fill='toself',
            name=songid_1
      ))
      fig.add_trace(go.Scatterpolar(
            r=vals2,
            theta=cols,
            fill='toself',
            name=songid_2
      ))

      fig.update_layout(
      polar=dict(
      radialaxis=dict(
            visible=True,
            range=[0, 5]
      )),
      showlegend=True
      )
      
      return fig

@router.get('/graph')
async def graph(enter_song_1_here: str, enter_song_2_here: str):
      """
      ## How to use -
      * Click on "try it out."
      * Look up two song ID's above. 
      * Copy and paste 2 song ID's into the inputs below.
      * The output will be a JSON string that should be a plotly radar plot.
      * It will show the similarities and differences of the two songs features.
      
      ## Path Parameter -
      `enter_song_1_here`: Type in song ID for song 1.

      ## Path Parameter -
      `enter_song_2_here`: Type in song ID for song 2.
      
      ## Response -
      JSON string to render with [react-plotly.js](https://plotly.com/javascript/react/)
      """

      graph = graph_two_songs(enter_song_1_here, enter_song_2_here)

      return graph.to_json()