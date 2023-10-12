import dash

from v1_1.layouts.primary import primary_layout

app = dash.Dash(__name__)

app.layout = primary_layout

if __name__ == '__main__':
    app.run_server(debug=True)
