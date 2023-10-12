import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from v2_1.read.poverty_data import country_options

primary_layout = html.Div([
    html.H1('Poverty And Equity Database'),
    html.H2('The World Bank'),
    dcc.Dropdown(id='country',
                 options=country_options),
    html.Br(),
    html.Div(id='report'),
    html.Br(),
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
