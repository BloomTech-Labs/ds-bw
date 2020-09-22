from fastapi import APIRouter
from bs4 import BeautifulSoup
import requests
from app.api.nlp import pos_sentiment_score, neg_sentiment_score
import pandas as pd
import sqlite3

router = APIRouter()


@router.get('/current-top-10-sweet')
def current_top_10_sweet():
    n_com = 100
    top_n = 10
    page = requests.get("https://news.ycombinator.com/newcomments")
    soup = BeautifulSoup(page.content, features='html.parser')


    user_coms = zip(soup.find_all('a', class_='hnuser')[:n_com],
                    soup.find_all('div', class_='comment')[:n_com])

    com_scores_sweet = []
    users_comments = []

    for user, com in user_coms:
        score = pos_sentiment_score(com.get_text())
        com_scores_sweet.append([user.get_text(), score])
        users_comments.append([user.get_text(), com.get_text()])

    com_scores_sweet.sort(key=lambda x: x[1], reverse=True)
    for idx in range(len(com_scores_sweet)):
        com_scores_sweet[idx].insert(0, idx + 1)
        response_object = pd.DataFrame(com_scores_sweet[:top_n], columns=['Rank', 'Hacker News User', 'Score'])
    return response_object.to_json()


@router.get('/current-top-10-salty')
def current_top_10_salty():
    n_com = 100
    top_n = 10
    page = requests.get("https://news.ycombinator.com/newcomments")
    soup = BeautifulSoup(page.content, features='html.parser')

    user_coms = zip(soup.find_all('a', class_='hnuser')[:n_com],
                    soup.find_all('div', class_='comment')[:n_com])

    com_scores_salty = []
    users_comments = []

    for user, com in user_coms:
        score = neg_sentiment_score(com.get_text())
        com_scores_salty.append([user.get_text(), score])
        users_comments.append([user.get_text(), com.get_text()])

    com_scores_salty.sort(key=lambda x: x[1], reverse=True)
    for idx in range(len(com_scores_salty)):
        com_scores_salty[idx].insert(0, idx + 1)
        response_object = pd.DataFrame(com_scores_salty[:top_n], columns=['Rank', 'Hacker News User', 'Score'])
    return response_object.to_json()


@router.get('/user-comments<user-name>')
def user_comments(user_name):
    conn = sqlite3.connect(db)
    curs = conn.cursor()

    query = curs.execute(f"SELECT author, comment FROM hn_comments WHERE author =={user_name}", conn)

    user_comment = curs.fetchall()

    return user_comment.to_json()

if __name__ == '__main__':
    print(current_top_10_salty())
