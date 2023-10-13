from dash import callback, Output, Input, html

from v3_1.read.PovStatsData import poverty_data, is_pop_total


@callback(
    Output('report', 'children'),
    Input('country', 'value')

)
def display_country_report(country):
    if country is None:
        return ''
    is_country = poverty_data['Country Name'] == country
    filtered_df = poverty_data[is_country & is_pop_total]
    population = filtered_df.loc[:, '2010'].values[0]
    result = [html.H3(country), f'The population of {country} in 2010 was {population:,.0f}.']
    return result
