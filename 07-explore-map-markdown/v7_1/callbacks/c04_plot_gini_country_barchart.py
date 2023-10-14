from dash import callback, Output, Input
from dash.exceptions import PreventUpdate
from plotly import express as px

from v7_1.read.population_df import gini, gini_df


@callback(Output('gini_country_barchart', 'figure'), Input('gini_country_dropdown', 'value'))
def plot_gini_country_barchart(countries):
    if not countries:
        raise PreventUpdate
    df = gini_df[gini_df['Country Name'].isin(countries)].dropna(subset=[gini])
    fig = px.bar(df,
                 x='year',
                 y=gini,
                 height=100 + (250 * len(countries)),
                 facet_row='Country Name',
                 color='Country Name',
                 labels={gini: 'Gini Index'},
                 title=''.join([gini, '<br><b>', ', '.join(countries), '</b>']))
    fig.layout.paper_bgcolor = '#E5ECF6'
    return fig
