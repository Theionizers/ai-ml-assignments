from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).with_name("AB_NYC_2019.csv"))

clean_df = df.dropna(subset=['neighbourhood', 'room_type', 'price', 'number_of_reviews']).copy()


group_median = clean_df.groupby(['neighbourhood', 'room_type'])['price'].transform('median')


clean_df['pct_difference'] = ((clean_df['price'] - group_median) / group_median) * 100


filtered_df = clean_df[clean_df['number_of_reviews'] >= 10]

top_overpriced = filtered_df.sort_values(by='pct_difference', ascending=False).head(20)

print(top_overpriced[['id', 'neighbourhood', 'room_type', 'price', 'pct_difference', 'number_of_reviews']])
