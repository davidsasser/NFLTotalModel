from bs4 import BeautifulSoup
import os
import csv

with open('../data/game_stats_2019.csv', 'w', newline='') as data:
    game_data = csv.writer(data, delimiter=',',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
    game_data.writerow(['Week', 'HomeTeam', 'AwayTeam', 'Total', 'H-RushAtt', 'H-RushYards',
                                'H-PassYards', 'H-Turnover', 'A-RushAtt', 'A-RushYards', 'A-PassYards', 'A-Turnover', 'Result'])

    for subdir, dirs, files in os.walk('../data/2019'):
        for filename in files:
            filepath = "/" + subdir.split("\\")[1] + "/" + filename

            print(filepath)

            page = open("../data/2019/" + filepath, "r")
            soup = BeautifulSoup(page, 'lxml')
            game_info = soup.find(id='div_game_info')
            week = subdir.split("\\")[1]

            total = game_info.find_all('td')[-1]
            team_stats = soup.find(id='team_stats')
            stats = team_stats.find_all('td')
            vis_name = team_stats.find_all('th', {"data-stat": "vis_stat"})
            home_name = team_stats.find_all('th', {"data-stat": "home_stat"})
            vis_stats = team_stats.find_all('td', {"data-stat": "vis_stat"})
            home_stats = team_stats.find_all('td', {"data-stat": "home_stat"})

            page.close()

            # print(str(vis_name[0].text))
            # print("-----------------------------")
            # print(str(vis_stats))
            # print("-----------------------------")
            # print(str(home_name[0].text))
            # print("-----------------------------")
            # print(str(home_stats))
            # print("-----------------------------")
            # print(str(total.text))

            total = total.text
            if(total.split(" ")[1] == "(under)"):
                result = -1
            elif(total.split(" ")[1] == "(over)"):
                result = 1
            else:
                result = 0

            game_data.writerow([week, str(home_name[0].text), str(vis_name[0].text), total.split(" ")[0], str(home_stats[1].text.split("-")[0]), str(home_stats[1].text.split("-")[1]), str(
                home_stats[2].text.split("-")[2]), str(home_stats[7].text), str(vis_stats[1].text.split("-")[0]), str(vis_stats[1].text.split("-")[1]), str(vis_stats[2].text.split("-")[2]), str(vis_stats[7].text), result])
