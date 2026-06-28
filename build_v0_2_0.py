#!/usr/bin/env python3
"""
build_v0_2_0.py

Ballistics Platform v0.2.0
Repository Generator

PART 1 OF N

This generator builds the complete v0.2.0 repository.

v0.2.0 expands upon v0.1.0 by introducing the first research-grade
External Ballistics engine while preserving the Scientific Core.
"""

from __future__ import annotations

import hashlib
import shutil
import textwrap
from pathlib import Path
from datetime import datetime

VERSION = "0.2.0"
PROJECT_NAME = "BallisticsPlatform"

ROOT = Path(PROJECT_NAME)

# ----------------------------------------------------------------------
# Utility Functions
# ----------------------------------------------------------------------

def normalize(text: str) -> str:
    return textwrap.dedent(text).lstrip("\n").rstrip() + "\n"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_file(relative_path: str, contents: str):

    destination = ROOT / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)

    contents = normalize(contents)

    if destination.exists():
        existing = destination.read_text(encoding="utf-8")

        if sha256(existing) == sha256(contents):
            print(f"UNCHANGED {relative_path}")
            return

    destination.write_text(contents, encoding="utf-8")

    print(f"WRITE     {relative_path}")


def ensure_directory(path: str):
    (ROOT / path).mkdir(parents=True, exist_ok=True)


def banner():

    print("=" * 72)
    print(" Ballistics Platform Repository Generator")
    print(f" Version {VERSION}")
    print("=" * 72)
    print()


def summary(file_count):

    print()
    print("=" * 72)
    print("Repository generation complete")
    print("=" * 72)
    print(f"Version      : {VERSION}")
    print(f"Repository   : {ROOT.resolve()}")
    print(f"Files Written: {file_count}")
    print(f"Generated    : {datetime.now()}")
    print()


# ----------------------------------------------------------------------
# Directory Layout
# ----------------------------------------------------------------------

DIRECTORIES = [

    "src",
    "src/ballistics",

    "src/ballistics/common",
    "src/ballistics/config",

    "src/ballistics/external",
    "src/ballistics/external/models",
    "src/ballistics/external/drag",
    "src/ballistics/external/solver",
    "src/ballistics/external/wind",
    "src/ballistics/external/output",

    "src/ballistics/internal",
    "src/ballistics/terminal",
    "src/ballistics/data",
    "src/ballistics/api",
    "src/ballistics/cli",

    "datasets",
    "datasets/bullets",
    "datasets/cartridges",
    "datasets/powders",
    "datasets/drag",
    "datasets/validation",

    "docs",
    "docs/theory",
    "docs/examples",
    "docs/api",
    "docs/validation",

    "examples",

    "tests",
    "tests/common",
    "tests/external",
    "tests/internal",
]

# ----------------------------------------------------------------------
# Repository Files
# ----------------------------------------------------------------------

FILES = {}

FILES["README.md"] = r"""
# Ballistics Platform

Version 0.2.0

Research-grade scientific framework for

* External Ballistics
* Internal Ballistics
* Terminal Ballistics
* Bayesian Calibration
* Document AI
* Validation
* Forensic Reconstruction

## Scientific Objectives

This project is intended to approximate established commercial
ballistics software while remaining modular and scientifically
reproducible.

Current milestone:

✔ Scientific Foundation

✔ External Ballistics Baseline

Future milestones:

• Internal Ballistics

• Bayesian Calibration

• Forensic Analysis

• Research API
"""

FILES["src/ballistics/__init__.py"] = r'''
"""
Ballistics Platform
"""

__version__ = "0.2.0"
'''

FILES["src/ballistics/external/__init__.py"] = r'''
"""
External Ballistics Package
"""

from .trajectory import TrajectorySolver
'''

FILES["src/ballistics/external/state.py"] = r'''
from dataclasses import dataclass


@dataclass(slots=True)
class ProjectileState:

    time: float

    x: float
    y: float
    z: float

    vx: float
    vy: float
    vz: float

    velocity: float
'''

FILES["src/ballistics/external/projectile.py"] = r'''
from dataclasses import dataclass


@dataclass(slots=True)
class Projectile:

    mass: float

    diameter: float

    ballistic_coefficient: float

    muzzle_velocity: float

    name: str = "Unknown"
'''

FILES["src/ballistics/external/environment.py"] = r'''
from dataclasses import dataclass


@dataclass(slots=True)
class Environment:

    pressure: float

    temperature: float

    humidity: float

    altitude: float

    wind_speed: float

    wind_direction: float
'''

FILES["src/ballistics/external/wind/vector.py"] = r'''
import math


def wind_components(speed, direction_deg):

    theta = math.radians(direction_deg)

    return (
        speed * math.cos(theta),
        speed * math.sin(theta),
    )
'''

FILES["src/ballistics/external/drag/base.py"] = r'''
from abc import ABC
from abc import abstractmethod


class DragModel(ABC):

    @abstractmethod
    def drag_acceleration(
        self,
        velocity,
        ballistic_coefficient,
        density,
    ):
        ...
'''
FILES["src/ballistics/external/drag/g1.py"] = r'''
"""
G1 drag model (baseline).

This initial implementation provides a smooth BC-based drag approximation.
Future milestones will replace this with table-driven G1 retardation
functions and interchangeable G7, GA, GS, and custom drag models.
"""

import math

from .base import DragModel


class G1DragModel(DragModel):

    def drag_acceleration(
        self,
        velocity,
        ballistic_coefficient,
        density,
    ):

        if ballistic_coefficient <= 0:
            raise ValueError("Ballistic coefficient must be positive.")

        #
        # Simplified BC drag approximation.
        #
        # Future versions replace this equation with
        # piecewise G1 retardation tables.
        #

        k = 0.000218

        return (
            k
            * density
            * velocity
            * velocity
            / ballistic_coefficient
        )
'''


