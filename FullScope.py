import os
import numpy as np
import pandas as pd
import requests
from astropy import units as u
from astropy.time import Time
from poliastro.bodies import Sun
from poliastro.twobody import Orbit
import plotly.graph_objects as go

# -----------------------------
# 1. Download MPCORB data
# -----------------------------
URL = "https://minorplanetcenter.net/iau/MPCORB/MPCORB.DAT"
FILE = "MPCORB.DAT"

if not os.path.exists(FILE):
    print("Downloading MPCORB data...")
    r = requests.get(URL)
    with open(FILE, "wb") as f:
        f.write(r.content)

# -----------------------------
# 2. Parse MPCORB (simplified)
# -----------------------------
print("Parsing data...")

data = []
with open(FILE, "r") as f:
    lines = f.readlines()

# Skip header (first ~40 lines)
for line in lines[40:5000]:  # LIMIT to 5000 objects for performance
    try:
        a = float(line[92:103])       # semi-major axis (AU)
        e = float(line[70:79])        # eccentricity
        i = float(line[59:68])        # inclination
        node = float(line[48:57])     # longitude of ascending node
        peri = float(line[37:46])     # argument of perihelion
        M = float(line[26:35])        # mean anomaly

        data.append([a, e, i, node, peri, M])
    except:
        continue

df = pd.DataFrame(data, columns=['a','e','i','node','peri','M'])

# -----------------------------
# 3. Generate positions over time
# -----------------------------
print("Computing orbits...")

times = np.linspace(0, 365, 30)  # 1 year, 30 frames
frames = []

for t in times:
    xs, ys, zs = [], [], []

    for _, row in df.iterrows():
        try:
            orbit = Orbit.from_classical(
                Sun,
                row['a'] * u.au,
                row['e'] * u.one,
                row['i'] * u.deg,
                row['node'] * u.deg,
                row['peri'] * u.deg,
                row['M'] * u.deg
            )

            propagated = orbit.propagate(t * u.day)
            r = propagated.r.to(u.au)

            xs.append(r.x.value)
            ys.append(r.y.value)
            zs.append(r.z.value)

        except:
            continue

    frame = go.Frame(
        data=[go.Scatter3d(
            x=xs, y=ys, z=zs,
            mode='markers',
            marker=dict(size=2, color='orange', opacity=0.7)
        )],
        name=str(t)
    )

    frames.append(frame)

# -----------------------------
# 4. Create Plotly animation
# -----------------------------
print("Rendering visualization...")

fig = go.Figure(
    data=[go.Scatter3d(
        x=frames[0].data[0].x,
        y=frames[0].data[0].y,
        z=frames[0].data[0].z,
        mode='markers',
        marker=dict(size=2, color='orange')
    )],
    frames=frames
)

fig.update_layout(
    title="Asteroid Simulation (MPC Data)",
    scene=dict(
        xaxis_title="X (AU)",
        yaxis_title="Y (AU)",
        zaxis_title="Z (AU)"
    ),
    updatemenus=[{
        "type": "buttons",
        "buttons": [
            {"label": "Play", "method": "animate",
             "args": [None, {"frame": {"duration": 100, "redraw": True}}]},
            {"label": "Pause", "method": "animate",
             "args": [[None], {"frame": {"duration": 0}}]}
        ]
    }]
)

fig.show()