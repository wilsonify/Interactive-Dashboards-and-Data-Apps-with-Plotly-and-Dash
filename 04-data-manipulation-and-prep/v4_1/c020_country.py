"""

Chapter 4 - Data Manipulation and Preparation, Paving the Way to `Plotly Express`

* Understanding long format (tidy) data
* Understanding the role of data manipulation skills
* Learning Plotly Express

"""
from unicodedata import lookup

import pandas as pd
import plotly.express as px

# ## Country

country = pd.read_csv('../../data/PovStatsCountry.csv', na_values='', keep_default_na=False)
print(country.shape)
country.head()

region_isna_short_name = country[country['Region'].isna()]['Short Name']
print(f"region_isna_short_name = {region_isna_short_name}")

country['Region'].value_counts(dropna=False).to_frame()

country['is_country'] = country['Region'].notna()
country[['Short Name', 'Region', 'is_country']].sample(10)

income_group_counts = country['Income Group'].value_counts(dropna=False)
print(f"income_group_counts = {income_group_counts}")

px.bar(y=income_group_counts,
       x=income_group_counts.index.astype(str),
       title='Number of countries per income group')

country_codes = country[country['is_country']]['2-alpha code'].dropna().str.lower().tolist()

lookup('REGIONAL INDICATOR SYMBOL LETTER A')


def flag(letters):
    if pd.isna(letters):
        return ''
    if letters.lower() not in country_codes:
        return ''
    l0 = lookup(f'REGIONAL INDICATOR SYMBOL LETTER {letters[0]}')
    l1 = lookup(f'REGIONAL INDICATOR SYMBOL LETTER {letters[1]}')
    return f"{l0}{l1}"


print(*[flag(c) for c in country_codes])

country['flag'] = [flag(code) for code in country['2-alpha code']]

country[['Short Name', 'flag', 'is_country']].sample(10)

country_series = pd.read_csv('../../data/PovStatsCountry-Series.csv')
print(country_series.shape)
country_series.head()
