import dash
import dash_bootstrap_components as dbc

from v3_1.callbacks import (
    c01_display_country_report,
    c02_plot_countries_by_population
)
from v3_1.layouts.primary_layout import primary_layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = primary_layout
assert dir(c01_display_country_report)
assert dir(c02_plot_countries_by_population)

if __name__ == '__main__':
    app.run_server(debug=True)
