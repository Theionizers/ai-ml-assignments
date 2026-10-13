from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).with_name("AB_NYC_2019.csv"))
df['last_review'] = pd.to_datetime(df['last_review'])
x = df[df['number_of_reviews'] >= 5]
y = x.groupby('neighbourhood').agg(c=('id', 'count'), m=('reviews_per_month', 'median'))
r = y[y['c'] >= 50].sort_values(by='m', ascending=False).head(10)
print(r)
