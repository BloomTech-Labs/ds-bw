from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import features, graph, predict

app = FastAPI(
    title='Spotify Song Suggester',
    description='Helps users find and visualize songs that fit their personal taste.',
    version='0.1',
    docs_url='/',
)

app.include_router(features.router)
app.include_router(graph.router)
app.include_router(predict.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
