import plotly.graph_objects as go
import numpy as np

x = [1.30264177701689, 1.57084444444444, 2.04871511111111]
y = [0.345, 0.391, 0.524]
yerr = [0.01, 0.01, 0.01]
xerr = [0.029310597604849, 0.0188797370102964, 0.0118509272727448]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='lines',
))
fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='markers',
    name='measured',
    error_y=dict(
        type='data',
        array=yerr,
        color='purple',
        thickness=1.5,
        width=3,
    ),
    error_x=dict(
        type='data',
        array=xerr,
        color='purple',
        thickness=1.5,
        width=3,
    ),
    marker=dict(color='purple', size=8)
))
fig.write_html("test.html")
