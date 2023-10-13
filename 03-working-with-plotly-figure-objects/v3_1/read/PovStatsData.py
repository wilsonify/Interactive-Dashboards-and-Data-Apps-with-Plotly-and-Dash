import pandas as pd

poverty_data = pd.read_csv('../../data/PovStatsData.csv')
regions = [
    'East Asia & Pacific', 'Europe & Central Asia', 'Fragile and conflict affected situations', 'High income',
    'IDA countries classified as fragile situations', 'IDA total', 'Latin America & Caribbean', 'Low & middle income',
    'Low income', 'Lower middle income', 'Middle East & North Africa', 'Middle income', 'South Asia',
    'Sub-Saharan Africa', 'Upper middle income', 'World'
]
is_in_region = poverty_data['Country Name'].isin(regions)
is_pop_total = poverty_data['Indicator Name'] == 'Population, total'
population_df = poverty_data[~is_in_region & is_pop_total]
country_options = [{'label': country, 'value': country} for country in poverty_data['Country Name'].unique()]
year_options = [{'label': year, 'value': str(year)} for year in range(1974, 2019)]
