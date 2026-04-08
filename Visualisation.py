import plotly.graph_objects as go

x, y, z = zip(*positions)

fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(size=2, color='orange', opacity=0.7)
)])

fig.update_layout(scene=dict(
    xaxis_title='X (AU)',
    yaxis_title='Y (AU)',
    zaxis_title='Z (AU)'
))

fig.show()