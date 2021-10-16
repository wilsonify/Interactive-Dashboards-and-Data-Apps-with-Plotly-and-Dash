import logging
import os
import re

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
from dash_table import DataTable

from parquet_table import gini, regions
from parquet_table.dash_helpers import multiline_indicator
from parquet_table.layout import construct_layout

path_to_this_file = os.path.abspath(__file__)
path_to_this_folder, this_file = os.path.split(path_to_this_file)
path_to_parent_folder, this_folder = os.path.split(path_to_this_folder)
path_to_data = f"{path_to_parent_folder}/data"


class ParquetTableApp():
    """
    Capture our Dash App and it's callbacks
    """
    app = dash.Dash(name=__name__, external_stylesheets=[dbc.themes.COSMO])

    def __init__(self):
        self.poverty_data = pd.read_csv(f"{path_to_data}/PovStatsData.csv", low_memory=False)
        self.poverty = pd.read_csv(f"{path_to_data}/poverty.csv", low_memory=False)
        self.pov_stats_series = pd.read_csv(f"{path_to_data}/PovStatsSeries.csv", low_memory=False)
        self.poverty_data = pd.read_csv(f"{path_to_data}/PovStatsData.csv", low_memory=False)
        self.poverty = pd.read_csv(f"{path_to_data}/poverty.csv", low_memory=False)
        self.pov_stats_series = pd.read_csv(f"{path_to_data}/PovStatsSeries.csv", low_memory=False)
        self.gini_df = self.poverty[self.poverty[gini].notna()]
        country_name_isin_regions = self.poverty_data["Country Name"].isin(regions)
        country_name_notin_regions = ~country_name_isin_regions
        indicator_name_is_population_total = self.poverty_data["Indicator Name"] == "Population, total"
        self.population_df = self.poverty_data[country_name_notin_regions & indicator_name_is_population_total]
        logging.debug(f"population_df.shape = {self.population_df.shape}")

        self.income_share_df = self.poverty.filter(regex="Country Name|^year$|Income share.*?20").dropna()
        self.income_share_df = self.income_share_df.rename(
            columns={
                "Income share held by lowest 20%": "01 Income share held by lowest 20%",
                "Income share held by second 20%": "02 Income share held by second 20%",
                "Income share held by third 20%": "03 Income share held by third 20%",
                "Income share held by fourth 20%": "04 Income share held by fourth 20%",
                "Income share held by highest 20%": "05 Income share held by highest 20%",
            }
        ).sort_index(axis=1)

        self.income_share_df.columns = [
            re.sub("\d Income share held by ", "", col).title()
            for col in self.income_share_df.columns
        ]
        self.income_share_cols = self.income_share_df.columns[:-2]

        self.perc_pov_cols = self.poverty.filter(regex="Poverty gap").columns
        self.perc_pov_df = self.poverty[self.poverty["is_country"]].dropna(subset=self.perc_pov_cols)
        self.perc_pov_years = sorted(set(self.perc_pov_df["year"]))

        self.app.layout = construct_layout(self.poverty, self.gini_df, self.income_share_df, self.perc_pov_years)

    @app.callback(
        Output("indicator_map_chart", "figure"),
        Output("indicator_map_details_md", "children"),
        Input("indicator_dropdown", "value"),
    )
    def display_generic_map_chart(self, indicator):
        if indicator is None:
            raise PreventUpdate
        df = self.poverty[self.poverty["is_country"]]
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

        series_df = self.pov_stats_series[self.pov_stats_series["Indicator Name"].eq(indicator)]
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
    def plot_gini_year_barchart(self, year):
        if not year:
            raise PreventUpdate
        df = self.gini_df[self.gini_df["year"].eq(year)].sort_values(gini).dropna(subset=[gini])
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
    def plot_gini_country_barchart(self, countries):
        if not countries:
            raise PreventUpdate
        df = self.gini_df[self.gini_df["Country Name"].isin(countries)].dropna(subset=[gini])
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
    def plot_income_share_barchart(self, country):
        if country is None:
            raise PreventUpdate
        fig = px.bar(
            self.income_share_df[self.income_share_df["Country Name"] == country].dropna(),
            x=self.income_share_cols,
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
    def plot_perc_pov_chart(self, year, indicator):
        indicator = self.perc_pov_cols[indicator]
        df = (
            self.perc_pov_df[self.perc_pov_df["year"].eq(year)]
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
    def display_histogram(self, years, indicator, nbins):
        if (not years) or (not indicator):
            raise PreventUpdate
        df = self.poverty[self.poverty["year"].isin(years) & self.poverty["is_country"]]
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
