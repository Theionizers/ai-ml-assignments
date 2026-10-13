from pathlib import Path

import pandas as pd
df = pd.read_csv(Path(__file__).with_name("AB_NYC_2019.csv"))
df['pq'] = pd.qcut(df['price'], 4, duplicates='drop')
s = df.groupby(['neighbourhood_group', 'room_type', 'pq']).agg(
    c=('id', 'count'),
    mp=('price', 'median'),
    amn=('minimum_nights', 'mean'),
    arp=('reviews_per_month', 'mean'),
    aa=('availability_365', 'mean')
)
r = s[s['c'] >= 30].sort_values(by='arp', ascending=False)
print(r)
