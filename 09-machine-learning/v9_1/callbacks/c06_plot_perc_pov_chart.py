from dash import callback, Output, Input
from dash.exceptions import PreventUpdate
from plotly import express as px

from v9_1.read.population_df import perc_pov_cols, perc_pov_df


@callback(Output('perc_pov_scatter_chart', 'figure'),
          Input('perc_pov_year_slider', 'value'),
          Input('perc_pov_indicator_slider', 'value'))
def plot_perc_pov_chart(year, indicator):
    indicator = perc_pov_cols[indicator]
    df = (perc_pov_df
          [perc_pov_df['year'].eq(year)]
          .dropna(subset=[indicator])
          .sort_values(indicator))
    if df.empty:
        raise PreventUpdate

    fig = px.scatter(df,
                     x=indicator,
                     y='Country Name',
                     color='Population, total',
                     size=[30] * len(df),
                     size_max=15,
                     hover_name='Country Name',
                     height=250 + (20 * len(df)),
                     color_continuous_scale='cividis',
                     title=indicator + '<b>: ' + f'{year}' + '</b>')
    fig.layout.paper_bgcolor = '#E5ECF6'
    fig.layout.xaxis.ticksuffix = '%'
    return fig
