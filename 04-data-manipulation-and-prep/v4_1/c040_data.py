"""

Chapter 4 - Data Manipulation and Preparation, Paving the Way to `Plotly Express`

* Understanding long format (tidy) data
* Understanding the role of data manipulation skills
* Learning Plotly Express

"""

import pandas as pd
import plotly.express as px

from v4_1.c020_country import country

# ## Data

data = pd.read_csv('../../data/PovStatsData.csv')
data = data.drop('Unnamed: 50', axis=1)
print(data.shape)
data.sample(3)

df = pd.DataFrame({
    'country': ['country_A', 'country_B'],
    'indicator': ['indicator 1', 'indicator 1'],
    '2015': [100, 10],
    '2020': [120, 15]
})
df.style.set_caption('<b>Wide format</b>')

melted = df.melt(id_vars=['country', 'indicator'], value_vars=['2015', '2020'], var_name='year')
melted.style.set_caption('<b>Long (tidy) format</b>')

(melted
 .pivot(index=['year', 'indicator'],
        columns='country', values='value')
 .reset_index()
 .style.set_caption('<b>Pivoted (wide) format</b>'))

id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']
data_melt = pd.melt(data, id_vars=id_vars, var_name='year').dropna(subset=['value'])
data_melt['year'] = data_melt['year'].astype(int)
print(data_melt.shape)
data_melt.sample(10)

data_pivot = data_melt.pivot(index=['Country Name', 'Country Code', 'year'],
                             columns='Indicator Name',
                             values='value').reset_index()

print(data_pivot.shape)
data_pivot.sample(5)

data_pivot[['Country Code', 'year']].duplicated().any()

left = melted
left.style.set_caption('df: "left"')

right = pd.DataFrame({
    'country': ['country_A', 'country_B'],
    'continent': ['Asia', 'Europe'],
    'group': ['low income', 'high income']
})
right.style.set_caption('df: "right"')

pd.merge(left=left, right=right, left_on='country', right_on='country', how='left').style.set_caption('df: merged')

poverty = pd.merge(data_pivot, country, left_on='Country Code', right_on='Country Code', how='left')

# "High Income" is NA, so we fill it with False values, as it is not a country
poverty['is_country'] = poverty['is_country'].fillna(False)
print(poverty.shape)
poverty.iloc[:, list(range(4)) + list(range(55, 65))].sample(10)

poverty[['Country Code', 'year']].duplicated().any()

