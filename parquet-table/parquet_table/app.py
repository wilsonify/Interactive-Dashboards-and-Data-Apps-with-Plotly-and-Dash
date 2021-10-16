import logging
import os
import re

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
from dash_table import DataTable

from parquet_table import cividis0
from parquet_table import gini, regions
from parquet_table.dash_helpers import make_empty_fig
from parquet_table.dash_helpers import multiline_indicator

path_to_this_file = os.path.abspath(__file__)
path_to_this_folder, this_file = os.path.split(path_to_this_file)
path_to_parent_folder, this_folder = os.path.split(path_to_this_folder)
path_to_data = f"{path_to_parent_folder}/data"

app = dash.Dash(name=__name__, external_stylesheets=[dbc.themes.COSMO])

poverty_data = pd.read_csv(f"{path_to_data}/PovStatsData.csv", low_memory=False)
poverty = pd.read_csv(f"{path_to_data}/poverty.csv", low_memory=False)
pov_stats_series = pd.read_csv(f"{path_to_data}/PovStatsSeries.csv", low_memory=False)
gini_df = poverty[poverty[gini].notna()]
country_name_isin_regions = poverty_data["Country Name"].isin(regions)
country_name_notin_regions = ~country_name_isin_regions
indicator_name_is_population_total = poverty_data["Indicator Name"] == "Population, total"
population_df = poverty_data[country_name_notin_regions & indicator_name_is_population_total]
logging.debug(f"population_df.shape = {population_df.shape}")
income_share_df = poverty.filter(regex="Country Name|^year$|Income share.*?20").dropna()
income_share_df = income_share_df.rename(
    columns={
        "Income share held by lowest 20%": "01 Income share held by lowest 20%",
        "Income share held by second 20%": "02 Income share held by second 20%",
        "Income share held by third 20%": "03 Income share held by third 20%",
        "Income share held by fourth 20%": "04 Income share held by fourth 20%",
        "Income share held by highest 20%": "05 Income share held by highest 20%",
    }
).sort_index(axis=1)
income_share_df.columns = [
    re.sub("\d Income share held by ", "", col).title()
    for col in income_share_df.columns
]
income_share_cols = income_share_df.columns[:-2]
perc_pov_cols = poverty.filter(regex="Poverty gap").columns
perc_pov_df = poverty[poverty["is_country"]].dropna(subset=perc_pov_cols)
perc_pov_years = sorted(set(perc_pov_df["year"]))

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

