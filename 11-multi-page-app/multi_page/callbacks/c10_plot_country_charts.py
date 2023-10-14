from urllib.parse import unquote

import dash_bootstrap_components as dbc
from dash import html
from dash import callback, Output, Input
from dash.exceptions import PreventUpdate
from plotly import express as px

from multi_page.read.poverty import poverty, country_df


@callback(Output('country_heading', 'children'),
          Output('country_page_graph', 'figure'),
          Output('country_table', 'children'),
          Input('location', 'pathname'),
          Input('country_page_contry_dropdown', 'value'),
          Input('country_page_indicator_dropdown', 'value'))
def plot_country_charts(pathname, countries, indicator):
    country = "unknown"
    if (not countries) or (not indicator):
        raise PreventUpdate
    if unquote(pathname[1:]) in countries:
        country = unquote(pathname[1:])
    df = poverty[poverty['is_country'] & poverty['Country Name'].isin(countries)]
    fig = px.line(df,
                  x='year',
                  y=indicator,
                  title='<b>' + indicator + '</b><br>' + ', '.join(countries),
                  color='Country Name')
    fig.layout.paper_bgcolor = '#E5ECF6'
    table = country_df[country_df['Short Name'] == countries[0]].T.reset_index()
    if table.shape[1] == 2:
        table.columns = [countries[0] + ' Info', '']
        table = dbc.Table.from_dataframe(table)
    else:
        table = html.Div([html.Br() for i in range(20)])
    return country + ' Poverty Data', fig, table
