from pathlib import Path

import pandas as pd


df = pd.read_csv(Path(__file__).with_name("AB_NYC_2019.csv"))


missing_count = df.isnull().sum()
missing_percentage = (missing_count / len(df)) * 100

missing_summary = pd.DataFrame({
    'Missing Count': missing_count,
    'Missing Percentage': missing_percentage
})

print("missing values:")
print(missing_summary[missing_summary['Missing Count'] > 0])


df['reviews_per_month_imputed'] = df['reviews_per_month']


global_median = df['reviews_per_month'].median()


neigh_medians = df.groupby('neighbourhood')['reviews_per_month'].median().reset_index()
neigh_medians = neigh_medians.rename(columns={'reviews_per_month': 'neigh_median'})


df = pd.merge(df, neigh_medians, on='neighbourhood', how='left')


df['reviews_per_month_imputed'] = df['reviews_per_month_imputed'].fillna(df['neigh_median'])
df['reviews_per_month_imputed'] = df['reviews_per_month_imputed'].fillna(global_median)


print("\nMissing comparison:")
print("Before imputation missing count:", df['reviews_per_month'].isnull().sum())
print("After imputation missing count:", df['reviews_per_month_imputed'].isnull().sum())