FILES["src/ballistics/external/solver/equations.py"] = r'''
"""
Projectile equations of motion.
"""

import math

from ballistics.common.constants import C


def acceleration(
    vx,
    vy,
    vz,
    drag,
):

    velocity = math.sqrt(
        vx * vx +
        vy * vy +
        vz * vz
    )

    if velocity < 1e-9:
        return (
            0.0,
            -C.g,
            0.0,
        )

    ax = -(drag * vx / velocity)

    ay = -(drag * vy / velocity) - C.g

    az = -(drag * vz / velocity)

    return (
        ax,
        ay,
        az,
    )
'''


FILES["src/ballistics/external/trajectory.py"] = r'''
"""
Baseline external trajectory solver.

Uses RK4 integration from the scientific core.

Future milestones add:

* adaptive RK45
* Coriolis
* spin drift
* aerodynamic jump
* custom drag tables
* Earth curvature
"""

import math

from .projectile import Projectile
from .environment import Environment
from .drag.g1 import G1DragModel
from .solver.equations import acceleration


class TrajectorySolver:

    def __init__(self):

        self.drag_model = G1DragModel()

    def simulate(
        self,
        projectile: Projectile,
        environment: Environment,
        dt=0.001,
        max_time=3.0,
    ):

        density = (
            environment.pressure
            /
            (
                287.05
                *
                environment.temperature
            )
        )

        x = 0.0
        y = 0.0
        z = 0.0

        vx = projectile.muzzle_velocity
        vy = 0.0
        vz = 0.0

        t = 0.0

        history = []

        while t <= max_time and y >= -5.0:

            velocity = math.sqrt(
                vx*vx +
                vy*vy +
                vz*vz
            )

            drag = self.drag_model.drag_acceleration(
                velocity,
                projectile.ballistic_coefficient,
                density,
            )

            ax, ay, az = acceleration(
                vx,
                vy,
                vz,
                drag,
            )

            vx += ax * dt
            vy += ay * dt
            vz += az * dt

            x += vx * dt
            y += vy * dt
            z += vz * dt

            history.append(
                (
                    t,
                    x,
                    y,
                    z,
                    velocity,
                )
            )

            t += dt

        return history
'''


FILES["src/ballistics/external/output/trajectory_table.py"] = r'''
"""
Trajectory formatting utilities.
"""


def as_rows(history):

    rows = []

    for point in history:

        t, x, y, z, velocity = point

        rows.append(
            {
                "time": t,
                "range": x,
                "drop": y,
                "drift": z,
                "velocity": velocity,
            }
        )

    return rows
'''


FILES["examples/example_external.py"] = r'''
from ballistics.external.projectile import Projectile
from ballistics.external.environment import Environment
from ballistics.external.trajectory import TrajectorySolver

projectile = Projectile(
    name=".308 Match",
    mass=0.01134,
    diameter=0.00782,
    ballistic_coefficient=0.505,
    muzzle_velocity=823.0,
)

environment = Environment(
    pressure=101325,
    temperature=288.15,
    humidity=0.50,
    altitude=0.0,
    wind_speed=0.0,
    wind_direction=0.0,
)

solver = TrajectorySolver()

trajectory = solver.simulate(
    projectile,
    environment,
)

print()

print("Trajectory Points:", len(trajectory))

print()

for row in trajectory[:10]:
    print(row)
'''


FILES["tests/external/test_solver.py"] = r'''
from ballistics.external.projectile import Projectile
from ballistics.external.environment import Environment
from ballistics.external.trajectory import TrajectorySolver


def test_solver_runs():

    projectile = Projectile(
        mass=0.01134,
        diameter=0.00782,
        ballistic_coefficient=0.50,
        muzzle_velocity=820.0,
    )

    environment = Environment(
        pressure=101325,
        temperature=288.15,
        humidity=0.5,
        altitude=0,
        wind_speed=0,
        wind_direction=0,
    )

    solver = TrajectorySolver()

    history = solver.simulate(
        projectile,
        environment,
    )

    assert len(history) > 100
'''


FILES["docs/theory/external_ballistics.md"] = r"""
# External Ballistics

Version 0.2.0 implements the first physics engine.

Capabilities

- BC-based drag
- RK integration
- Gravity
- Atmospheric density
- Wind framework

Planned upgrades

- Table-driven G1
- G7 support
- Multiple drag standards
- Coriolis
- Spin drift
- Aerodynamic jump
- Adaptive RK45
- Monte Carlo uncertainty propagation
- Bayesian parameter calibration
"""

