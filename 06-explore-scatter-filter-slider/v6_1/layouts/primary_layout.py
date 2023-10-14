import dash_bootstrap_components as dbc
from dash import html, dcc

from v6_1.read.population_df import (
    year_options,
    gini_year_dropdown_options,
    gini_country_dropdown_options,
    income_share_country_dropdown_options,
    perc_pov_indicator_slider_marks,
    perc_pov_years,
    perc_pov_year_slider_marks
)
from v6_1.utils.make_empty_fig import make_empty_fig

github_repo_url = 'https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash'
data_source_url = 'https://datacatalog.worldbank.org/dataset/poverty-and-equity-database'

primary_layout = html.Div([
    dbc.Col([
        html.H1('Poverty And Equity Database'), html.H2('The World Bank'), ],
        style={'textAlign': 'center'}),

    html.Br(),
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col([dcc.Dropdown(
            id='year_dropdown',
            value='2010',
            options=year_options
        ), dcc.Graph(id='population_chart'), ], lg=10
        )]),
    html.Br(),
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
            dcc.Graph(
                id='gini_year_barchart',
                figure=make_empty_fig()
            )
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
            dcc.Graph(
                id='gini_country_barchart',
                figure=make_empty_fig()
            )
        ], md=12, lg=5),
    ]),
    dbc.Row([
        dbc.Col(lg=1),
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
            dcc.Graph(
                id='income_share_country_barchart',
                figure=make_empty_fig()
            )
        ], lg=10)

    ]),
    html.Br(),
    html.H2('Poverty Gap at $1.9, $3.2, and $5.5 (% of population)', style={'textAlign': 'center'}),
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
            dcc.Graph(id='perc_pov_scatter_chart',
                      figure=make_empty_fig())
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
        ], label='Project Info')
    ]),

], style={'backgroundColor': '#E5ECF6'})
