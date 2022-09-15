import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x = random_x, y = random_y, mode = 'markers')]
layout = go.Layout(title='Plot',
 xaxis = dict(title='X axis'),
 yaxis = dict(title='Y axis'),
 hovermode = 'closest'
 )

fig = go.Figure(data= data, layout = layout)
pyo.plot(fig, filename = 'Scatter.html')


np.random.seed(50)
random_x = np.linspace(0,1,100)
random_y = np.random.randn(100)
data0 = go.Scatter(x = random_x, y = random_y, mode = 'markers', name='markers')
data1 = go.Scatter(x = random_x, y = random_y+5, mode = 'lines', name='mylines')
data = [data0, data1]
layout = go.Layout(title='Line Chart')
            
                 
fig = go.Figure(data= data, layout = layout)
pyo.plot(fig, filename = 'line_chart.html')