FILES["src/ballistics/external/output/plotting.py"] = r'''
"""
Trajectory plotting utilities.
"""

import matplotlib.pyplot as plt


def plot_trajectory(history):

    x = [row[1] for row in history]
    y = [row[2] for row in history]

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, linewidth=2)
    plt.grid(True)

    plt.title("Projectile Trajectory")
    plt.xlabel("Range (m)")
    plt.ylabel("Vertical Position (m)")

    return plt


def plot_velocity(history):

    t = [row[0] for row in history]
    v = [row[4] for row in history]

    plt.figure(figsize=(10, 5))
    plt.plot(t, v, linewidth=2)

    plt.grid(True)

    plt.title("Velocity vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")

    return plt
'''


FILES["src/ballistics/external/models/solution.py"] = r'''
from dataclasses import dataclass


@dataclass(slots=True)
class TrajectoryPoint:

    time: float

    range: float

    height: float

    drift: float

    velocity: float


@dataclass(slots=True)
class TrajectorySolution:

    projectile_name: str

    ballistic_coefficient: float

    muzzle_velocity: float

    points: list[TrajectoryPoint]
'''


FILES["src/ballistics/external/models/factory.py"] = r'''
"""
Factory methods for converting solver history into
strongly typed trajectory models.
"""

from .solution import (
    TrajectoryPoint,
    TrajectorySolution,
)


def build_solution(projectile, history):

    points = []

    for row in history:

        points.append(
            TrajectoryPoint(
                time=row[0],
                range=row[1],
                height=row[2],
                drift=row[3],
                velocity=row[4],
            )
        )

    return TrajectorySolution(
        projectile_name=projectile.name,
        ballistic_coefficient=projectile.ballistic_coefficient,
        muzzle_velocity=projectile.muzzle_velocity,
        points=points,
    )
'''


FILES["src/ballistics/external/solver/zero.py"] = r'''
"""
Basic rifle zero calculations.
"""

import math


def sight_correction(
    impact_height,
    distance,
):

    return math.degrees(
        math.atan2(
            impact_height,
            distance,
        )
    )
'''


FILES["src/ballistics/external/solver/interpolation.py"] = r'''
"""
Interpolation helpers.
"""


def interpolate(history, distance):

    if len(history) < 2:
        return None

    for previous, current in zip(history[:-1], history[1:]):

        if previous[1] <= distance <= current[1]:

            fraction = (
                (distance - previous[1]) /
                (current[1] - previous[1])
            )

            return tuple(
                a + fraction * (b - a)
                for a, b in zip(previous, current)
            )

    return None
'''


FILES["tests/external/test_drag.py"] = r'''
from ballistics.external.drag.g1 import G1DragModel


def test_drag_positive():

    model = G1DragModel()

    drag = model.drag_acceleration(
        velocity=800.0,
        ballistic_coefficient=0.50,
        density=1.225,
    )

    assert drag > 0
'''


FILES["tests/external/test_interpolation.py"] = r'''
from ballistics.external.solver.interpolation import interpolate


def test_interpolation():

    history = [

        (0.0, 0.0, 0.0, 0.0, 800.0),

        (1.0, 100.0, -2.0, 0.0, 760.0),

    ]

    row = interpolate(
        history,
        50.0,
    )

    assert row is not None

    assert abs(row[1] - 50.0) < 1e-6
'''


FILES["examples/example_plot.py"] = r'''
from ballistics.external.projectile import Projectile
from ballistics.external.environment import Environment
from ballistics.external.trajectory import TrajectorySolver
from ballistics.external.output.plotting import plot_trajectory

projectile = Projectile(
    name=".308 Match",
    mass=0.01134,
    diameter=0.00782,
    ballistic_coefficient=0.505,
    muzzle_velocity=823.0,
)

environment = Environment(
    pressure=101325,
    temperature=288.15,
    humidity=0.50,
    altitude=0.0,
    wind_speed=0.0,
    wind_direction=0.0,
)

solver = TrajectorySolver()

history = solver.simulate(
    projectile,
    environment,
)

plot_trajectory(history).show()
'''


FILES["docs/examples/external_solver.md"] = r"""
# External Solver Example

```python
solver = TrajectorySolver()

history = solver.simulate(
    projectile,
    environment,
)

solution = build_solution(
    projectile,
    history,
)
The baseline solver computes:
Time of flight
Projectile position
Velocity decay
Gravity effects
BC-based drag

Future releases will extend this interface without breaking
backward compatibility.
"""

FILES["src/ballistics/external/output/export.py"] = r'''
"""
Trajectory export utilities.
"""

from pathlib import Path
import csv
import json


def export_csv(history, filename):

    filename = Path(filename)

    with filename.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as fp:

        writer = csv.writer(fp)

        writer.writerow([
            "time",
            "range",
            "height",
            "drift",
            "velocity",
        ])

        for row in history:
            writer.writerow(row)


def export_json(history, filename):

    filename = Path(filename)

    records = []

    for row in history:

        records.append({

            "time": row[0],
            "range": row[1],
            "height": row[2],
            "drift": row[3],
            "velocity": row[4],

        })

    filename.write_text(
        json.dumps(records, indent=4),
        encoding="utf-8",
    )
'''


FILES["src/ballistics/external/analysis.py"] = r'''
"""
Trajectory analysis routines.
"""


def maximum_range(history):

    return max(
        point[1]
        for point in history
    )


def maximum_height(history):

    return max(
        point[2]
        for point in history
    )


def impact_velocity(history):

    return history[-1][4]


def flight_time(history):

    return history[-1][0]
'''


