import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from multi_page.read.poverty import poverty, countries

country_dashboard = html.Div([
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col([
            html.Br(),
            html.H1(id='country_heading'),
            dbc.Row([
                dbc.Col(dcc.Graph(id='country_page_graph'))
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label('Select indicator:'),
                    dcc.Dropdown(
                        id='country_page_indicator_dropdown',
                        placeholder='Choose an indicator',
                        value='Population, total',
                        options=[{'label': indicator, 'value': indicator}
                                 for indicator in poverty.columns[3:54]]),
                ], lg=6, md=11),
                dbc.Col([
                    dbc.Label('Select countries:'),
                    dcc.Dropdown(id='country_page_contry_dropdown',
                                 placeholder='Select one or more countries to compare',
                                 multi=True,
                                 options=[{'label': c, 'value': c}
                                          for c in countries]),
                ], lg=6, md=11)
            ]),
            html.Br(), html.Br(),
            html.Div(id='country_table')
        ], lg=10)
    ]),
])
