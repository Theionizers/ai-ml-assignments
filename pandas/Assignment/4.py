from pathlib import Path

import pandas as pd

d = pd.read_csv(Path(__file__).with_name("AB_NYC_2019.csv"))
b = [-1, 50, 100, 200, 500, float('inf')]
l = ['$0-50', '$51-100', '$101-200', '$201-500', 'above $500']
d['pb'] = pd.cut(d['price'], bins=b, labels=l)
d['ab'] = pd.cut(d['availability_365'], 4)
r = d.pivot_table(index='pb', columns='ab', values='price', aggfunc=['median', 'count'])
print(r)