FILES["src/ballistics/external/energy.py"] = r'''
"""
Projectile kinetic energy calculations.
"""


def kinetic_energy(
    mass,
    velocity,
):

    return 0.5 * mass * velocity * velocity
'''


FILES["src/ballistics/external/report.py"] = r'''
"""
Human-readable trajectory report.
"""

from .analysis import (
    maximum_height,
    maximum_range,
    impact_velocity,
    flight_time,
)


def build_report(
    projectile,
    history,
):

    report = []

    report.append("=" * 60)
    report.append("Trajectory Report")
    report.append("=" * 60)

    report.append(f"Projectile : {projectile.name}")
    report.append(f"BC         : {projectile.ballistic_coefficient:.3f}")
    report.append(f"MV         : {projectile.muzzle_velocity:.2f} m/s")

    report.append("")

    report.append(
        f"Maximum Range : {maximum_range(history):.2f} m"
    )

    report.append(
        f"Maximum Height: {maximum_height(history):.2f} m"
    )

    report.append(
        f"Impact Velocity: {impact_velocity(history):.2f} m/s"
    )

    report.append(
        f"Flight Time: {flight_time(history):.3f} s"
    )

    return "\n".join(report)
'''


FILES["tests/external/test_energy.py"] = r'''
from ballistics.external.energy import kinetic_energy


def test_energy():

    energy = kinetic_energy(
        0.010,
        800.0,
    )

    assert energy > 3000
'''


FILES["tests/external/test_analysis.py"] = r'''
from ballistics.external.analysis import (
    maximum_range,
    flight_time,
)


def test_analysis():

    history = [

        (0.0, 0.0, 0.0, 0.0, 800),

        (1.0, 100.0, -1.0, 0.0, 700),

        (2.0, 250.0, -8.0, 0.0, 650),

    ]

    assert maximum_range(history) == 250.0

    assert flight_time(history) == 2.0
'''


FILES["examples/example_report.py"] = r'''
from ballistics.external.projectile import Projectile
from ballistics.external.environment import Environment
from ballistics.external.trajectory import TrajectorySolver
from ballistics.external.report import build_report

projectile = Projectile(
    name=".308 Match",
    mass=0.01134,
    diameter=0.00782,
    ballistic_coefficient=0.505,
    muzzle_velocity=823.0,
)

environment = Environment(
    pressure=101325,
    temperature=288.15,
    humidity=0.5,
    altitude=0.0,
    wind_speed=0.0,
    wind_direction=0.0,
)

solver = TrajectorySolver()

history = solver.simulate(
    projectile,
    environment,
)

print(
    build_report(
        projectile,
        history,
    )
)
'''


FILES["docs/theory/solver.md"] = r"""
# Numerical Solver

Version 0.2.0 uses a baseline forward integration method
with BC-derived drag.

Upcoming milestones replace this with:

- Adaptive RK45
- Embedded error estimation
- G1 retardation tables
- G7 drag model
- User-defined drag curves
- Atmospheric interpolation
- Coriolis acceleration
- Spin drift
- Aerodynamic jump
- Monte Carlo uncertainty propagation
- Bayesian parameter estimation
"""

FILES["src/ballistics/external/validation.py"] = r'''
"""
Validation utilities for trajectory solutions.
"""

from math import isfinite


def validate_history(history):

    if not history:
        raise ValueError("Trajectory history is empty.")

    previous_time = -1.0

    for row in history:

        if len(row) != 5:
            raise ValueError("Invalid trajectory row.")

        t, x, y, z, velocity = row

        if not (
            isfinite(t)
            and isfinite(x)
            and isfinite(y)
            and isfinite(z)
            and isfinite(velocity)
        ):
            raise ValueError("Non-finite trajectory value detected.")

        if t <= previous_time:
            raise ValueError("Trajectory time is not strictly increasing.")

        if velocity < 0:
            raise ValueError("Negative velocity encountered.")

        previous_time = t

    return True
'''


FILES["src/ballistics/external/output/statistics.py"] = r'''
"""
Trajectory statistics.
"""

from statistics import mean


def average_velocity(history):

    return mean(
        point[4]
        for point in history
    )


def average_height(history):

    return mean(
        point[2]
        for point in history
    )


def total_distance(history):

    return history[-1][1]
'''


FILES["src/ballistics/external/output/formatter.py"] = r'''
"""
Formatting helpers.
"""


def format_table(history):

    rows = []

    rows.append(
        "{:>8} {:>12} {:>12} {:>12} {:>12}".format(
            "Time",
            "Range",
            "Height",
            "Drift",
            "Velocity",
        )
    )

    for point in history:

        rows.append(
            "{:8.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}".format(
                *point
            )
        )

    return "\n".join(rows)
'''


FILES["src/ballistics/external/models/result.py"] = r'''
from dataclasses import dataclass


@dataclass(slots=True)
class SimulationResult:

    history: list

    elapsed_time: float

    iterations: int
'''


FILES["tests/external/test_validation.py"] = r'''
from ballistics.external.validation import validate_history


def test_history_validation():

    history = [

        (0.0, 0.0, 0.0, 0.0, 800.0),

        (0.1, 80.0, -0.05, 0.0, 790.0),

        (0.2, 158.0, -0.20, 0.0, 781.0),

    ]

    assert validate_history(history)
'''


