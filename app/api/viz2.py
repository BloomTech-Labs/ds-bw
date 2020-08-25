from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

router = APIRouter()


@router.get('/viz2')
async def viz2():
    features = ['acousticness', 'dancability', 'duration', 'energy', 'instrumentalenss', 'key',
          'liveliness', 'loudness', 'speechiness', 'tempo', 'time_signature', 'popularity']

    fig = go.Figure()
    fig.add_trace(go.Bar(
    x=features,
    y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
    name='Song_1',
    marker_color='greenyellow'
    ))
    fig.add_trace(go.Bar(
    x=features,
    y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
    name='Song_2',
    marker_color='deepskyblue'
    ))

    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    return fig.to_json()