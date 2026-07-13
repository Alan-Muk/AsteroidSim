# AsteroidSim

![Processing](https://img.shields.io/badge/Processing-4.x-006699)
![Java](https://img.shields.io/badge/Java-Mode-orange?logo=openjdk)
![Astronomy](https://img.shields.io/badge/Data-MPCORB-blue)
![Simulation](https://img.shields.io/badge/Simulation-Orbital_Mechanics-purple)
![License](https://img.shields.io/badge/License-MIT-green)

A real-time 3D asteroid belt simulation built with Processing that uses real orbital data from the Minor Planet Center (MPC) catalog to model thousands of asteroid trajectories using classical orbital mechanics.

The project combines astronomical datasets, numerical computation, object-oriented design, and real-time rendering to create an interactive visualization of the asteroid belt.

---

# Overview

AsteroidSim transforms real asteroid orbital parameters into a dynamic 3D simulation.

The system:

- Loads asteroid orbital elements from MPC data
- Computes asteroid positions using Keplerian mechanics
- Advances orbital states over simulation time
- Converts orbital coordinates into 3D space
- Renders thousands of objects in real time

The workflow:

```text
MPCORB Dataset
       |
       ↓
Orbital Element Parser
       |
       ↓
Kepler Orbit Calculator
       |
       ↓
3D Coordinate Transformation
       |
       ↓
Processing Rendering Engine
       |
       ↓
Interactive Asteroid Simulation
```

---

# Problem

Astronomical datasets often contain large collections of objects described through mathematical parameters rather than direct visual coordinates.

This project explores:

- How orbital data can be converted into spatial simulations
- How numerical methods can reproduce physical motion
- How large datasets can be rendered interactively

The goal was to transform raw orbital elements into an intuitive visualization of orbital dynamics.

---

# Architecture

## System Architecture

```text
             MPCORB.DAT

                 |
                 ↓

          MPCLoader Module

                 |
                 ↓

       Asteroid Object Model

                 |
                 ↓

          OrbitMath Engine

                 |
                 ↓

       3D Rendering Pipeline

                 |
                 ↓

        Processing Visualization
```

---

# Components

## MPC Data Loader

Responsible for:

- Parsing asteroid orbital elements
- Creating asteroid simulation objects
- Preparing astronomical data for computation

Input data:

- Semi-major axis
- Eccentricity
- Inclination
- Orbital angles
- Mean anomaly

---

## Asteroid Object Model

Each asteroid is represented as an independent simulation object.

Responsibilities:

- Store orbital parameters
- Calculate current position
- Update state based on simulation time

---

## Orbital Mathematics Engine

The simulation uses classical Keplerian orbital mechanics.

Each asteroid is described using:

| Parameter | Description |
|---|---|
| a | Semi-major axis (AU) |
| e | Eccentricity |
| i | Inclination |
| Ω | Longitude of ascending node |
| ω | Argument of perihelion |
| M | Mean anomaly |

---

# Orbital Calculation

The simulation advances orbital position using:

```
M(t) = M₀ + nt
```

where:

```
n = √(1 / a³)
```

Kepler's equation:

```
M = E - e sin(E)
```

is solved numerically using Newton-Raphson iteration.

The resulting eccentric anomaly is converted into orbital-plane coordinates and transformed into 3D heliocentric coordinates.

---

# Core Features

## Real Astronomical Data

- Uses MPCORB asteroid orbital catalog
- Simulates real asteroid trajectories
- Supports thousands of objects

---

## 3D Orbital Visualization

The simulation renders:

- Asteroid positions
- Orbital inclination
- Eccentric trajectories
- Heliocentric movement

---

## Real-Time Simulation

Features:

- Continuous time progression
- Automatic camera rotation
- Interactive 3D environment
- Dynamic position recalculation

---

## Large-Scale Rendering

The default configuration supports approximately:

- 2,000 asteroids
- Real-time position updates
- Continuous rendering

---

# Technical Highlights

- Implemented orbital mechanics calculations from first principles
- Built a numerical Kepler equation solver
- Designed an object-oriented simulation architecture
- Processed real astronomical datasets
- Converted mathematical models into 3D visualization
- Balanced simulation accuracy with rendering performance

---

# Design Decisions

## Object-Oriented Simulation Model

Each asteroid is represented as an independent object.

This allows:

- Modular calculations
- Easy extension of asteroid behavior
- Separation of physics and rendering logic

---

## Numerical Orbital Computation

Rather than storing fixed positions, the simulation calculates asteroid locations dynamically.

Benefits:

- Realistic motion
- Adjustable simulation speed
- Support for large time ranges

---

## Separation of Concerns

The project separates:

```
Data Loading

       ↓

Physics Calculations

       ↓

Rendering
```

This keeps astronomical computation independent from visualization.

---

# Project Structure

```text
AsteroidSim/

├── Asteroid.pde
├── OrbitMath.pde
├── MPCLoader.pde
├── AsteroidSim.pde
│
├── data/
│   └── MPCORB.DAT
│
└── README.md
```

---

# File Responsibilities

## Asteroid.pde

Represents individual asteroid objects.

Handles:

- Orbital parameters
- Position calculation
- Simulation updates

---

## OrbitMath.pde

Contains orbital mathematics utilities:

- Kepler solver
- Rotation calculations
- Coordinate transformations

---

## MPCLoader.pde

Handles:

- MPCORB parsing
- Orbital element extraction
- Object creation

---

## AsteroidSim.pde

Main simulation controller.

Handles:

- Loading data
- Updating simulation time
- Rendering the scene
- Camera movement

---

# Running Locally

## Requirements

- Processing 4.x
- Java Mode enabled
- MPCORB orbital element dataset

---

## Installation

1. Install Processing.

2. Download the latest MPCORB dataset from the Minor Planet Center.

3. Place the file:

```
data/MPCORB.DAT
```

4. Open:

```
AsteroidSim.pde
```

5. Run the sketch.

---

# Controls

Current controls:

- Automatic camera rotation
- Continuous simulation time progression

Future controls:

- Zoom
- Pause/resume
- Orbit inspection
- Time manipulation

---

# Performance Considerations

Each asteroid position is recomputed every frame.

Performance depends on:

- Number of simulated objects
- Rendering resolution
- CPU capability

Possible optimizations:

- GPU-based computation
- Spatial indexing
- Level-of-detail rendering

---

# Example Applications

- Astronomy visualization
- Physics simulation demonstrations
- Procedural rendering experiments
- Scientific data visualization
- Educational simulation tools

---

# Challenges

## Numerical Accuracy

Orbital motion requires accurate mathematical modeling.

Solution:

- Keplerian orbital equations
- Newton-Raphson numerical solving
- Coordinate transformations

---

## Rendering Large Object Sets

Thousands of moving objects can impact performance.

Solution:

- Lightweight object models
- Efficient frame updates
- Controlled simulation scale

---

## Converting Mathematics Into Visuals

Orbital elements are abstract mathematical values.

Solution:

- Transform orbital coordinates into 3D space
- Build intuitive visual representation

---

# Future Improvements

- Orbit trail rendering
- Planet visualization
- Adjustable simulation speed
- Interactive camera controls
- GPU-based rendering
- Full MPC catalog support
- Asteroid classification coloring
- Epoch-aware orbital propagation
- Collision prediction system

---

# Data Source

Orbital elements are derived from:

Minor Planet Center asteroid catalog (`MPCORB.DAT`)

---

# License

MIT License
