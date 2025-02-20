import pandas as pd

df1 = pd.read_csv('Big10 CSVs/big10_players_pg_min20.csv')

df1 = df1.fillna(0)

df1.to_csv('Big10 CSVs/new_big10_players_pg_min20.csv', index=False)