from urllib.parse import unquote

from dash import callback, Output, Input

from multi_page.read.poverty import countries


@callback(Output('country_page_contry_dropdown', 'value'),
          Input('location', 'pathname'))
def set_dropdown_values(pathname):
    if unquote(pathname[1:]) in countries:
        country = unquote(pathname[1:])
        return [country]
