from dash import callback, Output, Input
from dash.exceptions import PreventUpdate
from plotly import express as px

from multi_page.utils.multiline_indicator import multiline_indicator
from multi_page.read.pov_stats import series
from multi_page.read.poverty import poverty


@callback(Output('indicator_map_chart', 'figure'),
          Output('indicator_map_details_md', 'children'),
          Input('indicator_dropdown', 'value'))
def display_generic_map_chart(indicator):
    if indicator is None:
        raise PreventUpdate
    df = poverty[poverty['is_country']]
    fig = px.choropleth(df, locations='Country Code',
                        color=indicator,
                        title=indicator,
                        hover_name='Country Name',
                        color_continuous_scale='cividis',
                        animation_frame='year', height=650)
    fig.layout.geo.showframe = False
    fig.layout.geo.showcountries = True
    fig.layout.geo.projection.type = 'natural earth'
    fig.layout.geo.lataxis.range = [-53, 76]
    fig.layout.geo.lonaxis.range = [-138, 167]
    fig.layout.geo.landcolor = 'white'
    fig.layout.geo.bgcolor = '#E5ECF6'
    fig.layout.paper_bgcolor = '#E5ECF6'
    fig.layout.geo.countrycolor = 'gray'
    fig.layout.geo.coastlinecolor = 'gray'
    fig.layout.coloraxis.colorbar.title = multiline_indicator(indicator)

    series_df = series[series['Indicator Name'].eq(indicator)]
    if series_df.empty:
        markdown = "No details available on this indicator"
    else:
        limitations = series_df['Limitations and exceptions'].fillna('N/A').str.replace('\n\n', ' ').values[0]

        markdown = f"""
        ## {series_df['Indicator Name'].values[0]}  
        
        {series_df['Long definition'].values[0]}  
        
        * **Unit of measure** {series_df['Unit of measure'].fillna('count').values[0]}
        * **Periodicity** {series_df['Periodicity'].fillna('N/A').values[0]}
        * **Source** {series_df['Source'].values[0]}
        
        ### Limitations and exceptions:  
        
        {limitations}  

        """
    return fig, markdown
