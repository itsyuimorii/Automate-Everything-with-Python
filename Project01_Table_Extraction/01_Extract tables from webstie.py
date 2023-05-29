import pandas as pd
simpsons_list= pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')

print(len(simpsons_list))

print(simpsons_list[1])