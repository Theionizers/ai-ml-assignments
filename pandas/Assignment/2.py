from pathlib import Path

import pandas as pd
df = pd.read_csv(Path(__file__).with_name("AB_NYC_2019.csv"))
q1 = df.groupby('room_type')['price'].transform(lambda x: x.quantile(0.25))
q3 = df.groupby('room_type')['price'].transform(lambda x: x.quantile(0.75))
i = q3 - q1
c = df[(df['price'] >= q1 - 1.5 * i) & (df['price'] <= q3 + 1.5 * i)]
o = df.groupby('room_type').size()
rem = o - c.groupby('room_type').size()
rep = pd.DataFrame({'orig': o, 'rem': rem, 'pct': (rem / o) * 100})
print(rep)
