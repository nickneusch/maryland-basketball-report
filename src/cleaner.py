import pandas as pd

df1 = pd.read_csv('kenpom.csv')
df2 = pd.read_csv('shot_chart.csv')

def split_wl_column(df):
    # Split the W-L column into two separate columns for Wins and Losses
    df[['W', 'L']] = df['W-L'].str.split('-', expand=True)
    
    # Convert the Wins and Losses columns to integers
    df['W'] = pd.to_numeric(df['W'], errors='coerce')
    df['L'] = pd.to_numeric(df['L'], errors='coerce')
    
    return df

df1 = split_wl_column(df1)

print(df1)


df1.to_csv('new_kenpom.csv', index=False)
df2.to_csv('new_shot_chart.csv', index=False)

