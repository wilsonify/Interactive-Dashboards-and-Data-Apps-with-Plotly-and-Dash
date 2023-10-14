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

income_share_df.columns = [re.sub('\d Income share held by ', '', col).title()
                           for col in income_share_df.columns]
income_share_cols = income_share_df.columns[:-2]

country_options = [{'label': country, 'value': country} for country in poverty_data['Country Name'].unique()]
year_options = [{'label': year, 'value': str(year)} for year in range(1974, 2019)]
gini_year_dropdown_options = [{'label': year, 'value': year} for year in poverty['year'].unique()]
gini_country_dropdown_options = [{'label': country, 'value': country} for country in poverty['Country Name'].unique()]
income_share_country_dropdown_options = [{'label': country, 'value': country} for country in
                                         income_share_df['Country Name'].unique()]
