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

"""
Creates an interactive 3D visualization of asteroid positions.

Process:
- Extracts Cartesian coordinates from the positions list
- Generates a Plotly 3D scatter plot
- Displays asteroid locations in astronomical units (AU)

Visualization settings:
- Orange markers represent asteroids
- Semi-transparent markers improve depth visibility
- Interactive controls allow zooming, rotation, and panning

Output:
- Interactive 3D asteroid distribution map
"""
