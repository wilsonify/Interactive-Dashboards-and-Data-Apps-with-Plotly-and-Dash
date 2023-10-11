import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

from callbacks import (
    c01_display_content,
    c02_display_generic_map_chart,
    c03_plot_gini_year_barchart,
    c04_plot_gini_country_barchart,
    c05_plot_income_share_barchart,
    c06_plot_perc_pov_chart,
    c07_display_histogram,
    c08_clustered_map,
    c09_set_dropdown_values,
    c10_plot_country_charts,

)
from multi_page.layouts.country_dashboard import country_dashboard
from multi_page.layouts.indicators_dashboard import indicators_dashboard
from multi_page.layouts.main_layout import main_layout

assert dir(c01_display_content)
assert dir(c02_display_generic_map_chart)
assert dir(c03_plot_gini_year_barchart)
assert dir(c04_plot_gini_country_barchart)
assert dir(c05_plot_income_share_barchart)
assert dir(c06_plot_perc_pov_chart)
assert dir(c07_display_histogram)
assert dir(c08_clustered_map)
assert dir(c09_set_dropdown_values)
assert dir(c10_plot_country_charts)

app = dash.Dash(
    name=__name__,
    meta_tags=[{
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0, maximum-scale=4, minimum-scale=0.5,'
    }],
    external_stylesheets=[dbc.themes.COSMO])
server = app.server

app.validation_layout = html.Div([
    main_layout,
    indicators_dashboard,
    country_dashboard,
])

if __name__ == '__main__':
    app.layout = main_layout
    app.run_server(debug=False)
