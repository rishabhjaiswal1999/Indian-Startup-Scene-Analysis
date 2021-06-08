import plotly.graph_objects as go
import plotly.express as px


def plot():
    fig = go.Figure()

    fig.add_trace(go.Line(x=[i for i in range(10)],
                          y=[i*i for i in range(10)]))

    return fig


def plotBar(datapoints, title, xlabel, ylabel):

    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Bar(x=datapoints.index, y=datapoints.values))
    return fig


def plotGroupedBar(datapoints, title, xlabel, ylabel, categories, colors=['indianred', 'lightsalmon']):

    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)
    for category, point, color in zip(categories, datapoints, colors):
        fig.add_trace(go.Bar(x=point.index, y=point.values,
                             name=category, marker_color=color))
    return fig


def plotPie(datapoints):

    fig = px.pie(datapoints,names=datapoints.index
                ,values=datapoints.values,title='Total Number of Startup in Cities',height=800)
    fig.update_traces(textposition='inside',textinfo='percent+label')

    fig.show()
    return fig


def plotScatter(data, x, y, title='default title', template="plotly_dark"):
    fig = px.scatter(data_frame=data, x=x, y=y,
                     title=title, trendline="ols")

    fig.update_traces(marker=dict(size=10,
                                  line=dict(width=2,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    fig.update_layout(width=1000, height=500, template=template)

    return fig
