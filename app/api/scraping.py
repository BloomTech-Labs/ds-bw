from bs4 import BeautifulSoup
import requests

n_com = 100
top_n = 10
page = requests.get("https://news.ycombinator.com/newcomments")
soup = BeautifulSoup(page.content, features='html.parser')

com_scores = []
times = soup.find('a', class_='age')[:n_com]
users = soup.find('a', class_='hnuser')[:n_com]
coms = soup.find_all('div', class_='comment')[:n_com]

for user in users:
    print(user.get_text())

for com in coms:
    print(com.get_text())

for time in times:
    print(time.get_text())




