import dash_bootstrap_components as dbc
from dash import html, dcc

from v9_1.read.population_df import indicator_dropdown_options, year_cluster_slider_marks, \
    ncluster_cluster_slider_marks, cluster_indicator_dropdown_options, hist_indicator_dropdown_options, \
    hist_multi_year_selector_options, hist_bins_slider_marks, gini_year_dropdown_options, gini_country_dropdown_options, \
    income_share_country_dropdown_options, perc_pov_indicator_slider_marks, perc_pov_years, perc_pov_year_slider_marks, \
    data_source_url, github_repo_url
from v9_1.utils.make_empty_fig import make_empty_fig

primary_layout = html.Div([
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
                    dcc.Dropdown(
                        id='indicator_dropdown',
                        value='GINI index (World Bank estimate)',
                        options=indicator_dropdown_options
                    ),
                    dcc.Graph(id='indicator_map_chart'),
                    dcc.Markdown(id='indicator_map_details_md', style={'backgroundColor': '#E5ECF6'})
                ], label='Explore Metrics'),
                dbc.Tab([
                    ##########################################
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Select the year:'),
                            dcc.Slider(
                                id='year_cluster_slider',
                                min=1974, max=2018, step=1, included=False,
                                value=2018,
                                marks=year_cluster_slider_marks
                            )
                        ], lg=7, md=12),
                        dbc.Col([
                            dbc.Label('Select the number of clusters:'),
                            dcc.Slider(
                                id='ncluster_cluster_slider',
                                min=2, max=15, step=1, included=False,
                                value=4,
                                marks=ncluster_cluster_slider_marks
                            ),
                        ], lg=5, md=12)
                    ]),
                    html.Br(),
                    dbc.Label('Select Indicators:'),
                    dcc.Dropdown(
                        id='cluster_indicator_dropdown',
                        optionHeight=40,
                        multi=True,
                        value=['GINI index (World Bank estimate)'],
                        options=cluster_indicator_dropdown_options
                    ),
                    html.Br(),
                    dcc.Graph(id='clustered_map_chart')

                    ##########################################

                ], label='Cluster Countries'),
            ]),

        ], lg=8)
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col([
            dbc.Label('Indicator:'),
            dcc.Dropdown(
                id='hist_indicator_dropdown',
                optionHeight=40,
                value='GINI index (World Bank estimate)',
                options=hist_indicator_dropdown_options
            ),
        ], lg=5),
        dbc.Col([
            dbc.Label('Years:'),
            dcc.Dropdown(
                id='hist_multi_year_selector',
                multi=True,
                value=[2015],
                placeholder='Select one or more years',
                options=hist_multi_year_selector_options
            ),
        ], lg=3),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col([
            html.Br(),
            dbc.Label('Modify number of bins:'),
            dcc.Slider(
                id='hist_bins_slider',
                dots=True, min=0, max=100, step=5, included=False,
                marks=hist_bins_slider_marks
            ),
            dcc.Graph(id='indicator_year_histogram', figure=make_empty_fig()),
        ], lg=8)

    ]),

    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col([
            html.Div(id='table_histogram_output'),
            html.Br(), html.Br(),
        ], lg=7)
    ]),

    html.H2('Gini Index - World Bank Data', style={'textAlign': 'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col([
            dbc.Label('Year'),
            dcc.Dropdown(
                id='gini_year_dropdown',
                placeholder='Select a year',
                options=gini_year_dropdown_options
            ),
            html.Br(),
            dcc.Graph(id='gini_year_barchart',
                      figure=make_empty_fig())
        ], md=12, lg=5),
        dbc.Col([
            dbc.Label('Countries'),
            dcc.Dropdown(
                id='gini_country_dropdown',
                placeholder='Select one or more countries',
                multi=True,
                options=gini_country_dropdown_options
            ),
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
            dcc.Dropdown(
                id='income_share_country_dropdown',
                placeholder='Select a country',
                options=income_share_country_dropdown_options
            ),
            dcc.Graph(id='income_share_country_barchart', figure=make_empty_fig())
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
            dcc.Slider(
                id='perc_pov_indicator_slider',
                min=0,
                max=2,
                step=1,
                included=False,
                value=0,
                marks=perc_pov_indicator_slider_marks
            ),
        ], lg=2),
        dbc.Col([
            dbc.Label('Select year:'),
            dcc.Slider(
                id='perc_pov_year_slider',
                min=perc_pov_years[0],
                max=perc_pov_years[-1],
                step=1,
                included=False,
                value=2018,
                marks=perc_pov_year_slider_marks
            ),
        ], lg=5),
    ]),
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col([
            dcc.Graph(id='perc_pov_scatter_chart', figure=make_empty_fig())
        ], lg=10)
    ]),

    dbc.Tabs([
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Number of Economies: 170'),
                html.Li('Temporal Coverage: 1974 - 2019'),
                html.Li('Update Frequency: Quarterly'),
                html.Li('Last Updated: March 18, 2020'),
                html.Li(['Source: ', html.A(data_source_url, href=data_source_url)])
            ])
        ], label='Key Facts'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Book title: Interactive Dashboards and Data Apps with Plotly and Dash'),
                html.Li(['GitHub repo: ', html.A(github_repo_url, href=github_repo_url)])
            ])
        ], label='Poject Info')
    ]),
], style={'backgroundColor': '#E5ECF6'})
