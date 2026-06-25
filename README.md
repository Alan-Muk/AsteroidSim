# AsteroidSim

A real-time 3D asteroid belt visualization built with Processing using orbital elements from the Minor Planet Center (MPC) catalog.

![Asteroid Simulation]

## Overview

AsteroidSim loads real asteroid orbital elements from `MPCORB.DAT` and computes their positions using classical Keplerian orbital mechanics. The simulation displays thousands of asteroids orbiting the Sun in a 3D environment, providing an interactive view of the structure of the asteroid belt.

## Features

* Loads asteroid orbital elements directly from MPC data
* Solves Kepler's Equation using Newton-Raphson iteration
* Converts orbital elements to 3D heliocentric coordinates
* Renders thousands of asteroids in real time
* Supports inclined and eccentric orbits
* Simple Processing-based visualization
* Rotating 3D camera view

## Orbital Model

Each asteroid is represented by the standard set of Keplerian orbital elements:

| Parameter | Description                 |
| --------- | --------------------------- |
| a         | Semi-major axis (AU)        |
| e         | Eccentricity                |
| i         | Inclination                 |
| Ω         | Longitude of ascending node |
| ω         | Argument of perihelion      |
| M         | Mean anomaly                |

The simulation advances each orbit according to:

M(t) = M₀ + nt

where:

n = √(1 / a³)

Kepler's Equation is solved numerically:

M = E − e sin(E)

The resulting orbital-plane coordinates are transformed into 3D space using standard orbital rotations.

## Project Structure

```text
AsteroidSim/
├── Asteroid.pde
├── OrbitMath.pde
├── MPCLoader.pde
├── AsteroidSim.pde
├── data/
│   └── MPCORB.DAT
└── README.md
```

### Asteroid.pde

Represents a single asteroid and computes its position at a given simulation time.

### OrbitMath.pde

Contains:

* Kepler solver
* Rotation utilities
* Orbital coordinate transformations

### MPCLoader.pde

Parses orbital elements from MPCORB data files and constructs asteroid objects.

### AsteroidSim.pde

Main application:

* Loads asteroid data
* Updates simulation time
* Renders the Sun
* Draws asteroid positions

## Requirements

* Processing 4.x
* Java mode enabled
* MPCORB orbital element file

## Installation

1. Install Processing.
2. Download the latest `MPCORB.DAT` from the Minor Planet Center.
3. Place `MPCORB.DAT` inside the project's `data` directory.
4. Open the sketch in Processing.
5. Run the simulation.

## Controls

Current version:

* Automatic camera rotation
* Continuous time progression

Additional controls can be added for zooming, pausing, and orbit inspection.

## Performance

The default configuration loads approximately 2,000 asteroids and runs smoothly on most systems.

Increasing the object count can provide a denser visualization of the asteroid belt but will require additional CPU resources because each asteroid's position is recomputed every frame.

## Future Improvements

* Orbit trail rendering
* Planet visualization
* Adjustable simulation speed
* Interactive camera controls
* GPU-based rendering
* Full MPC catalog support
* Asteroid classification coloring
* Epoch-aware orbital propagation

## Data Source

Orbital elements are derived from the Minor Planet Center asteroid catalog (`MPCORB.DAT`).

## License

MIT License
