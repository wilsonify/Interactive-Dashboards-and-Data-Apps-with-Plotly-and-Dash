import html

from dash import callback, Output, Input
from dash.html import H3

from v2_1.read.poverty_data import poverty_data


@callback(Output('report', 'children'),
              Input('country', 'value'))
def display_country_report(country):
    if country is None:
        return ''

    filtered_df = poverty_data[(poverty_data['Country Name'] == country) &
                               (poverty_data['Indicator Name'] == 'Population, total')]
    population = filtered_df.loc[:, '2010'].values[0]

    return [H3(country),
            f'The population of {country} in 2010 was {population:,.0f}.']