app.layout = html.Div([
    dbc.Col([
            html.Br(),
            html.H1("Parquet Table Viewer"),
            html.H1("type an absolute path to a file"),
            dcc.Textarea(id='input_file_path_text_area'),
            html.Div(id='input_file_path_text_area_output'),
            html.Div(id="data_table_output"),
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


@app.callback(Output('input_file_path_text_area_output', 'children'),
              Input('input_file_path_text_area', 'value'))
def capture_input_file_path(input_text):
    if input_text is None:
        return "/path/to/file"
    return f"{input_text}"


@app.callback(
    Output("data_table_output", "children"),
    Input('input_file_path_text_area', 'value'),
)
def display_data_table(input_text):
    if input_text is None:
        return "data should display here"
    df = pd.DataFrame()
    if input_text.endswith('.csv'):
        df = pd.read_csv(f"{input_text}", low_memory=False)
    if input_text.endswith('.parquet'):
        df = pd.read_csv(f"{input_text}", low_memory=False)
    dt = DataTable(
        data=df.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in df.columns],
        style_header={'whiteSpace': 'normal'},
        # fixed_rows={'headers': True},
        virtualization=True,
        style_table={'height': '400px'})

    return dt


@app.callback(
    Output("indicator_map_chart", "figure"),
    Output("indicator_map_details_md", "children"),
    Input("indicator_dropdown", "value"),
)
def display_generic_map_chart(indicator):
    if indicator is None:
        raise PreventUpdate
    df = poverty[poverty["is_country"]]
    fig = px.choropleth(
        df,
        locations="Country Code",
        color=indicator,
        title=indicator,
        hover_name="Country Name",
        color_continuous_scale="cividis",
        animation_frame="year",
        height=650,
    )
    fig.layout.geo.showframe = False
    fig.layout.geo.showcountries = True
    fig.layout.geo.projection.type = "natural earth"
    fig.layout.geo.lataxis.range = [-53, 76]
    fig.layout.geo.lonaxis.range = [-138, 167]
    fig.layout.geo.landcolor = "white"
    fig.layout.geo.bgcolor = "#E5ECF6"
    fig.layout.paper_bgcolor = "#E5ECF6"
    fig.layout.geo.countrycolor = "gray"
    fig.layout.geo.coastlinecolor = "gray"
    fig.layout.coloraxis.colorbar.title = multiline_indicator(indicator)

    series_df = pov_stats_series[pov_stats_series["Indicator Name"].eq(indicator)]
    if series_df.empty:
        markdown = "No details available on this indicator"
    else:
        limitations = (
            series_df["Limitations and exceptions"]
                .fillna("N/A")
                .str.replace("\n\n", " ")
                .values[0]
        )

        markdown = f"""
                ## {series_df['Indicator Name'].values[0]}  

                {series_df['Long definition'].values[0]}  

                * **Unit of measure** {series_df['Unit of measure'].fillna('count').values[0]}
                * **Periodicity** {series_df['Periodicity'].fillna('N/A').values[0]}
                * **Source** {series_df['Source'].values[0]}

                ### Limitations and exceptions:  

                {limitations}  

                """
    return fig, markdown


@app.callback(
    Output("gini_year_barchart", "figure"), Input("gini_year_dropdown", "value")
)
def plot_gini_year_barchart(year):
    if not year:
        raise PreventUpdate
    df = gini_df[gini_df["year"].eq(year)].sort_values(gini).dropna(subset=[gini])
    n_countries = len(df["Country Name"])
    fig = px.bar(
        df,
        x=gini,
        y="Country Name",
        orientation="h",
        height=200 + (n_countries * 20),
        width=650,
        title=gini + " " + str(year),
    )
    fig.layout.paper_bgcolor = "#E5ECF6"
    return fig


@app.callback(
    Output("gini_country_barchart", "figure"),
    Input("gini_country_dropdown", "value"),
)
def plot_gini_country_barchart(countries):
    if not countries:
        raise PreventUpdate
    df = gini_df[gini_df["Country Name"].isin(countries)].dropna(subset=[gini])
    fig = px.bar(
        df,
        x="year",
        y=gini,
        height=100 + (250 * len(countries)),
        facet_row="Country Name",
        color="Country Name",
        labels={gini: "Gini Index"},
        title="".join([gini, "<br><b>", ", ".join(countries), "</b>"]),
    )
    fig.layout.paper_bgcolor = "#E5ECF6"
    return fig


@app.callback(
    Output("income_share_country_barchart", "figure"),
    Input("income_share_country_dropdown", "value"),
)
def plot_income_share_barchart(country):
    if country is None:
        raise PreventUpdate
    fig = px.bar(
        income_share_df[income_share_df["Country Name"] == country].dropna(),
        x=income_share_cols,
        y="Year",
        barmode="stack",
        height=600,
        hover_name="Country Name",
        title=f"Income Share Quintiles - {country}",
        orientation="h",
    )
    fig.layout.legend.title = None
    fig.layout.legend.orientation = "h"
    fig.layout.legend.x = 0.2
    fig.layout.legend.y = -0.15
    fig.layout.xaxis.title = "Percent of Total Income"
    fig.layout.paper_bgcolor = "#E5ECF6"
    fig.layout.plot_bgcolor = "#E5ECF6"
    return fig


@app.callback(
    Output("perc_pov_scatter_chart", "figure"),
    Input("perc_pov_year_slider", "value"),
    Input("perc_pov_indicator_slider", "value"),
)
def plot_perc_pov_chart(year, indicator):
    indicator = perc_pov_cols[indicator]
    df = (
        perc_pov_df[perc_pov_df["year"].eq(year)]
            .dropna(subset=[indicator])
            .sort_values(indicator)
    )
    if df.empty:
        raise PreventUpdate

    fig = px.scatter(
        df,
        x=indicator,
        y="Country Name",
        color="Population, total",
        size=[30] * len(df),
        size_max=15,
        hover_name="Country Name",
        height=250 + (20 * len(df)),
        color_continuous_scale="cividis",
        title=indicator + "<b>: " + f"{year}" + "</b>",
    )
    fig.layout.paper_bgcolor = "#E5ECF6"
    fig.layout.xaxis.ticksuffix = "%"
    return fig


@app.callback(
    Output("indicator_year_histogram", "figure"),
    Output("table_histogram_output", "children"),
    Input("hist_multi_year_selector", "value"),
    Input("hist_indicator_dropdown", "value"),
    Input("hist_bins_slider", "value"),
)
def display_histogram(years, indicator, nbins):
    if (not years) or (not indicator):
        raise PreventUpdate
    df = poverty[poverty["year"].isin(years) & poverty["is_country"]]
    fig = px.histogram(
        df,
        x=indicator,
        facet_col="year",
        color="year",
        title=indicator + " Histogram",
        nbins=nbins,
        facet_col_wrap=4,
        height=700,
    )
    fig.for_each_xaxis(lambda axis: axis.update(title=""))
    fig.add_annotation(
        text=indicator, x=0.5, y=-0.12, xref="paper", yref="paper", showarrow=False
    )
    fig.layout.paper_bgcolor = "#E5ECF6"

    table = (
        DataTable(
            columns=[
                {"name": col, "id": col}
                for col in df[["Country Name", "year", indicator]].columns
            ],
            data=df[["Country Name", "year", indicator]].to_dict("records"),
            style_header={"whiteSpace": "normal"},
            fixed_rows={"headers": True},
            virtualization=True,
            style_table={"height": "400px"},
            sort_action="native",
            filter_action="native",
            export_format="csv",
            style_cell={"minWidth": "150px"},
        ),
    )

    return fig, table
