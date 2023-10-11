from dash import callback, Output, Input
from dash.exceptions import PreventUpdate
from plotly import express as px

from multi_page.read.poverty import gini_df, gini


@callback(Output('gini_year_barchart', 'figure'),
          Input('gini_year_dropdown', 'value'))
def plot_gini_year_barchart(year):
    if not year:
        raise PreventUpdate
    df = gini_df[gini_df['year'].eq(year)].sort_values(gini).dropna(subset=[gini])
    n_countries = len(df['Country Name'])
    fig = px.bar(df,
                 x=gini,
                 y='Country Name',
                 orientation='h',
                 height=200 + (n_countries * 20),
                 title=gini + ' ' + str(year))
    fig.layout.paper_bgcolor = '#E5ECF6'
    return fig
