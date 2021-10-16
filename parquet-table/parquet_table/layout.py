import os

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from parquet_table import cividis0
from parquet_table.dash_helpers import make_empty_fig

path_to_this_file = os.path.abspath(__file__)
path_to_this_folder, this_file = os.path.split(path_to_this_file)
path_to_parent_folder, this_folder = os.path.split(path_to_this_folder)
path_to_data = f"{path_to_parent_folder}/data"


def construct_layout(poverty, gini_df, income_share_df, perc_pov_years):
    poverty_dropdown_options = [
        {"label": indicator, "value": indicator} for indicator in poverty.columns[3:54]
    ]
    gini_dropdown_options = [
        {"label": indicator, "value": indicator} for indicator in poverty.columns[3:54]
    ]
    hist_year_dropdown_options = [
        {"label": year, "value": year} for year in poverty["year"].drop_duplicates().sort_values()
    ]
    countries_dropdown_options = [
        {"label": country, "value": country} for country in gini_df["Country Name"].unique()
    ]
    income_share_dropdown_options = [
        {"label": country, "value": country} for country in income_share_df["Country Name"].unique()
    ]
    perc_pov_year_slider_marks = {
        year: {"label": str(year), "style": {"color": cividis0, "fontSize": 14}, } for year in
        perc_pov_years[::5]}
    gini_year_dropdown_options = [
        {"label": year, "value": year} for year in gini_df["year"].drop_duplicates().sort_values()
    ]
    perc_pov_year_slider_min = perc_pov_years[0]
    perc_pov_year_slider_max = perc_pov_years[-1]

    return html.Div([
        dbc.Col(
            [
                html.Br(),
                html.H1("Poverty And Equity Database"),
                html.H2("The World Bank"),
            ],
            style={"textAlign": "center"},
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(lg=2),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id="indicator_dropdown",
                            value="GINI index (World Bank estimate)",
                            options=poverty_dropdown_options,
                        ),
                        dcc.Graph(id="indicator_map_chart"),
                        dcc.Markdown(
                            id="indicator_map_details_md",
                            style={"backgroundColor": "#E5ECF6"},
                        ),
                    ],
                    lg=8,
                ),
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(lg=2),
                dbc.Col(
                    [
                        dbc.Label("Indicator:"),
                        dcc.Dropdown(
                            id="hist_indicator_dropdown",
                            optionHeight=40,
                            value="GINI index (World Bank estimate)",
                            options=gini_dropdown_options,
                        ),
                    ],
                    lg=5,
                ),
                dbc.Col(
                    [
                        dbc.Label("Years:"),
                        dcc.Dropdown(
                            id="hist_multi_year_selector",
                            multi=True,
                            value=[2015],
                            placeholder="Select one or more years",
                            options=hist_year_dropdown_options,
                        ),
                    ],
                    lg=3,
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(lg=2),
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Label("Modify number of bins:"),
                        dcc.Slider(
                            id="hist_bins_slider",
                            dots=True,
                            min=0,
                            max=100,
                            step=5,
                            included=False,
                            marks={x: str(x) for x in range(0, 105, 5)},
                        ),
                        dcc.Graph(
                            id="indicator_year_histogram", figure=make_empty_fig()
                        ),
                    ],
                    lg=8,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(lg=2),
                dbc.Col(
                    [
                        html.Div(id="table_histogram_output"),
                        html.Br(),
                        html.Br(),
                    ],
                    lg=7,
                ),
            ]
        ),
        html.H2("Gini Index - World Bank Data", style={"textAlign": "center"}),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(lg=1),
                dbc.Col(
                    [
                        dbc.Label("Year"),
                        dcc.Dropdown(
                            id="gini_year_dropdown",
                            placeholder="Select a year",
                            options=gini_year_dropdown_options,
                        ),
                        html.Br(),
                        dcc.Graph(id="gini_year_barchart", figure=make_empty_fig()),
                    ],
                    md=12,
                    lg=5,
                ),
                dbc.Col(
                    [
                        dbc.Label("Countries"),
                        dcc.Dropdown(
                            id="gini_country_dropdown",
                            placeholder="Select one or more countries",
                            multi=True,
                            options=countries_dropdown_options,
                        ),
                        html.Br(),
                        dcc.Graph(
                            id="gini_country_barchart", figure=make_empty_fig()
                        ),
                    ],
                    md=12,
                    lg=5,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(lg=2),
                dbc.Col(
                    [
                        html.Br(),
                        html.H2(
                            "Income Share Distribution",
                            style={"textAlign": "center"},
                        ),
                        html.Br(),
                        dbc.Label("Country"),
                        dcc.Dropdown(
                            id="income_share_country_dropdown",
                            placeholder="Select a country",
                            options=income_share_dropdown_options,
                        ),
                        dcc.Graph(
                            id="income_share_country_barchart",
                            figure=make_empty_fig(),
                        ),
                    ],
                    lg=8,
                ),
            ]
        ),
        html.Br(),
        html.H2(
            "Poverty Gap at $1.9, $3.2, and $5.5 (% of population)",
            style={"textAlign": "center"},
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(lg=2),
                dbc.Col(
                    [
                        dbc.Label("Select poverty level:"),
                        dcc.Slider(
                            id="perc_pov_indicator_slider",
                            min=0,
                            max=2,
                            step=1,
                            included=False,
                            value=0,
                            marks={
                                0: {
                                    "label": "$1.9",
                                    "style": {
                                        "color": cividis0,
                                        "fontWeight": "bold",
                                        "fontSize": 15,
                                    },
                                },
                                1: {
                                    "label": "$3.2",
                                    "style": {
                                        "color": cividis0,
                                        "fontWeight": "bold",
                                        "fontSize": 15,
                                    },
                                },
                                2: {
                                    "label": "$5.5",
                                    "style": {
                                        "color": cividis0,
                                        "fontWeight": "bold",
                                        "fontSize": 15,
                                    },
                                },
                            },
                        ),
                    ],
                    lg=2,
                ),
                dbc.Col(
                    [
                        dbc.Label("Select year:"),
                        dcc.Slider(
                            id="perc_pov_year_slider",
                            min=perc_pov_year_slider_min,
                            max=perc_pov_year_slider_max,
                            step=1,
                            included=False,
                            value=2018,
                            marks=perc_pov_year_slider_marks,
                        ),
                    ],
                    lg=5,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(lg=1),
                dbc.Col(
                    [
                        dcc.Graph(
                            id="perc_pov_scatter_chart", figure=make_empty_fig()
                        )
                    ],
                    lg=10,
                ),
            ]
        ),
        dbc.Tabs(
            [
                dbc.Tab(
                    [
                        html.Ul(
                            [
                                html.Br(),
                                html.Li("Number of Economies: 170"),
                                html.Li("Temporal Coverage: 1974 - 2019"),
                                html.Li("Update Frequency: Quarterly"),
                                html.Li("Last Updated: March 18, 2020"),
                                html.Li(
                                    [
                                        "Source: ",
                                        html.A(
                                            "https://datacatalog.worldbank.org/dataset/poverty-and-equity-database",
                                            href="https://datacatalog.worldbank.org/dataset/poverty-and-equity-database",
                                        ),
                                    ]
                                ),
                            ]
                        )
                    ],
                    label="Key Facts",
                ),
                dbc.Tab(
                    [
                        html.Ul(
                            [
                                html.Br(),
                                html.Li(
                                    "Book title: Interactive Dashboards and Data Apps with Plotly and Dash"
                                ),
                                html.Li(
                                    [
                                        "GitHub repo: ",
                                        html.A(
                                            "https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash",
                                            href="https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash",
                                        ),
                                    ]
                                ),
                            ]
                        )
                    ],
                    label="Project Info",
                ),
            ]
        ),
    ],
        style={"backgroundColor": "#E5ECF6"},
    )
