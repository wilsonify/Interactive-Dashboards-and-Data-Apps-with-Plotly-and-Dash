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
regions = [
    'East Asia & Pacific', 'Europe & Central Asia', 'Fragile and conflict affected situations', 'High income',
    'IDA countries classified as fragile situations', 'IDA total', 'Latin America & Caribbean', 'Low & middle income',
    'Low income', 'Lower middle income', 'Middle East & North Africa', 'Middle income', 'South Asia',
    'Sub-Saharan Africa', 'Upper middle income', 'World'
]
is_in_region = poverty_data['Country Name'].isin(regions)
is_pop_total = poverty_data['Indicator Name'] == 'Population, total'

population_df = poverty_data[~is_in_region & is_pop_total]
population_dol = df2dol(population_df)
json.dump(population_dol, open("populationData.json", "w"))

population_sample_df = population_df.head(5)
population_sample_dol = df2dol(population_sample_df)
json.dump(population_sample_dol, open("populationDataSample.json", "w"))
