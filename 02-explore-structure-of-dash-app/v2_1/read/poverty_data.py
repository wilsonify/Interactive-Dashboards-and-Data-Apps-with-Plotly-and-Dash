import pandas as pd

poverty_data = pd.read_csv('../../data/PovStatsData.csv')
country_name_unique = poverty_data['Country Name'].unique()
country_options = [
    {'label': country, 'value': country}
    for country in country_name_unique
]
