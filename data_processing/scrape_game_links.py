import requests
from bs4 import BeautifulSoup

games = []

for i in range(1, 18):
    URL = f'https://www.pro-football-reference.com/years/2019/week_{i}.htm'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='content')
    game_links = results.find_all('td', class_='gamelink')
    games.append(game_links)

f = open("games.txt", "w+")
for i in games:
    for x in i:
        f.write(str(x) + ",")
    f.write("\n\n")
f.close()
