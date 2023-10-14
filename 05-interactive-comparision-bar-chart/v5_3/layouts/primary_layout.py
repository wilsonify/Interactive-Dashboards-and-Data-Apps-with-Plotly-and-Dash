import dash_bootstrap_components as dbc
from dash import html, dcc

from v5_3.read.population_df import (
    year_options,
    gini_year_dropdown_options,
    gini_country_dropdown_options,
    income_share_country_dropdown_options
)
from v5_3.utils.make_empty_fig import make_empty_fig

gitHub_repo_url = 'https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash'

primary_layout = html.Div([
    html.H1('Poverty And Equity Database'),
    html.H2('The World Bank'),
    html.Br(),
    dcc.Dropdown(id='year_dropdown', value='2010', options=year_options),
    dcc.Graph(id='population_chart'),
    html.Br(),
    html.H2('Gini Index - World Bank Data', style={'textAlign': 'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col([
            dbc.Label('Year'),
            dcc.Dropdown(id='gini_year_dropdown', placeholder='Select a year', options=gini_year_dropdown_options),
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
        dbc.Col(lg=1),
        dbc.Col([
            html.Br(),
            html.H2('Income Share Distribution', style={'textAlign': 'center'}),
            html.Br(),
            dbc.Label('Country'),
            dcc.Dropdown(id='income_share_country_dropdown',
                         placeholder='Select a country',
                         options=income_share_country_dropdown_options),
            dcc.Graph(id='income_share_country_barchart',
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
                html.Li(['GitHub repo: ', html.A(gitHub_repo_url, href=gitHub_repo_url)])
            ])
        ], label='Project Info')
    ]),

], style={'backgroundColor': '#E5ECF6'})
