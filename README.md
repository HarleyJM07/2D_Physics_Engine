# 2D Physics Engine

A 2D physics engine built from scratch in Python, using [pygame](https://www.pygame.org/) purely for rendering and input — all the physics (vectors, forces, integration, collision detection, and collision resolution) is implemented from first principles, with no physics library involved.

## Overview

This started as a project to actually understand how physics engines work under the hood, rather than just using one. Every part of the simulation — how objects move, how they fall, how they bounce off walls and each other — is built up from basic vector math and Newtonian mechanics.

## Physics concepts covered

- **Vectors** — position, velocity, and force are all represented as 2D vectors (`Vector2`), with operations like addition, subtraction, scaling, dot product, and normalization.
- **Newton's second law (F = ma)** — forces (like gravity) are accumulated on a body each frame, then converted into acceleration by dividing by mass, so heavier objects resist forces more than lighter ones.
- **Semi-implicit Euler integration** — the numerical method used to turn acceleration into velocity, and velocity into position, frame by frame, using delta time (`dt`) so the simulation runs at the same speed regardless of frame rate.
- **Collision detection** — circle-vs-circle overlap is detected by comparing the distance between two centers to the sum of their radii (using squared distances to avoid unnecessary `sqrt` calls).
- **Impulse-based collision resolution** — collisions are resolved using conservation of momentum and a restitution (bounciness) coefficient, so mass and speed both affect the outcome realistically, rather than just stopping objects dead.
- **Solver iterations** — collision resolution runs multiple passes per frame to keep groups of overlapping objects stable, instead of jittering when many objects are packed closely together.
- **Spatial partitioning (grid broad-phase)** — instead of checking every pair of objects for collisions every frame (which gets slow fast), objects are bucketed into a grid, and only objects sharing or neighboring a grid cell are checked against each other.

## Features

- Gravity and realistic falling motion
- Circle-circle collisions with proper momentum transfer
- Collisions with all four boundaries (floor, ceiling, left wall, right wall)
- Grid-based spatial partitioning for better performance with many objects
- Live FPS counter
- Click on empty space to spawn a new ball
- Click and drag existing balls
- Throwing: release a dragged ball while moving the mouse to fling it, with velocity based on how fast the mouse was moving

## Running it

Requires Python 3 and [pygame](https://www.pygame.org/).

```bash
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install pygame
python demo.py
```

## Project structure

- `vector2.py` — 2D vector math (`Vector2` class)
- `rigid_body.py` — physics objects with mass, position, velocity, and force accumulation
- `world.py` — the simulation itself: gravity, integration, collision detection/resolution, spatial grid
- `demo.py` — pygame window, rendering, and mouse/keyboard input

## What I'd add next

- Different shapes (rectangles/AABBs), not just circles
- Per-object mass and restitution (currently uniform across all balls)
- Rotation and angular velocity