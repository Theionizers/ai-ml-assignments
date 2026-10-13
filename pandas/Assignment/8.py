from pathlib import Path

import pandas as pd
d = pd.read_csv(Path(__file__).with_name("AB_NYC_2019.csv"))
d['lat'] = pd.cut(d['latitude'], 20)
d['long'] = pd.cut(d['longitude'], 20)
s = d.groupby(['lat', 'long']).agg(c=('id', 'count'), m=('price', 'median'), a=('availability_365', 'mean'))
r = s[s['c'] >= 20].sort_values(by='m', ascending=False).head(10)
print(r)