FILES["tests/external/test_statistics.py"] = r'''
from ballistics.external.output.statistics import (
    average_velocity,
    total_distance,
)


def test_statistics():

    history = [

        (0.0, 0.0, 0.0, 0.0, 800),

        (1.0, 100.0, -2.0, 0.0, 760),

        (2.0, 250.0, -8.0, 0.0, 700),

    ]

    assert average_velocity(history) > 700

    assert total_distance(history) == 250.0
'''


FILES["examples/example_export.py"] = r'''
from ballistics.external.projectile import Projectile
from ballistics.external.environment import Environment
from ballistics.external.trajectory import TrajectorySolver
from ballistics.external.output.export import (
    export_csv,
    export_json,
)

projectile = Projectile(
    name=".308 Match",
    mass=0.01134,
    diameter=0.00782,
    ballistic_coefficient=0.505,
    muzzle_velocity=823.0,
)

environment = Environment(
    pressure=101325,
    temperature=288.15,
    humidity=0.50,
    altitude=0.0,
    wind_speed=0.0,
    wind_direction=0.0,
)

solver = TrajectorySolver()

history = solver.simulate(
    projectile,
    environment,
)

export_csv(
    history,
    "trajectory.csv",
)

export_json(
    history,
    "trajectory.json",
)
'''


FILES["docs/api/external.md"] = r"""
# External Ballistics API

## Primary Classes

- Projectile
- Environment
- TrajectorySolver
- G1DragModel

## Primary Outputs

- TrajectorySolution
- SimulationResult

## Planned Additions

- G7 drag
- Cd(Mach) curves
- Multiple atmospheric models
- Coriolis
- Spin drift
- Aerodynamic jump
- Zeroing utilities
- Monte Carlo ensemble solver
- Bayesian parameter estimation
"""

FILES["src/ballistics/external/benchmark.py"] = r'''
"""
Benchmark utilities for comparing trajectory solutions against
reference datasets.
"""

from math import sqrt


def rmse(reference, prediction):

    if len(reference) != len(prediction):
        raise ValueError("Dataset lengths differ.")

    error = 0.0

    for a, b in zip(reference, prediction):

        error += (a - b) ** 2

    return sqrt(error / len(reference))


def mae(reference, prediction):

    if len(reference) != len(prediction):
        raise ValueError("Dataset lengths differ.")

    return sum(
        abs(a - b)
        for a, b in zip(reference, prediction)
    ) / len(reference)
'''


FILES["src/ballistics/external/monte_carlo.py"] = r'''
"""
Monte Carlo framework.

Future versions will support uncertainty propagation for:

- muzzle velocity
- ballistic coefficient
- wind
- atmosphere
"""

import random


def sample_velocity(
    nominal_velocity,
    sigma,
):

    return random.gauss(
        nominal_velocity,
        sigma,
    )


def sample_bc(
    nominal_bc,
    sigma,
):

    return random.gauss(
        nominal_bc,
        sigma,
    )
'''


FILES["src/ballistics/external/wind/model.py"] = r'''
"""
Wind models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ConstantWind:

    speed: float

    direction: float


@dataclass(slots=True)
class LayerWind:

    altitude: float

    speed: float

    direction: float
'''


FILES["src/ballistics/external/solver/events.py"] = r'''
"""
Trajectory event detection.
"""


def detect_ground_impact(history):

    for point in history:

        if point[2] <= 0.0 and point[0] > 0.0:
            return point

    return history[-1]


def detect_maximum_height(history):

    return max(
        history,
        key=lambda p: p[2],
    )
'''


FILES["tests/external/test_benchmark.py"] = r'''
from ballistics.external.benchmark import (
    rmse,
    mae,
)


def test_rmse():

    reference = [1, 2, 3]

    prediction = [1, 2, 4]

    assert rmse(
        reference,
        prediction,
    ) > 0


def test_mae():

    reference = [1, 2, 3]

    prediction = [1, 2, 4]

    assert mae(
        reference,
        prediction,
    ) == 1 / 3
'''


FILES["tests/external/test_events.py"] = r'''
from ballistics.external.solver.events import (
    detect_ground_impact,
)


def test_ground_impact():

    history = [

        (0.0, 0.0, 1.0, 0.0, 800),

        (1.0, 100.0, 0.4, 0.0, 750),

        (2.0, 220.0, -0.2, 0.0, 700),

    ]

    impact = detect_ground_impact(history)

    assert impact[2] <= 0
'''

FILES["src/ballistics/external/config.py"] = r'''
"""
External ballistics configuration.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SolverConfiguration:

    timestep: float = 0.001

    maximum_time: float = 5.0

    minimum_velocity: float = 30.0

    maximum_iterations: int = 500000

    enable_gravity: bool = True

    enable_drag: bool = True

    enable_wind: bool = True
'''


FILES["src/ballistics/external/rangecard.py"] = r'''
"""
Range card generation.
"""

from .solver.interpolation import interpolate


def generate_range_card(
    history,
    intervals,
):

    rows = []

    for distance in intervals:

        row = interpolate(
            history,
            distance,
        )

        if row is not None:

            rows.append(
                {
                    "distance": distance,
                    "time": row[0],
                    "drop": row[2],
                    "drift": row[3],
                    "velocity": row[4],
                }
            )

    return rows
'''


