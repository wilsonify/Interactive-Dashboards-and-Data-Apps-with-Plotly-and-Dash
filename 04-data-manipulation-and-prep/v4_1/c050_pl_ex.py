"""

Chapter 4 - Data Manipulation and Preparation, Paving the Way to `Plotly Express`

* Understanding long format (tidy) data
* Understanding the role of data manipulation skills
* Learning Plotly Express

"""

import pandas as pd
import plotly.express as px

# ## Learning Plotly Express


df = pd.DataFrame({
    'numbers': [1, 2, 3, 4, 5, 6, 7, 8],
    'colors': ['blue', 'green', 'orange', 'yellow', 'black', 'gray', 'pink', 'white'],
    'floats': [1.1, 1.2, 1.3, 2.4, 2.1, 5.6, 6.2, 5.3],
    'shapes': ['rectangle', 'circle', 'triangle', 'rectangle', 'circle', 'triangle', 'rectangle', 'circle'],
    'letters': list('AAABBCCC')
})

print(f"df = {df}")

px.scatter(
    df,
    x='numbers',
    y='floats'
)

px.scatter(
    df,
    x='numbers',
    y='floats',
    color='shapes',
    symbol='shapes'
)

px.scatter(
    df,
    x='numbers',
    y='floats',
    color='letters',
    symbol='letters',
    size=[35] * 8
)

print(f"df = {df}")

px.bar(df, x='letters', y='floats', color='shapes', barmode='group')
fig = px.scatter(x=[1, 2, 3], y=[23, 12, 34])
fig.add_annotation(x=1, y=23, text='This is the first value')
fig.write_html("bar_letters_vs_floats.html")
