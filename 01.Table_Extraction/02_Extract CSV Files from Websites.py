import pandas as pd

# https://www.football-data.co.uk/englandm.php

# reading 1 csv file from the website
df_premier23 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')
# showing dataframe
df_premier23.rename(columns={'PCAHA':'home_goals'}, inplace = True)
print(df_premier23)