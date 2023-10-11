from urllib.parse import unquote

from dash import callback, Output, Input

from multi_page.layouts.country_dashboard import country_dashboard
from multi_page.layouts.indicators_dashboard import indicators_dashboard
from multi_page.read.poverty import countries


@callback(Output('main_content', 'children'),
          Input('location', 'pathname'))
def display_content(pathname):
    if unquote(pathname[1:]) in countries:
        return country_dashboard
    else:
        return indicators_dashboard
