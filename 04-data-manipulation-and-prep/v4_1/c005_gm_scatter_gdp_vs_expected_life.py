import plotly.express as px

gapminder = px.data.gapminder()
print(f"gapminder = {gapminder}")

gdpPercap_vs_lifeExp_fig = px.scatter(
    data_frame=gapminder,
    x='gdpPercap',
    y='lifeExp',
    color='continent',
    animation_frame='year',
    log_x=True,
    hover_name='country',
    title='Life Expectancy and GDP per capita. 1952 - 2007',
    labels={'gdpPercap': 'GDP per Capita', 'lifeExp': 'Life Expectancy'},
    size='pop',
    size_max=90,
    facet_col='continent',
    range_y=[20, 100],
    height=600,
    width=1300
)

gdpPercap_vs_lifeExp_fig.write_html("gdpPercap_vs_lifeExp_fig.html")
