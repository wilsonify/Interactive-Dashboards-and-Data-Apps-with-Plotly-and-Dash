import re

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

poverty_data = pd.read_csv('../../data/PovStatsData.csv')
poverty = pd.read_csv('../../data/poverty.csv', low_memory=False)

gini = 'GINI index (World Bank estimate)'
gini_df = poverty[poverty[gini].notna()]

regions = ['East Asia & Pacific', 'Europe & Central Asia',
           'Fragile and conflict affected situations', 'High income',
           'IDA countries classified as fragile situations', 'IDA total',
           'Latin America & Caribbean', 'Low & middle income', 'Low income',
           'Lower middle income', 'Middle East & North Africa',
           'Middle income', 'South Asia', 'Sub-Saharan Africa',
           'Upper middle income', 'World']

population_df = poverty_data[~poverty_data['Country Name'].isin(regions) &
                             (poverty_data['Indicator Name'] == 'Population, total')]

income_share_df = poverty.filter(regex='Country Name|^year$|Income share.*?20').dropna()
income_share_df = income_share_df.rename(columns={
    'Income share held by lowest 20%': '1 Income share held by lowest 20%',
    'Income share held by second 20%': '2 Income share held by second 20%',
    'Income share held by third 20%': '3 Income share held by third 20%',
    'Income share held by fourth 20%': '4 Income share held by fourth 20%',
    'Income share held by highest 20%': '5 Income share held by highest 20%'
}).sort_index(axis=1)

income_share_df.columns = [re.sub(r'\d Income share held by ', '', col).title()
                           for col in income_share_df.columns]
income_share_cols = income_share_df.columns[:-2]

perc_pov_cols = poverty.filter(regex='Poverty gap').columns
perc_pov_df = poverty[poverty['is_country']].dropna(subset=perc_pov_cols)
perc_pov_years = sorted(set(perc_pov_df['year']))

cividis0 = px.colors.sequential.Cividis[0]
perc_pov_year_slider_marks = {year: {'label': str(year), 'style': {'color': cividis0, 'fontSize': 14}} for year in
                              perc_pov_years[::5]}
perc_pov_indicator_slider_marks = {
    0: {'label': '$1.9', 'style': {'color': cividis0, 'fontWeight': 'bold', 'fontSize': 15}},
    1: {'label': '$3.2', 'style': {'color': cividis0, 'fontWeight': 'bold', 'fontSize': 15}},
    2: {'label': '$5.5',
        'style': {'color': cividis0, 'fontWeight': 'bold', 'fontSize': 15}}}
year_options = [{'label': year, 'value': str(year)} for year in range(1974, 2019)]
gini_year_dropdown_options = [{'label': year, 'value': year} for year in
                              gini_df['year'].drop_duplicates().sort_values()]
gini_country_dropdown_options = [{'label': country, 'value': country} for country in gini_df['Country Name'].unique()]
income_share_country_dropdown_options = [{'label': country, 'value': country} for country in
                                         income_share_df['Country Name'].unique()]
