from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).with_name("AB_NYC_2019.csv"))
s = df.groupby(['neighbourhood_group', 'neighbourhood']).agg(c=('id', 'count'), m=('price', 'median')).reset_index()
f = s[s['c'] >= 100]
r = f.sort_values(by=['neighbourhood_group', 'm'], ascending=[True, False]).groupby('neighbourhood_group').head(3)
print(r)