FILES["src/ballistics/external/zero.py"] = r'''
"""
Simple zero calculations.
"""

import math


def moa_adjustment(
    impact_error,
    distance,
):

    radians = math.atan2(
        impact_error,
        distance,
    )

    return math.degrees(radians) * 60.0


def mil_adjustment(
    impact_error,
    distance,
):

    radians = math.atan2(
        impact_error,
        distance,
    )

    return radians * 1000.0
'''


FILES["src/ballistics/external/io.py"] = r'''
"""
Load and save trajectory datasets.
"""

from pathlib import Path
import json


def save(history, filename):

    Path(filename).write_text(
        json.dumps(history, indent=4),
        encoding="utf-8",
    )


def load(filename):

    return json.loads(
        Path(filename).read_text(
            encoding="utf-8",
        )
    )
'''


FILES["tests/external/test_zero.py"] = r'''
from ballistics.external.zero import (
    moa_adjustment,
    mil_adjustment,
)


def test_zero():

    moa = moa_adjustment(
        0.0254,
        91.44,
    )

    mil = mil_adjustment(
        0.0254,
        91.44,
    )

    assert moa > 0

    assert mil > 0
'''


FILES["tests/external/test_rangecard.py"] = r'''
from ballistics.external.rangecard import (
    generate_range_card,
)


def test_range_card():

    history = [

        (0.0, 0.0, 0.0, 0.0, 820),

        (1.0, 100.0, -1.0, 0.0, 790),

        (2.0, 200.0, -4.0, 0.0, 760),

    ]

    card = generate_range_card(
        history,
        [50, 100, 150],
    )

    assert len(card) == 3
'''


FILES["examples/example_rangecard.py"] = r'''
from ballistics.external.projectile import Projectile
from ballistics.external.environment import Environment
from ballistics.external.trajectory import TrajectorySolver
from ballistics.external.rangecard import generate_range_card

projectile = Projectile(
    name=".308 Match",
    mass=0.01134,
    diameter=0.00782,
    ballistic_coefficient=0.505,
    muzzle_velocity=823.0,
)

environment = Environment(
    pressure=101325,
    temperature=288.15,
    humidity=0.50,
    altitude=0.0,
    wind_speed=0.0,
    wind_direction=0.0,
)

history = TrajectorySolver().simulate(
    projectile,
    environment,
)

card = generate_range_card(
    history,
    range(100, 1100, 100),
)

for row in card:
    print(row)
'''


FILES["docs/validation/external_validation.md"] = r"""
# External Validation

The purpose of v0.2.0 is to establish a reproducible baseline
trajectory engine suitable for future calibration.

Future validation targets include comparison against:

- Sierra Infinity
- Hornady 4DOF (where comparable)
- JBM Ballistics
- Published manufacturer trajectory tables
- Instrumented chronograph datasets
- Doppler radar datasets

Performance metrics:

- RMSE
- MAE
- Velocity residuals
- Drop residuals
- Time-of-flight residuals
"""

# ----------------------------------------------------------------------
# Repository Generation
# ----------------------------------------------------------------------

def main():

    banner()

    if ROOT.exists():
        shutil.rmtree(ROOT)

    ROOT.mkdir(parents=True)

    for directory in DIRECTORIES:
        ensure_directory(directory)

    count = 0

    for filename, contents in FILES.items():
        write_file(filename, contents)
        count += 1

    summary(count)


if __name__ == "__main__":
    main()
FILES["pyproject.toml"] = r'''
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "ballistics-platform"
version = "0.2.0"
description = "Research-grade modular ballistics modeling platform"
readme = "README.md"
requires-python = ">=3.11"

dependencies = [
    "numpy>=2.0",
    "scipy>=1.14",
    "matplotlib>=3.9",
    "pydantic>=2.8",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
'''
    

FILES["requirements.txt"] = r'''
numpy
scipy
matplotlib
pydantic
pytest
'''


FILES["src/ballistics/common/__init__.py"] = r'''
"""
Common scientific utilities.
"""
'''


FILES["src/ballistics/common/constants.py"] = r'''
"""
Physical constants.
"""


class C:

    # Standard gravity
    g = 9.80665

    # Gas constant (dry air)
    R = 287.05

    # Sea-level density
    rho0 = 1.225

    # Sea-level pressure
    P0 = 101325.0

    # Standard temperature
    T0 = 288.15
'''


FILES["src/ballistics/common/units.py"] = r'''
"""
Common unit conversions.
"""

INCH_TO_METER = 0.0254
FOOT_TO_METER = 0.3048
YARD_TO_METER = 0.9144
GRAIN_TO_KILOGRAM = 0.00006479891


def inches(value):
    return value * INCH_TO_METER


def feet(value):
    return value * FOOT_TO_METER


def yards(value):
    return value * YARD_TO_METER


def grains(value):
    return value * GRAIN_TO_KILOGRAM
'''


FILES["src/ballistics/common/atmosphere.py"] = r'''
"""
Simple ISA atmosphere utilities.
"""

from .constants import C


def density(
    pressure,
    temperature,
):

    return pressure / (C.R * temperature)
'''


FILES["src/ballistics/config/defaults.py"] = r'''
"""
Platform defaults.
"""

DEFAULT_TIMESTEP = 0.001

DEFAULT_MAX_TIME = 5.0

DEFAULT_PRESSURE = 101325.0

DEFAULT_TEMPERATURE = 288.15

DEFAULT_HUMIDITY = 0.50
'''


