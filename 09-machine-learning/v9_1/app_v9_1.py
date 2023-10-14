import dash
import dash_bootstrap_components as dbc

from v9_1.layouts.primary_layout import primary_layout
from v9_1.callbacks import (
    c01_display_generic_map_chart,
    c03_plot_gini_year_barchart,
    c04_plot_gini_country_barchart,
    c05_plot_income_share_barchart,
    c07_display_histogram,
    c08_clustered_map,
)

assert dir(c01_display_generic_map_chart)
assert dir(c03_plot_gini_year_barchart)
assert dir(c04_plot_gini_country_barchart)
assert dir(c05_plot_income_share_barchart)
assert dir(c07_display_histogram)
assert dir(c08_clustered_map)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
app.layout = primary_layout

if __name__ == '__main__':
    server = app.server
    app.run_server(debug=True)
