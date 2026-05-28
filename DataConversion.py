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

"""
Creates orbital models for each asteroid using classical orbital elements.

Process:
- Iterates through asteroid orbital data
- Builds heliocentric orbits around the Sun
- Converts orbital parameters into 3D position vectors
- Stores Cartesian coordinates (x, y, z) in astronomical units

Libraries:
- astropy: unit handling and astronomical calculations
- poliastro: orbital mechanics and orbit generation

Error handling:
- Invalid or malformed asteroid records are skipped automatically
"""