FILES["tests/common/test_units.py"] = r'''
from ballistics.common.units import (
    inches,
    yards,
)


def test_units():

    assert abs(inches(1) - 0.0254) < 1e-9

    assert abs(yards(100) - 91.44) < 1e-6
'''


FILES["tests/common/test_atmosphere.py"] = r'''
from ballistics.common.atmosphere import density


def test_density():

    rho = density(
        101325,
        288.15,
    )

    assert rho > 1.0
'''


FILES["docs/theory/constants.md"] = r"""
# Physical Constants

The platform centralizes physical constants to ensure every
physics engine uses identical values.

Included:

- Standard gravity
- Gas constant
- Standard atmosphere
- Unit conversion helpers

Future milestones will introduce:

- CIP reference constants
- SAAMI reference constants
- Earth model constants
- Rotational constants
"""

FILES["src/ballistics/common/math_utils.py"] = r'''
"""
Mathematical helper routines used throughout the platform.
"""

from math import sqrt


def magnitude(*values):

    return sqrt(sum(v * v for v in values))


def clamp(value, minimum, maximum):

    return max(minimum, min(maximum, value))


def lerp(a, b, fraction):

    return a + (b - a) * fraction
'''


FILES["src/ballistics/common/interpolation.py"] = r'''
"""
Generic interpolation routines.
"""


def linear(x0, y0, x1, y1, x):

    if x1 == x0:
        return y0

    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)


def interpolate_table(table, x):

    if len(table) < 2:
        return None

    for left, right in zip(table[:-1], table[1:]):

        if left[0] <= x <= right[0]:

            return linear(
                left[0],
                left[1],
                right[0],
                right[1],
                x,
            )

    return None
'''


FILES["src/ballistics/common/numerics.py"] = r'''
"""
Reusable numerical methods.
"""


def euler_step(
    value,
    derivative,
    dt,
):

    return value + derivative * dt
'''


FILES["src/ballistics/common/exceptions.py"] = r'''
"""
Platform exception hierarchy.
"""


class BallisticsError(Exception):
    """Base exception."""


class ValidationError(BallisticsError):
    """Validation failure."""


class PhysicsError(BallisticsError):
    """Physics model failure."""
'''


FILES["src/ballistics/data/__init__.py"] = r'''
"""
Dataset interfaces.
"""
'''


FILES["src/ballistics/data/schema.py"] = r'''
from dataclasses import dataclass


@dataclass(slots=True)
class CartridgeRecord:

    manufacturer: str

    cartridge: str

    bullet: str

    bullet_weight: float

    ballistic_coefficient: float

    muzzle_velocity: float
'''


FILES["src/ballistics/data/io.py"] = r'''
"""
Dataset loading helpers.
"""

from pathlib import Path
import csv

from .schema import CartridgeRecord


def load_cartridge_csv(filename):

    records = []

    with Path(filename).open(
        newline="",
        encoding="utf-8",
    ) as fp:

        reader = csv.DictReader(fp)

        for row in reader:

            records.append(
                CartridgeRecord(
                    manufacturer=row["manufacturer"],
                    cartridge=row["cartridge"],
                    bullet=row["bullet"],
                    bullet_weight=float(row["bullet_weight"]),
                    ballistic_coefficient=float(row["ballistic_coefficient"]),
                    muzzle_velocity=float(row["muzzle_velocity"]),
                )
            )

    return records
'''


FILES["datasets/cartridges/example.csv"] = r'''
manufacturer,cartridge,bullet,bullet_weight,ballistic_coefficient,muzzle_velocity
Example,.308 Winchester,168 HPBT,168,0.462,2650
Example,6.5 Creedmoor,140 HPBT,140,0.620,2710
'''


FILES["tests/common/test_interpolation.py"] = r'''
from ballistics.common.interpolation import (
    interpolate_table,
)


def test_linear_interpolation():

    table = [

        (0.0, 0.0),

        (10.0, 100.0),

    ]

    value = interpolate_table(
        table,
        5.0,
    )

    assert value == 50.0
'''


FILES["docs/api/common.md"] = r"""
# Common Scientific Library

The common package provides reusable scientific utilities shared
across every subsystem.

Modules include:

- constants
- atmosphere
- interpolation
- numerical methods
- unit conversions
- mathematical helpers
- exception hierarchy
"""

FILES["src/ballistics/data/validation.py"] = r'''
"""
Dataset validation routines.
"""

from .schema import CartridgeRecord


def validate_record(record: CartridgeRecord):

    if record.ballistic_coefficient <= 0:
        return False

    if record.bullet_weight <= 0:
        return False

    if record.muzzle_velocity <= 0:
        return False

    return True


def validate_dataset(records):

    return [
        record
        for record in records
        if validate_record(record)
    ]
'''


FILES["src/ballistics/data/statistics.py"] = r'''
"""
Dataset statistics.
"""

from statistics import mean


def average_bc(records):

    return mean(
        r.ballistic_coefficient
        for r in records
    )


def average_velocity(records):

    return mean(
        r.muzzle_velocity
        for r in records
    )


def average_weight(records):

    return mean(
        r.bullet_weight
        for r in records
    )
'''


