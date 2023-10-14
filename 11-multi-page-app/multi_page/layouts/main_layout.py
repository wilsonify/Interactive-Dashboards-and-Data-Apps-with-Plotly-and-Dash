import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from multi_page.read.poverty import countries

main_layout = html.Div([
    html.Div([
        dbc.NavbarSimple([
            dbc.DropdownMenu([
                dbc.DropdownMenuItem(country, href=country) for country in countries
            ],
                label='Select country'),
        ], brand='Home', brand_href='/'),
        dcc.Location(id='location'),
        html.Div(id='main_content'),
        html.Br(),
        dbc.Row([
            dbc.Col(lg=1),
            dbc.Col([
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
                    ], label='Poject Info')
                ]),
            ])
        ])
    ], style={'backgroundColor': '#E5ECF6'})
])
