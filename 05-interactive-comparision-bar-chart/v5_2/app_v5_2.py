import dash
import dash_bootstrap_components as dbc

from v5_2.layouts.primary_layout import primary_layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = primary_layout

if __name__ == '__main__':
    app.run_server(debug=True)
