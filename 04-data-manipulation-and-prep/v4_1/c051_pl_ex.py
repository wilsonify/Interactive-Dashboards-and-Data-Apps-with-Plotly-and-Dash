"""

Chapter 4 - Data Manipulation and Preparation, Paving the Way to `Plotly Express`

* Understanding long format (tidy) data
* Understanding the role of data manipulation skills
* Learning Plotly Express

"""

import plotly.express as px

from v4_1.c040_data import poverty

# ## Learning Plotly Express


poverty.head(2)

year = 2015
indicator = 'Income share held by lowest 10%'
grouper = 'Region'

df = (
    poverty[poverty['year'].eq(year)]
    .sort_values(indicator)
    .dropna(subset=[indicator, grouper])
)

income_share_p10_vs_country = px.scatter(
    df,
    x=indicator,
    y='Country Name',
    color=grouper,
    symbol=grouper,
    facet_row=grouper,
    log_x=True,
    hover_name=df['Short Name'] + ' ' + df['flag'],
    size=[1] * len(df),
    template='ggplot2',
    title=' '.join([indicator, 'by', grouper, str(year)]),
    height=1500,
    width=1300
)

income_share_p10_vs_country.write_html("income_share_p10_vs_country.html")
