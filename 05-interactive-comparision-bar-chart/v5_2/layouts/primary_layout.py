import dash_bootstrap_components as dbc
from dash import html, dcc

from v5_2.read.population_df import (
    country_options,
    year_options,
    gini_year_dropdown_options,
    gini_country_dropdown_options,
    income_share_country_dropdown_options
)

primary_layout = html.Div([
    html.H1('Poverty And Equity Database'),
    html.H2('The World Bank'),
    dcc.Dropdown(id='country', options=country_options),
    html.Br(),
    html.Div(id='report'),
    html.Br(),
    dcc.Dropdown(id='year_dropdown', value='2010', options=year_options),
    dcc.Graph(id='population_chart'),
    html.Br(),
    html.H2('Gini Index - World Bank Data', style={'textAlign': 'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='gini_year_dropdown', options=gini_year_dropdown_options),
            html.Br(),
            dcc.Graph(id='gini_year_barchart')
        ]),
        dbc.Col([
            dcc.Dropdown(id='gini_country_dropdown', options=gini_country_dropdown_options),
            html.Br(),
            dcc.Graph(id='gini_country_barchart')
        ]),
    ]),
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col([
            html.H2('Income Share Distribution', style={'textAlign': 'center'}),
            html.Br(),
            dcc.Dropdown(id='income_share_country_dropdown', options=income_share_country_dropdown_options),
            dcc.Graph(id='income_share_country_barchart')
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
                html.Li([
                    'Source: ',
                    html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                           href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
                ])
            ])

        ], label='Key Facts'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Book title: Interactive Dashboards and Data Apps with Plotly and Dash'),
                html.Li(['GitHub repo: ',
                         html.A(
                             'https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                             href='https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')
                         ])
            ])
        ], label='Project Info')
    ]),

])
