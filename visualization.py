import plotly.graph_objects as go

def plot():
    fig = go.Figure()

    fig.add_trace( go.Line( x = [i for i in range(10)] , y = [ i*i for i in range(10) ] ) )

    return fig

def plotBar(datapoints, title, xlabel, ylabel):
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    fig.add_trace( go.Bar(x = datapoints.index,y= datapoints.values))
    return fig

def plotGroupedBar(datapoints, title, xlabel, ylabel, categories, colors = ['indianred', 'lightsalmon']):
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    for category, point, color in zip(categories, datapoints, colors):
        fig.add_trace( go.Bar(x = point.index,y= point.values, name = category, marker_color = color))
    return fig

def plotPie(datapoints, colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']):
    fig=go.Figure(data=[go.Pie(labels=typ.index,values=typ.values)])
    fig.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=10,
                    marker=dict(colors=colrs))
    fig.data[0].marker.line.width = 3
    fig.data[0].marker.line.color = "black"                
    fig.update_layout(height=600,autosize=True ,plot_bgcolor='rgb(275, 275, 275)')
    return fig