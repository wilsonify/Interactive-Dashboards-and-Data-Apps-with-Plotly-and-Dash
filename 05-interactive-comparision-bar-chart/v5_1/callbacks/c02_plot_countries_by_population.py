from dash import callback, Output, Input
from plotly import graph_objects as go

from v5_1.read.population_df import population_df


@callback(Output('population_chart', 'figure'),
          Input('year_dropdown', 'value'))
def plot_countries_by_population(year):
    fig = go.Figure()
    year_df = population_df[['Country Name', year]].sort_values(year, ascending=False)[:20]
    fig.add_bar(x=year_df['Country Name'],
                y=year_df[year])
    fig.layout.title = f'Top twenty countries by population - {year}'
    return fig
