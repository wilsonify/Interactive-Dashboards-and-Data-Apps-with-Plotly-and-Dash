from plotly import graph_objects as go


def make_empty_fig():
    fig = go.Figure()
    fig.layout.paper_bgcolor = "#E5ECF6"
    fig.layout.plot_bgcolor = "#E5ECF6"
    return fig


def multiline_indicator(indicator):
    final = []
    split = indicator.split()
    for i in range(0, len(split), 3):
        final.append(" ".join(split[i: i + 3]))
    return "<br>".join(final)