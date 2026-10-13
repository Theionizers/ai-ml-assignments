from pathlib import Path

import pandas as pd
df = pd.read_csv(Path(__file__).with_name("AB_NYC_2019.csv"))
h = df.groupby('host_id').agg(tot=('id', 'count'), avg_p=('price', 'mean'), med_p=('price', 'median'), tot_a=('availability_365', 'sum')).reset_index()
f = h[h['tot'] >= 5]
r = f.sort_values(by=['tot', 'med_p'], ascending=[False, False]).head(10)
print(r)
