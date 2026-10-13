from pathlib import Path

import pandas as pd
df= pd.read_csv(Path(__file__).with_name("AB_NYC_2019.csv"))
h = df.groupby('host_id').size().reset_index(name='cnt')
h['cat'] = h['cnt'].apply(lambda x: 'large' if x >= 10 else 'small')
m = pd.merge(df, h[['host_id', 'cat']], on='host_id')
r = m.groupby('cat').agg(mp=('price', 'median'), ar=('reviews_per_month', 'mean'), aa=('availability_365', 'mean'))
print(r)
