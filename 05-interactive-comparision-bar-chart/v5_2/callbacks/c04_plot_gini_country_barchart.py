from dash import callback, Output, Input
from dash.exceptions import PreventUpdate
from plotly import express as px

from v5_2.read.population_df import poverty, gini


@callback(Output('gini_country_barchart', 'figure'), Input('gini_country_dropdown', 'value'))
def plot_gini_country_barchart(country):
    if not country:
        raise PreventUpdate
    df = poverty[poverty['Country Name'] == country].dropna(subset=[gini])
    fig = px.bar(df,
                 x='year',
                 y=gini,
                 title=' - '.join([gini, country]))
    return fig
