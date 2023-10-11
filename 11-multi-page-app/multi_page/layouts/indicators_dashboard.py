import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from multi_page.read.income_share import income_share_df
from multi_page.read.poverty import poverty, gini_df, perc_pov_years
from multi_page.utils.make_empty_fig import make_empty_fig

cividis0 = px.colors.sequential.Cividis[0]

indicators_dashboard = html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Poverty And Equity Database'),
        html.H2('The World Bank'),

    ], style={'textAlign': 'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col([
            dbc.Tabs([
                dbc.Tab([
                    html.Br(),
                    dcc.Dropdown(id='indicator_dropdown',
                                 value='GINI index (World Bank estimate)',
                                 options=[{'label': indicator,
                                           'value': indicator}
                                          for indicator in poverty.columns[3:54]]),
                    dcc.Graph(id='indicator_map_chart'),
                    dcc.Markdown(id='indicator_map_details_md',
                                 style={'backgroundColor': '#E5ECF6'})
                ], label='Explore Metrics'),
                dbc.Tab([
                    html.Br(),
                    dbc.Row([
                        dbc.Col(lg=1),
                        dbc.Col([
                            dbc.Label('Select the year:'),
                            dcc.Slider(id='year_cluster_slider',
                                       min=1974, max=2018, step=1, included=False,
                                       value=2018,
                                       marks={year: str(year)
                                              for year in range(1974, 2019, 5)})
                        ], lg=6, md=12),
                        dbc.Col([
                            dbc.Label('Select the number of clusters:'),
                            dcc.Slider(id='ncluster_cluster_slider',
                                       min=2, max=15, step=1, included=False,
                                       value=2,
                                       marks={n: str(n) for n in range(2, 16)}),
                        ], lg=4, md=12)
                    ]),
                    html.Br(),
                    dbc.Row([
                        dbc.Col(lg=1),
                        dbc.Col([
                            dbc.Label('Select Indicators:'),
                            dcc.Dropdown(id='cluster_indicator_dropdown', optionHeight=40,
                                         multi=True,
                                         value=['Population, total'],
                                         options=[{'label': indicator, 'value': indicator}
                                                  for indicator in poverty.columns[3:54]]),
                        ], lg=6),
                        dbc.Col([
                            dbc.Label(''), html.Br(),
                            dbc.Button("Submit", id='clustering_submit_button'),
                        ]),
                    ]),
                    dcc.Loading([
                        dcc.Graph(id='clustered_map_chart')
                    ])
                ], label='Cluster Countries'),
            ]),
        ], lg=8)
    ]),
    html.Br(),
    html.Br(),
    html.Hr(),
    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col([
            dbc.Label('Indicator:'),
            dcc.Dropdown(id='hist_indicator_dropdown', optionHeight=40,
                         value='GINI index (World Bank estimate)',
                         options=[{'label': indicator, 'value': indicator}
                                  for indicator in poverty.columns[3:54]]),
        ], lg=5),
        dbc.Col([
            dbc.Label('Years:'),
            dcc.Dropdown(id='hist_multi_year_selector',
                         multi=True,
                         value=[2015],
                         placeholder='Select one or more years',
                         options=[{'label': year, 'value': year}
                                  for year in poverty['year'].drop_duplicates().sort_values()]),
        ], lg=3),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col([
            html.Br(),
            dbc.Label('Modify number of bins:'),
            dcc.Slider(id='hist_bins_slider',
                       dots=True, min=0, max=100, step=5, included=False,
                       marks={x: str(x) for x in range(0, 105, 5)}),
            dcc.Graph(id='indicator_year_histogram', figure=make_empty_fig()),
        ], lg=8)

    ]),

    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col([
            html.Div(id='table_histogram_output'),
            html.Br(), html.Br(),
        ], lg=8)
    ]),

    html.H2('Gini Index - World Bank Data', style={'textAlign': 'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col([
            dbc.Label('Year'),
            dcc.Dropdown(id='gini_year_dropdown',
                         placeholder='Select a year',
                         options=[{'label': year, 'value': year}
                                  for year in gini_df['year'].drop_duplicates().sort_values()]),
            html.Br(),
            dcc.Graph(id='gini_year_barchart',
                      figure=make_empty_fig())
        ], md=12, lg=5),
        dbc.Col([
            dbc.Label('Countries'),
            dcc.Dropdown(id='gini_country_dropdown',
                         placeholder='Select one or more countries',
                         multi=True,
                         options=[{'label': country, 'value': country}
                                  for country in gini_df['Country Name'].unique()]),
            html.Br(),
            dcc.Graph(id='gini_country_barchart',
                      figure=make_empty_fig())
        ], md=12, lg=5),
    ]),
    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col([
            html.Br(),
            html.H2('Income Share Distribution', style={'textAlign': 'center'}),
            html.Br(),
            dbc.Label('Country'),
            dcc.Dropdown(id='income_share_country_dropdown',
                         placeholder='Select a country',
                         options=[{'label': country, 'value': country}
                                  for country in income_share_df['Country Name'].unique()]),
            dcc.Graph(id='income_share_country_barchart',
                      figure=make_empty_fig())
        ], lg=8)
    ]),
    html.Br(),
    html.H2('Poverty Gap at $1.9, $3.2, and $5.5 (% of population)',
            style={'textAlign': 'center'}),
    html.Br(), html.Br(),

    dbc.Row([
        dbc.Col(lg=2),

        dbc.Col([
            dbc.Label('Select poverty level:'),
            dcc.Slider(id='perc_pov_indicator_slider',
                       min=0,
                       max=2,
                       step=1,
                       included=False,
                       value=0,
                       marks={0: {'label': '$1.9', 'style': {'color': cividis0, 'fontWeight': 'bold', 'fontSize': 15}},
                              1: {'label': '$3.2', 'style': {'color': cividis0, 'fontWeight': 'bold', 'fontSize': 15}},
                              2: {'label': '$5.5',
                                  'style': {'color': cividis0, 'fontWeight': 'bold', 'fontSize': 15}}}),
        ], lg=2),
        dbc.Col([
            dbc.Label('Select year:'),
            dcc.Slider(id='perc_pov_year_slider',
                       min=perc_pov_years[0],
                       max=perc_pov_years[-1],
                       step=1,
                       included=False,
                       value=2018,
                       marks={year: {'label': str(year),
                                     'style': {'color': cividis0, 'fontSize': 14}}
                              for year in perc_pov_years[::5]}),
        ], lg=5),
    ]),
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col([
            dcc.Graph(id='perc_pov_scatter_chart',
                      figure=make_empty_fig())
        ], lg=10)
    ]),
], style={'backgroundColor': '#E5ECF6'})
