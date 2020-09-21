from bs4 import BeautifulSoup
import requests
from app.api.nlp import sentiment_score

n_com = 100
top_n = 10
page = requests.get("https://news.ycombinator.com/newcomments")
soup = BeautifulSoup(page.content, features='html.parser')

com_scores = []
user_coms = zip(soup.find_all('a', class_='hnuser')[:n_com],
                soup.find_all('div', class_='comment')[:n_com])
for user, com in user_coms:
    score = sentiment_score(com.get_text())
    com_scores.append([user.get_text(), score])
    print(com_scores)
com_scores.sort(key=lambda x: x[1], reverse=True)
for idx in range(len(com_scores)):
    com_scores[idx].insert(0, idx+1)




