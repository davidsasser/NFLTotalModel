import pandas as pd

teams = ['CHI', 'GNB', 'CAR', 'CLE', 'LAR', 'TEN', 'ARI', 'DET', 'DAL', 'NYG', 'JAX', 'KAN', 'MIA', 'BAL', 'MIN',
         'ATL', 'NWE', 'PIT', 'NYJ', 'BUF', 'PHI', 'WAS', 'LAC', 'IND', 'SEA', 'CIN', 'TAM', 'SFO', 'NOR', 'HOU', 'OAK', 'DEN']

df = pd.read_csv(r'../data/game_stats_2019.csv')

rushAtt = []
rushYards = []
passYards = []
turnovers = []

for x in range(6, 17):
    for i in teams:
        team_h = df.loc[df['HomeTeam'] == i]
        first_6_team_h = team_h.loc[df['Week'] < (x+1)]
        rushAtt_h = first_6_team_h['H-RushAtt'].sum()
        rushYards_h = first_6_team_h['H-RushYards'].sum()
        passYards_h = first_6_team_h['H-PassYards'].sum()
        turnover_h = first_6_team_h['H-Turnover'].sum()

        team_a = df.loc[df['AwayTeam'] == i]
        first_6_team_a = team_a.loc[df['Week'] < x]
        rushAtt_a = first_6_team_a['A-RushAtt'].sum()
        rushYards_a = first_6_team_a['A-RushYards'].sum()
        passYards_a = first_6_team_a['A-PassYards'].sum()
        turnover_a = first_6_team_a['A-Turnover'].sum()

        num_of_games = len(pd.concat([first_6_team_a, first_6_team_h]))

        rushAtt.append((rushAtt_a + rushAtt_h) / num_of_games)
        rushYards.append((rushYards_a + rushYards_h) / num_of_games)
        passYards.append((passYards_a + passYards_h) / num_of_games)
        turnovers.append((turnover_a + turnover_h) / num_of_games)

    data = {'Name': teams, 'RushAtt': rushAtt, 'rushYards': rushYards,
            'passYards': passYards, 'Turnovers': turnovers}

    # Create DataFrame
    week_df = pd.DataFrame(data)

    week_df.to_csv(f'../data/week{str(x)}.csv', index=False)

    rushAtt = []
    rushYards = []
    passYards = []
    turnovers = []
