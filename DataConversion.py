from astropy import units as u
from astropy.time import Time
from poliastro.bodies import Sun
from poliastro.twobody import Orbit

positions = []

for _, row in asteroids.iterrows():
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
        # Get position at epoch
        pos = orbit.r.to(u.au)
        positions.append([pos.x.value, pos.y.value, pos.z.value])
    except Exception as e:
        continue  # skip problematic entries