import dash
import dash_bootstrap_components as dbc
import pandas as pd



poverty_data = pd.read_csv('../../data/PovStatsData.csv')
poverty = pd.read_csv('../../data/poverty.csv', low_memory=False)
gini = 'GINI index (World Bank estimate)'

regions = ['East Asia & Pacific', 'Europe & Central Asia',
           'Fragile and conflict affected situations', 'High income',
           'IDA countries classified as fragile situations', 'IDA total',
           'Latin America & Caribbean', 'Low & middle income', 'Low income',
           'Lower middle income', 'Middle East & North Africa',
           'Middle income', 'South Asia', 'Sub-Saharan Africa',
           'Upper middle income', 'World']

country_in_regions = poverty_data['Country Name'].isin(regions)
indicator_in_pop_total = poverty_data['Indicator Name'] == 'Population, total'
population_df = poverty_data[~country_in_regions & indicator_in_pop_total]

country_options = [{'label': country, 'value': country} for country in poverty_data['Country Name'].unique()]

year_options = [{'label': year, 'value': str(year)} for year in range(1974, 2019)]

gini_year_dropdown_options = [{'label': year, 'value': year} for year in poverty['year'].unique()]

gini_country_dropdown_options = [{'label': country, 'value': country} for country in poverty['Country Name'].unique()]