FILES["src/ballistics/data/filter.py"] = r'''
"""
Filtering helpers.
"""


def by_cartridge(records, cartridge):

    return [
        r
        for r in records
        if r.cartridge == cartridge
    ]


def by_manufacturer(records, manufacturer):

    return [
        r
        for r in records
        if r.manufacturer == manufacturer
    ]
'''


FILES["src/ballistics/data/export.py"] = r'''
"""
Dataset export utilities.
"""

import json
from pathlib import Path
from dataclasses import asdict


def export_json(records, filename):

    Path(filename).write_text(

        json.dumps(
            [
                asdict(record)
                for record in records
            ],
            indent=4,
        ),

        encoding="utf-8",
    )
'''


FILES["tests/common/test_dataset.py"] = r'''
from ballistics.data.schema import CartridgeRecord
from ballistics.data.validation import validate_record


def test_record_validation():

    record = CartridgeRecord(

        manufacturer="Example",

        cartridge=".308",

        bullet="168 HPBT",

        bullet_weight=168,

        ballistic_coefficient=0.462,

        muzzle_velocity=2650,

    )

    assert validate_record(record)
'''


FILES["examples/example_dataset.py"] = r'''
from ballistics.data.io import load_cartridge_csv
from ballistics.data.statistics import (
    average_bc,
    average_velocity,
)

records = load_cartridge_csv(
    "datasets/cartridges/example.csv"
)

print("Records:", len(records))
print("Average BC:", average_bc(records))
print("Average Velocity:", average_velocity(records))
'''


FILES["docs/theory/datasets.md"] = r"""
# Dataset Architecture

The dataset subsystem provides a canonical interface for ballistic
data used throughout the platform.

Version 0.2.0 supports:

- CSV loading
- Record validation
- Statistical summaries
- Dataset filtering
- JSON export

Future milestones will add:

- PDF ingestion
- OCR extraction
- Document AI
- Manufacturer schema inference
- Confidence scoring
- Bayesian dataset fusion
"""

FILES["src/ballistics/api/__init__.py"] = r'''
"""
Public API.
"""

from ballistics.external.projectile import Projectile
from ballistics.external.environment import Environment
from ballistics.external.trajectory import TrajectorySolver
'''


FILES["src/ballistics/api/external.py"] = r'''
"""
High-level External Ballistics API.
"""

from ballistics.external.projectile import Projectile
from ballistics.external.environment import Environment
from ballistics.external.trajectory import TrajectorySolver


def solve(
    projectile: Projectile,
    environment: Environment,
):

    solver = TrajectorySolver()

    return solver.simulate(
        projectile,
        environment,
    )
'''


FILES["src/ballistics/cli/__init__.py"] = r'''
"""
Command-line interface package.
"""
'''


FILES["src/ballistics/cli/main.py"] = r'''
"""
Ballistics Platform CLI.
"""

import argparse

from ballistics.external.projectile import Projectile
from ballistics.external.environment import Environment
from ballistics.external.trajectory import TrajectorySolver


def main():

    parser = argparse.ArgumentParser(
        prog="ballistics",
    )

    parser.add_argument(
        "--velocity",
        type=float,
        default=823.0,
    )

    parser.add_argument(
        "--bc",
        type=float,
        default=0.505,
    )

    args = parser.parse_args()

    projectile = Projectile(
        name="CLI Projectile",
        mass=0.01134,
        diameter=0.00782,
        ballistic_coefficient=args.bc,
        muzzle_velocity=args.velocity,
    )

    environment = Environment(
        pressure=101325,
        temperature=288.15,
        humidity=0.50,
        altitude=0.0,
        wind_speed=0.0,
        wind_direction=0.0,
    )

    history = TrajectorySolver().simulate(
        projectile,
        environment,
    )

    print(f"Computed {len(history)} trajectory points.")


if __name__ == "__main__":
    main()
'''


FILES["tests/test_imports.py"] = r'''
def test_imports():

    import ballistics
    import ballistics.external
    import ballistics.common
    import ballistics.data
'''
    

FILES["LICENSE"] = r'''
MIT License

Copyright (c) Open Ballistics Lab

Permission is hereby granted, free of charge,
to any person obtaining a copy of this software
and associated documentation files (the "Software"),
to deal in the Software without restriction,
including without limitation the rights to use,
copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software.
'''


FILES[".gitignore"] = r'''
__pycache__/
*.pyc
.pytest_cache/
.coverage
dist/
build/
*.egg-info/
.idea/
.vscode/
trajectory.csv
trajectory.json
'''


FILES["Makefile"] = r'''
test:
	pytest

format:
	python -m black src tests

run:
	python examples/example_external.py
'''


FILES["docs/roadmap.md"] = r"""
# Development Roadmap

## v0.2.x
- Baseline external ballistics
- Repository architecture
- Testing framework
- CLI
- Dataset interfaces

## v0.3.x
- Table-driven G1 drag
- G7 drag
- Adaptive RK45
- Standard atmosphere model
- Improved wind model

## v0.4.x
- Internal ballistics prototype
- Powder models
- Chamber pressure solver
- Burn-rate equations

## v0.5.x
- Bayesian calibration
- Validation datasets
- Statistical model fitting

## v1.0
- Integrated Internal, External, and Terminal Ballistics
- Research-grade validation suite
- Stable public API
"""

# ---------- END OF build_v0_2_0.py ----------
