import dash
import dash_bootstrap_components as dbc

from v2_1.callbacks.display_country_report import display_country_report
from v2_1.layouts.primary import primary_layout

assert dir(display_country_report)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = primary_layout

if __name__ == '__main__':
    app.run_server(debug=True)
