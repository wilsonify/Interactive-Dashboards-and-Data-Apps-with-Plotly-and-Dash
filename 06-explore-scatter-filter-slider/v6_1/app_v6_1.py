import dash
import dash_bootstrap_components as dbc

from v6_1.callbacks import (
    c02_plot_countries_by_population,
    c03_plot_gini_year_barchart,
    c04_plot_gini_country_barchart,
    c05_plot_income_share_barchart,
    c06_plot_perc_pov_chart
)
from v6_1.layouts.primary_layout import primary_layout

assert dir(c02_plot_countries_by_population)
assert dir(c03_plot_gini_year_barchart)
assert dir(c04_plot_gini_country_barchart)
assert dir(c05_plot_income_share_barchart)
assert dir(c06_plot_perc_pov_chart)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

app.layout = primary_layout
if __name__ == '__main__':
    app.run_server(debug=True)
