import requests
from bs4 import BeautifulSoup

games = []

fr = open("games.txt", "r")
lines = fr.readlines()
week = 0

for i in lines:
    if(i == '\n'):
        continue
    elif(i == "Week\n"):
        week += 1
    else:
        URL = f'https://www.pro-football-reference.com{i.strip()}'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        fw = open(
            f'../data/2019/w{str(week)}/{i.strip().split("/")[2]}.html', "w+")
        fw.write(str(soup))
        fw.close()
        # game_info = soup.find(id='div_game_info')
        # print(game_info)
        # total = game_info.find_all('tr', {"data-row": "7"})
        # team_stats = soup.find(id='team_stats')
        # stats = team_stats.find_all('th', {"data-stat": "stat"})
        # vis_name = team_stats.find_all('th', {"data-stat": "vis_stat"})
        # home_name = team_stats.find_all('th', {"data-stat": "home_stat"})
        # vis_stats = team_stats.find_all('tr', {"data-stat": "vis_stat"})
        # home_stats = team_stats.find_all('tr', {"data-stat": "home_stat"})

# print(str(vis_name))
# print(str(vis_stats))
# print(str(home_name))
# print(str(home_stats))
# print(str(total))

fr.close()

# for i in range(1, 18):
#     URL = f'https://www.pro-football-reference.com/{i}'
#     page = requests.get(URL)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     results = soup.find(id='content')
#     game_links = results.find_all('td', class_='gamelink')
#     games.append(game_links)

# f = open("games.txt", "w+")
# for i in games:
#     for x in i:
#         f.write(str(x) + ",")
#     f.write("\n\n")
# f.close()
