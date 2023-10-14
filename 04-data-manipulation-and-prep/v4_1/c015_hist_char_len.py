import plotly.express as px

from v4_1.c010_series import series

histogram_fig = px.histogram(
    x=series['Long definition'].str.len(),
    title='Indicator <b>Long definition</b> lenghts (characters)'
)
histogram_fig.write_html("histogram_fig.html")
