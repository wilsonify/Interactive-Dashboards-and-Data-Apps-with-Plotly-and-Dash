import json

import pandas as pd


def nan2none(obj):
    if pd.isnull(obj):
        return None
    else:
        return obj


def df2dol(df):
    dol = {}
    for col in df.columns:
        col_list = df[col].to_list()
        col_list = [nan2none(_) for _ in col_list]
        dol[col] = col_list
    return dol


poverty_data = pd.read_csv('../../../data/PovStatsData.csv')
country_name_unique = poverty_data['Country Name'].unique()
country_options = [
    {'label': country, 'value': country}
    for country in country_name_unique
]

poverty_dol = df2dol(poverty_data)
json.dump(poverty_dol, open("PovStatsData.json", "w"))

poverty_sample_df = poverty_data.head(5)
poverty_sample_dol = df2dol(poverty_sample_df)
json.dump(poverty_sample_dol, open("PovStatsDataSample.json", "w"))
