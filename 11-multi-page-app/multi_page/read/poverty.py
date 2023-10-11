import pandas as pd

regions = ['East Asia & Pacific', 'Europe & Central Asia',
           'Fragile and conflict affected situations', 'High income',
           'IDA countries classified as fragile situations', 'IDA total',
           'Latin America & Caribbean', 'Low & middle income', 'Low income',
           'Lower middle income', 'Middle East & North Africa',
           'Middle income', 'South Asia', 'Sub-Saharan Africa',
           'Upper middle income', 'World']
poverty_data = pd.read_csv('../data/PovStatsData.csv')
poverty = pd.read_csv('../data/poverty.csv', low_memory=False)

population_df = poverty_data[
    ~poverty_data['Country Name'].isin(regions) &
    (poverty_data['Indicator Name'] == 'Population, total')]

perc_pov_cols = poverty.filter(regex='Poverty gap').columns
perc_pov_df = poverty[poverty['is_country']].dropna(subset=perc_pov_cols)
perc_pov_years = sorted(set(perc_pov_df['year']))

gini = 'GINI index (World Bank estimate)'
gini_df = poverty[poverty[gini].notna()]

country_df = pd.read_csv('../data/PovStatsCountry.csv').drop(['Unnamed: 30'], axis=1)
countries = poverty[poverty['is_country']]['Country Name'].drop_duplicates().sort_values().tolist()
