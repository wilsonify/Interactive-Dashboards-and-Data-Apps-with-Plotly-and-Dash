from dash import callback, Output, Input
from dash.exceptions import PreventUpdate
from plotly import express as px

from v5_3.read.population_df import income_share_df, income_share_cols


@callback(Output('income_share_country_barchart', 'figure'), Input('income_share_country_dropdown', 'value'))
def plot_income_share_barchart(country):
    if country is None:
        raise PreventUpdate
    fig = px.bar(income_share_df[income_share_df['Country Name'] == country].dropna(),
                 x=income_share_cols,
                 y='Year',
                 barmode='stack',
                 height=600,
                 hover_name='Country Name',
                 title=f'Income Share Quintiles - {country}',
                 orientation='h',
                 )
    fig.layout.legend.title = None
    fig.layout.legend.orientation = 'h'
    fig.layout.legend.x = 0.2
    fig.layout.xaxis.title = 'Percent of Total Income'
    fig.layout.paper_bgcolor = '#E5ECF6'
    fig.layout.plot_bgcolor = '#E5ECF6'
    return fig
