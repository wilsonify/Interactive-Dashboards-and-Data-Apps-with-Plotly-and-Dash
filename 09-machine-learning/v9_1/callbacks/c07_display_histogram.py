from dash import callback, Output, Input
from dash.dash_table import DataTable
from dash.exceptions import PreventUpdate
from plotly import express as px

from v9_1.read.population_df import poverty


@callback(Output('indicator_year_histogram', 'figure'),
          Output('table_histogram_output', 'children'),
          Input('hist_multi_year_selector', 'value'),
          Input('hist_indicator_dropdown', 'value'),
          Input('hist_bins_slider', 'value'))
def display_histogram(years, indicator, nbins):
    if (not years) or (not indicator):
        raise PreventUpdate
    df = poverty[poverty['year'].isin(years) & poverty['is_country']]
    fig = px.histogram(df, x=indicator, facet_col='year', color='year',
                       title=indicator + ' Histogram',
                       nbins=nbins,
                       facet_col_wrap=4, height=700)
    fig.for_each_xaxis(lambda axis: axis.update(title=''))
    fig.add_annotation(text=indicator, x=0.5, y=-0.12, xref='paper', yref='paper', showarrow=False)
    fig.layout.paper_bgcolor = '#E5ECF6'

    table = DataTable(columns=[{'name': col, 'id': col}
                               for col in df[['Country Name', 'year', indicator]].columns],
                      data=df[['Country Name', 'year', indicator]].to_dict('records'),

                      style_header={'whiteSpace': 'normal'},
                      fixed_rows={'headers': True},
                      virtualization=True,
                      style_table={'height': '400px'},

                      sort_action='native',
                      filter_action='native',
                      export_format='csv',
                      style_cell={'minWidth': '150px'}),

    return fig, table
