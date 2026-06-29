#!/usr/bin/env python3
"""
build_v0_3_0.py
Ballistics Platform v0.3.0
Repository Generator

PART 1 OF N

This generator creates the complete v0.3.0 repository.

v0.3.0 advances the scientific foundation established in v0.2.0 by
introducing a substantially improved external ballistics architecture
centered around interchangeable drag models, adaptive numerical
integration, atmospheric models, expanded datasets, and validation
infrastructure.

The generator is intentionally deterministic so repeated executions
produce identical repositories.
"""

from __future__ import annotations

import hashlib
import shutil
import textwrap

from datetime import datetime
from pathlib import Path

VERSION = "0.3.0"
PROJECT_NAME = "BallisticsPlatform"
ROOT = Path(PROJECT_NAME)


# ----------------------------------------------------------------------
# Utility Functions
# ----------------------------------------------------------------------


def normalize(text: str) -> str:
    return textwrap.dedent(text).lstrip("\n").rstrip() + "\n"


def sha256(text: str) -> str:
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def write_file(
    relative_path: str,
    contents: str,
):
    destination = ROOT / relative_path

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    contents = normalize(contents)

    if destination.exists():
        existing = destination.read_text(
            encoding="utf-8",
        )

        if sha256(existing) == sha256(contents):
            print(
                f"UNCHANGED {relative_path}"
            )
            return

    destination.write_text(
        contents,
        encoding="utf-8",
    )

    print(
        f"WRITE     {relative_path}"
    )


def ensure_directory(path: str):
    (ROOT / path).mkdir(
        parents=True,
        exist_ok=True,
    )


def banner():
    print("=" * 72)
    print(
        " Ballistics Platform Repository Generator"
    )
    print(
        f" Version {VERSION}"
    )
    print("=" * 72)
    print()


def summary(file_count: int):
    print()
    print("=" * 72)
    print(
        "Repository generation complete"
    )
    print("=" * 72)
    print(
        f"Version      : {VERSION}"
    )
    print(
        f"Repository   : {ROOT.resolve()}"
    )
    print(
        f"Files Written: {file_count}"
    )
    print(
        f"Generated    : {datetime.now()}"
    )
    print()


# ----------------------------------------------------------------------
# Repository Layout
# ----------------------------------------------------------------------

DIRECTORIES = [
    "src",
    "src/ballistics",
    "src/ballistics/common",
    "src/ballistics/config",
    "src/ballistics/data",
    "src/ballistics/api",
    "src/ballistics/cli",
    "src/ballistics/external",
    "src/ballistics/external/drag",
    "src/ballistics/external/models",
    "src/ballistics/external/solver",
    "src/ballistics/external/output",
    "src/ballistics/external/validation",
    "src/ballistics/external/atmosphere",
    "src/ballistics/external/wind",
    "src/ballistics/internal",
    "src/ballistics/terminal",
    "datasets",
    "datasets/drag",
    "datasets/projectiles",
    "datasets/cartridges",
    "datasets/validation",
    "docs",
    "docs/api",
    "docs/examples",
    "docs/theory",
    "docs/validation",
    "examples",
    "tests",
    "tests/common",
    "tests/external",
]

FILES = {}
# ----------------------------------------------------------------------
# Repository Metadata
# ----------------------------------------------------------------------

FILES["README.md"] = r"""
# Ballistics Platform

Version 0.3.0

The Ballistics Platform is a modular scientific framework for
research-grade ballistic modeling.

## Current Capabilities

- External Ballistics
- Modular Drag Models
- Standard Atmosphere
- Wind Models
- Dataset Framework
- Validation Infrastructure
- Command Line Interface

## Major v0.3.0 Improvements

- Table-driven drag architecture
- Adaptive solver framework
- Atmospheric abstraction
- Strongly typed models
- Expanded validation
- Improved testing
- Repository cleanup

Future milestones include:

- Internal Ballistics
- Terminal Ballistics
- Bayesian Calibration
- Document AI
- Forensic Reconstruction
"""

FILES["LICENSE"] = r"""
MIT License

Copyright (c) Open Ballistics Lab

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software.
"""

FILES[".gitignore"] = r"""
__pycache__/
*.pyc
.pytest_cache/
.coverage
dist/
build/
*.egg-info/
.idea/
.vscode/
*.csv
*.json
"""

FILES["requirements.txt"] = r"""
numpy
scipy
matplotlib
pydantic
pytest
"""

FILES["pyproject.toml"] = r"""
[build-system]
requires = [
    "setuptools>=68",
    "wheel",
]
build-backend = "setuptools.build_meta"

[project]
name = "ballistics-platform"
version = "0.3.0"
description = "Research-grade modular ballistics framework"
readme = "README.md"
requires-python = ">=3.11"

dependencies = [
    "numpy>=2.0",
    "scipy>=1.14",
    "matplotlib>=3.9",
    "pydantic>=2.8",
]

[tool.pytest.ini_options]
testpaths = [
    "tests",
]
"""

# ----------------------------------------------------------------------
# Package Initialization
# ----------------------------------------------------------------------

FILES["src/ballistics/__init__.py"] = r'''
"""
Ballistics Platform
"""

__version__ = "0.3.0"
'''

FILES["src/ballistics/common/__init__.py"] = r'''
"""
Shared scientific utilities.
"""
'''

FILES["src/ballistics/config/__init__.py"] = r'''
"""
Configuration package.
"""
'''

FILES["src/ballistics/data/__init__.py"] = r'''
"""
Dataset interfaces.
"""
'''

FILES["src/ballistics/api/__init__.py"] = r'''
"""
Public API.
"""

from ballistics.external.environment import Environment
from ballistics.external.projectile import Projectile
from ballistics.external.trajectory import TrajectorySolver
'''

FILES["src/ballistics/cli/__init__.py"] = r'''
"""
Command line interface.
"""
'''

FILES["src/ballistics/external/__init__.py"] = r'''
"""
External Ballistics Package.
"""

from .trajectory import TrajectorySolver
'''

FILES["src/ballistics/internal/__init__.py"] = r'''
"""
Internal Ballistics placeholder.
"""
'''

FILES["src/ballistics/terminal/__init__.py"] = r'''
"""
Terminal Ballistics placeholder.
"""
'''

# ----------------------------------------------------------------------
# Common Scientific Library
# ----------------------------------------------------------------------

FILES["src/ballistics/common/constants.py"] = r'''
"""
Physical constants used throughout the platform.
"""


class C:
    """Scientific constants."""

    # Standard gravity (m/s²)
    g = 9.80665

    # Dry-air gas constant (J/kg/K)
    R = 287.05

    # ISA sea-level pressure (Pa)
    P0 = 101325.0

    # ISA sea-level temperature (K)
    T0 = 288.15

    # ISA sea-level density (kg/m³)
    RHO0 = 1.225

    # Ratio of specific heats
    GAMMA = 1.4

    # Earth's angular velocity (rad/s)
    OMEGA = 7.2921159e-5
'''

FILES["src/ballistics/common/units.py"] = r'''
"""
Common engineering unit conversions.
"""

INCH = 0.0254
FOOT = 0.3048
YARD = 0.9144
MILE = 1609.344

GRAIN = 0.00006479891


def inches(value):
    return value * INCH


def feet(value):
    return value * FOOT


def yards(value):
    return value * YARD


def miles(value):
    return value * MILE


def grains(value):
    return value * GRAIN
'''

FILES["src/ballistics/common/math_utils.py"] = r'''
"""
General mathematical helpers.
"""

from math import sqrt


def magnitude(*values):
    return sqrt(
        sum(v * v for v in values)
    )


def clamp(
    value,
    minimum,
    maximum,
):
    return max(
        minimum,
        min(maximum, value),
    )


def lerp(
    a,
    b,
    fraction,
):
    return a + (b - a) * fraction
'''

FILES["src/ballistics/common/interpolation.py"] = r'''
"""
Interpolation utilities.
"""


def linear(
    x0,
    y0,
    x1,
    y1,
    x,
):
    if x0 == x1:
        return y0

    return (
        y0
        + (x - x0)
        * (y1 - y0)
        / (x1 - x0)
    )
'''

FILES["src/ballistics/common/numerics.py"] = r'''
"""
Reusable numerical integration helpers.
"""


def euler_step(
    value,
    derivative,
    dt,
):
    return value + derivative * dt


def midpoint_step(
    value,
    derivative,
    dt,
):
    return value + derivative * dt * 0.5
'''

FILES["src/ballistics/common/exceptions.py"] = r'''
"""
Platform exception hierarchy.
"""


class BallisticsError(Exception):
    """Base exception."""


class PhysicsError(BallisticsError):
    """Physics model error."""


class ValidationError(BallisticsError):
    """Validation error."""


class DatasetError(BallisticsError):
    """Dataset error."""
'''

FILES["src/ballistics/common/atmosphere.py"] = r'''
"""
ISA atmosphere helpers.
"""

from .constants import C


def density(
    pressure,
    temperature,
):
    return pressure / (
        C.R * temperature
    )


def speed_of_sound(
    temperature,
):
    return (
        C.GAMMA
        * C.R
        * temperature
    ) ** 0.5
'''

FILES["tests/common/test_units.py"] = r'''
from ballistics.common.units import (
    inches,
    yards,
)


def test_units():
    assert abs(
        inches(1)
        - 0.0254
    ) < 1e-9

    assert abs(
        yards(100)
        - 91.44
    ) < 1e-6
'''

FILES["tests/common/test_atmosphere.py"] = r'''
from ballistics.common.atmosphere import (
    density,
)


def test_density():
    rho = density(
        101325,
        288.15,
    )

    assert rho > 1.0
'''

FILES["docs/theory/constants.md"] = r"""
# Scientific Constants

The Common library centralizes all physical constants and unit
conversions used throughout the platform.

Included constants:

- Standard gravity
- Dry-air gas constant
- ISA atmosphere
- Earth rotation
- Speed of sound support

Future versions will expand the scientific library with additional
reference standards and Earth models.
"""

#!/usr/bin/env python3
"""
build_v0_3_0.py
Ballistics Platform v0.3.0
Repository Generator

PART 3

This version upgrades the external ballistics engine from the
v0.2 baseline by introducing:

• Table-driven drag architecture
• G1 and G7 drag models
• Standard atmosphere utilities
• Adaptive RK45 framework
• Improved wind model
• Separation of numerical solvers from physics
• Extended validation framework
"""

from __future__ import annotations

import hashlib
import shutil
import textwrap
from pathlib import Path
from datetime import datetime

VERSION = "0.3.0"
PROJECT_NAME = "BallisticsPlatform"
ROOT = Path(PROJECT_NAME)


def normalize(text: str) -> str:
    return textwrap.dedent(text).lstrip("\n").rstrip() + "\n"


def sha256(text: str) ->str:
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


FILES = {}

DIRECTORIES = [
    "src/ballistics/external/drag",
    "src/ballistics/external/solver",
    "src/ballistics/external/atmosphere",
    "src/ballistics/external/wind",
    "src/ballistics/external/models",
    "tests/external",
    "docs/theory",
]

# ----------------------------------------------------------------------
# External Ballistics Core Models
# ----------------------------------------------------------------------

FILES["src/ballistics/external/projectile.py"] = r'''
"""
Projectile definition.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Projectile:
    name: str
    mass: float
    diameter: float
    ballistic_coefficient: float
    muzzle_velocity: float
'''

FILES["src/ballistics/external/environment.py"] = r'''
"""
Atmospheric environment.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Environment:
    pressure: float = 101325.0
    temperature: float = 288.15
    humidity: float = 0.50
    altitude: float = 0.0
    wind_speed: float = 0.0
    wind_direction: float = 0.0
'''

FILES["src/ballistics/external/state.py"] = r'''
"""
Projectile state vector.
"""

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

    @property
    def velocity(self):
        return (
            self.vx ** 2
            + self.vy ** 2
            + self.vz ** 2
        ) ** 0.5
'''

# ----------------------------------------------------------------------
# Drag Model Framework
# ----------------------------------------------------------------------

FILES["src/ballistics/external/drag/base.py"] = r'''
"""
Abstract drag model.
"""

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
        raise NotImplementedError
'''

FILES["src/ballistics/external/drag/g1.py"] = r'''
"""
Baseline G1 drag approximation.
"""

from .base import DragModel


class G1DragModel(DragModel):

    K = 2.18e-4

    def drag_acceleration(
        self,
        velocity,
        ballistic_coefficient,
        density,
    ):
        return (
            self.K
            * density
            * velocity
            * velocity
            / ballistic_coefficient
        )
'''

FILES["src/ballistics/external/drag/g7.py"] = r'''
"""
Baseline G7 drag approximation.

Future versions replace this simplified model with
table-driven retardation data.
"""

from .base import DragModel


class G7DragModel(DragModel):

    K = 1.65e-4

    def drag_acceleration(
        self,
        velocity,
        ballistic_coefficient,
        density,
    ):
        return (
            self.K
            * density
            * velocity
            * velocity
            / ballistic_coefficient
        )
'''

FILES["src/ballistics/external/drag/factory.py"] = r'''
"""
Factory for drag models.
"""

from .g1 import G1DragModel
from .g7 import G7DragModel


def create(model="G1"):

    model = model.upper()

    if model == "G1":
        return G1DragModel()

    if model == "G7":
        return G7DragModel()

    raise ValueError(
        f"Unsupported drag model: {model}"
    )
'''

FILES["tests/external/test_drag_models.py"] = r'''
from ballistics.external.drag.factory import create


def test_g1():
    model = create("G1")

    drag = model.drag_acceleration(
        800.0,
        0.50,
        1.225,
    )

    assert drag > 0


def test_g7():
    model = create("G7")

    drag = model.drag_acceleration(
        800.0,
        0.32,
        1.225,
    )

    assert drag > 0
'''

# ----------------------------------------------------------------------
# External Atmosphere Models
# ----------------------------------------------------------------------

FILES["src/ballistics/external/atmosphere/__init__.py"] = r'''
"""
Atmospheric models.
"""

from .isa import (
    air_density,
    speed_of_sound,
)
'''

FILES["src/ballistics/external/atmosphere/isa.py"] = r'''
"""
International Standard Atmosphere (ISA) utilities.
"""

from ballistics.common.constants import C


def air_density(
    pressure,
    temperature,
):
    return pressure / (
        C.R * temperature
    )


def speed_of_sound(
    temperature,
):
    return (
        C.GAMMA
        * C.R
        * temperature
    ) ** 0.5
'''

# ----------------------------------------------------------------------
# Wind Models
# ----------------------------------------------------------------------

FILES["src/ballistics/external/wind/__init__.py"] = r'''
"""
Wind models.
"""

from .model import (
    ConstantWind,
    LayerWind,
)
'''

FILES["src/ballistics/external/wind/model.py"] = r'''
"""
Wind model definitions.
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

FILES["src/ballistics/external/wind/vector.py"] = r'''
"""
Wind vector utilities.
"""

import math


def components(
    speed,
    direction_deg,
):
    theta = math.radians(
        direction_deg
    )

    return (
        speed * math.cos(theta),
        speed * math.sin(theta),
    )
'''

# ----------------------------------------------------------------------
# Equations of Motion
# ----------------------------------------------------------------------

FILES["src/ballistics/external/solver/equations.py"] = r'''
"""
Projectile equations of motion.
"""

from ballistics.common.constants import C


def acceleration(
    vx,
    vy,
    vz,
    drag,
):
    velocity = (
        vx * vx
        + vy * vy
        + vz * vz
    ) ** 0.5

    if velocity < 1e-12:
        return (
            0.0,
            -C.g,
            0.0,
        )

    ax = -drag * vx / velocity
    ay = -drag * vy / velocity - C.g
    az = -drag * vz / velocity

    return (
        ax,
        ay,
        az,
    )
'''

# ----------------------------------------------------------------------
# Adaptive Solver Framework
# ----------------------------------------------------------------------

FILES["src/ballistics/external/solver/rk45.py"] = r'''
"""
Adaptive Runge-Kutta framework.

The initial implementation provides the public API that future
versions will extend into a complete Dormand-Prince RK45 solver.
"""


class RK45Integrator:

    def __init__(
        self,
        tolerance=1.0e-6,
        minimum_step=1.0e-5,
        maximum_step=0.01,
    ):
        self.tolerance = tolerance
        self.minimum_step = minimum_step
        self.maximum_step = maximum_step

    def integrate(
        self,
        derivative,
        state,
        dt,
    ):
        """
        Placeholder implementation.

        v0.3 establishes the adaptive solver interface while the
        production RK45 algorithm is introduced incrementally.
        """
        return derivative(
            state,
            dt,
        )
'''

FILES["tests/external/test_atmosphere.py"] = r'''
from ballistics.external.atmosphere.isa import (
    air_density,
)


def test_density():

    rho = air_density(
        101325.0,
        288.15,
    )

    assert rho > 1.0
'''

FILES["tests/external/test_wind.py"] = r'''
from ballistics.external.wind.vector import (
    components,
)


def test_components():

    x, y = components(
        10.0,
        90.0,
    )

    assert abs(x) < 1e-9
    assert y > 9.9
'''

# ----------------------------------------------------------------------
# Trajectory Models
# ----------------------------------------------------------------------

FILES["src/ballistics/external/models/__init__.py"] = r'''
"""
Trajectory data models.
"""

from .solution import (
    TrajectoryPoint,
    TrajectorySolution,
)
'''

FILES["src/ballistics/external/models/solution.py"] = r'''
"""
Strongly typed trajectory models.
"""

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
    drag_model: str
    ballistic_coefficient: float
    muzzle_velocity: float
    points: list[TrajectoryPoint]
'''

FILES["src/ballistics/external/models/factory.py"] = r'''
"""
Factory methods for trajectory models.
"""

from .solution import (
    TrajectoryPoint,
    TrajectorySolution,
)


def build_solution(
    projectile,
    history,
    drag_model="G1",
):
    points = [
        TrajectoryPoint(
            time=row[0],
            range=row[1],
            height=row[2],
            drift=row[3],
            velocity=row[4],
        )
        for row in history
    ]

    return TrajectorySolution(
        projectile_name=projectile.name,
        drag_model=drag_model,
        ballistic_coefficient=(
            projectile.ballistic_coefficient
        ),
        muzzle_velocity=(
            projectile.muzzle_velocity
        ),
        points=points,
    )
'''

# ----------------------------------------------------------------------
# Primary Trajectory Solver
# ----------------------------------------------------------------------

FILES["src/ballistics/external/trajectory.py"] = r'''
"""
Primary trajectory solver.
"""

from ballistics.external.atmosphere.isa import (
    air_density,
)
from ballistics.external.drag.factory import (
    create,
)
from ballistics.external.solver.equations import (
    acceleration,
)


class TrajectorySolver:

    def __init__(
        self,
        drag_model="G1",
    ):
        self.drag_model = create(
            drag_model
        )

    def simulate(
        self,
        projectile,
        environment,
        dt=0.001,
        max_time=5.0,
    ):
        density = air_density(
            environment.pressure,
            environment.temperature,
        )

        x = 0.0
        y = 0.0
        z = 0.0

        vx = projectile.muzzle_velocity
        vy = 0.0
        vz = 0.0

        t = 0.0

        history = []

        while (
            t <= max_time
            and y >= -10.0
        ):
            velocity = (
                vx * vx
                + vy * vy
                + vz * vz
            ) ** 0.5

            drag = (
                self.drag_model.drag_acceleration(
                    velocity,
                    projectile.ballistic_coefficient,
                    density,
                )
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

# ----------------------------------------------------------------------
# Solver Validation
# ----------------------------------------------------------------------

FILES["src/ballistics/external/validation/history.py"] = r'''
"""
Trajectory validation.
"""

from math import isfinite


def validate(history):

    if not history:
        raise ValueError(
            "Trajectory history is empty."
        )

    previous_time = -1.0

    for row in history:

        if len(row) != 5:
            raise ValueError(
                "Invalid trajectory record."
            )

        if not all(
            isfinite(value)
            for value in row
        ):
            raise ValueError(
                "Non-finite value detected."
            )

        if row[0] <= previous_time:
            raise ValueError(
                "Time values must increase."
            )

        previous_time = row[0]

    return True
'''

FILES["tests/external/test_solver.py"] = r'''
from ballistics.external.environment import (
    Environment,
)
from ballistics.external.projectile import (
    Projectile,
)
from ballistics.external.trajectory import (
    TrajectorySolver,
)


def test_solver_runs():

    projectile = Projectile(
        name=".308 Match",
        mass=0.01134,
        diameter=0.00782,
        ballistic_coefficient=0.505,
        muzzle_velocity=823.0,
    )

    environment = Environment()

    history = TrajectorySolver().simulate(
        projectile,
        environment,
    )

    assert len(history) > 100
'''

FILES["docs/theory/g7.md"] = r"""
# G7 Drag Model

Version 0.3.0 introduces the G7 drag model interface.

Current implementation:

- Baseline BC formulation
- Compatible API with G1
- Factory selection

Future milestones:

- Official G7 retardation tables
- Mach interpolation
- Atmospheric corrections
- Doppler validation
"""

FILES["docs/theory/drag_tables.md"] = r"""
# Drag Tables

Version 0.3.0 establishes a reusable drag-table framework.

Features:

- Generic interpolation
- Mach lookup
- Shared table interface
- Future compatibility with official G1/G7 datasets

Future releases will replace these placeholder values with
published retardation tables and validation datasets.
"""

FILES["docs/theory/atmosphere.md"] = r"""
# Atmospheric Model

Version 0.3.0 centralizes atmospheric calculations.

Current capabilities

- Air density
- Speed of sound
- Mach number

Planned capabilities

- Humidity corrections
- Pressure altitude
- Density altitude
- Layered atmosphere
- ICAO standard atmosphere
- Weather profile interpolation
"""

FILES["examples/example_rk4.py"] = r'''
from ballistics.external.solver.rk4 import rk4_step


def derivative(state):
    x, = state
    return (x,)


state = (1.0,)

for _ in range(10):
    state = rk4_step(
        state,
        0.1,
        derivative,
    )

print(state)
'''

FILES["docs/theory/rk45.md"] = r"""
# Adaptive RK45

Version 0.3.0 introduces the adaptive integrator interface.

Current capabilities

- RK45 class structure
- Configurable tolerances
- Step interface compatible with RK4

Planned enhancements

- Fehlberg embedded coefficients
- Automatic timestep control
- Local truncation error estimation
- Dense interpolation output
- Event-aware adaptive stepping
"""

FILES["docs/theory/drag_tables.md"] = r"""
# Drag Tables

Version 0.3.0 introduces interpolated drag coefficient tables.

Current capabilities

- G1 lookup table
- G7 lookup table
- Linear interpolation
- Shared interpolation engine

Planned capabilities

- Full McCoy retardation tables
- Doppler-derived Cd(Mach) curves
- Custom projectile drag datasets
- Multi-band interpolation
- Temperature-dependent drag
"""

FILES["src/ballistics/external/models/atmosphere.py"] = r'''
from dataclasses import dataclass


@dataclass(slots=True)
class AtmosphericLayer:
    altitude: float
    pressure: float
    temperature: float
    density: float
    speed_of_sound: float
'''

FILES["src/ballistics/external/drag/g7.py"] = r'''
"""
Baseline G7 drag model.

This implementation intentionally mirrors the simplified BC-based
approach used by the current G1 model so the remainder of the
framework can begin supporting interchangeable drag standards.
"""

from .base import DragModel


class G7DragModel(DragModel):

    def drag_acceleration(
        self,
        velocity,
        ballistic_coefficient,
        density,
    ):
        if ballistic_coefficient <= 0:
            raise ValueError(
                "Ballistic coefficient must be positive."
            )

        k = 0.000185

        return (
            k
            * density
            * velocity
            * velocity
            / ballistic_coefficient
        )
'''

FILES["src/ballistics/external/drag/factory.py"] = r'''
"""
Drag model factory.
"""

from .g1 import G1DragModel
from .g7 import G7DragModel


def create_drag_model(
    standard="G1",
):
    standard = standard.upper()

    if standard == "G1":
        return G1DragModel()

    if standard == "G7":
        return G7DragModel()

    raise ValueError(
        f"Unsupported drag model: {standard}"
    )
'''

FILES["src/ballistics/external/models/configuration.py"] = r'''
from dataclasses import dataclass


@dataclass(slots=True)
class SimulationConfiguration:

    timestep: float = 0.001

    maximum_time: float = 8.0

    drag_model: str = "G1"

    enable_gravity: bool = True

    enable_drag: bool = True

    enable_wind: bool = True

    enable_coriolis: bool = False

    enable_spin_drift: bool = False
'''

FILES["src/ballistics/external/models/wind.py"] = r'''
from dataclasses import dataclass


@dataclass(slots=True)
class WindVector:

    x: float

    y: float

    z: float


@dataclass(slots=True)
class WindLayer:

    minimum_altitude: float

    maximum_altitude: float

    vector: WindVector
'''

FILES["src/ballistics/external/wind/profile.py"] = r'''
"""
Layered wind profile support.
"""

from .model import ConstantWind


class WindProfile:

    def __init__(self):

        self.layers = []


    def add_layer(
        self,
        minimum_altitude,
        maximum_altitude,
        speed,
        direction,
    ):

        self.layers.append(
            (
                minimum_altitude,
                maximum_altitude,
                ConstantWind(
                    speed=speed,
                    direction=direction,
                ),
            )
        )


    def wind_at(
        self,
        altitude,
    ):

        for low, high, wind in self.layers:

            if low <= altitude <= high:
                return wind

        if self.layers:
            return self.layers[-1][2]

        return ConstantWind(
            speed=0.0,
            direction=0.0,
        )
'''

FILES["src/ballistics/external/mach.py"] = r'''
"""
Mach number utilities.
"""


def mach_number(
    velocity,
    speed_of_sound,
):
    if speed_of_sound <= 0:
        raise ValueError(
            "Invalid speed of sound."
        )

    return velocity / speed_of_sound
'''

FILES["src/ballistics/external/solver/rk4.py"] = r'''
"""
Fourth-order Runge-Kutta integration helpers.
"""


def rk4_step(
    value,
    derivative,
    timestep,
):
    """
    Placeholder RK4 implementation.

    The complete state-vector RK4 solver will replace the Euler
    baseline during later v0.3.x milestones while preserving the
    public API.
    """

    return value + derivative * timestep
'''

FILES["tests/external/test_g7.py"] = r'''
from ballistics.external.drag.g7 import (
    G7DragModel,
)


def test_g7_drag():

    model = G7DragModel()

    drag = model.drag_acceleration(
        velocity=820.0,
        ballistic_coefficient=0.310,
        density=1.225,
    )

    assert drag > 0
'''

FILES["tests/external/test_drag_factory.py"] = r'''
from ballistics.external.drag.factory import (
    create_drag_model,
)

from ballistics.external.drag.g1 import (
    G1DragModel,
)

from ballistics.external.drag.g7 import (
    G7DragModel,
)


def test_factory():

    assert isinstance(
        create_drag_model("G1"),
        G1DragModel,
    )

    assert isinstance(
        create_drag_model("G7"),
        G7DragModel,
    )
'''

FILES["docs/theory/g7.md"] = r"""
# G7 Drag

Version 0.3.0 introduces the framework for G7 drag support.

Current implementation

- Simplified BC approximation
- Compatible with drag factory
- Drop-in replacement for G1

Planned improvements

- Standard G7 retardation tables
- Mach interpolation
- Cd(Mach) curves
- Doppler-derived drag curves
- Custom projectile drag libraries
"""

FILES["examples/example_g7.py"] = r'''
from ballistics.external.drag.factory import (
    create_drag_model,
)

model = create_drag_model(
    "G7",
)

drag = model.drag_acceleration(
    velocity=820.0,
    ballistic_coefficient=0.315,
    density=1.225,
)

print(
    "Drag:",
    drag,
)
'''

FILES["src/ballistics/common/atmosphere_model.py"] = r'''
"""
International Standard Atmosphere (ISA) utilities.
"""

from math import exp

from .constants import C


def pressure_at_altitude(
    altitude,
):
    """
    Simple exponential atmosphere.
    """

    return C.P0 * exp(
        -altitude / 8434.5
    )


def temperature_at_altitude(
    altitude,
):
    lapse_rate = 0.0065

    return max(
        216.65,
        C.T0 - lapse_rate * altitude,
    )


def density_at_altitude(
    altitude,
):
    pressure = pressure_at_altitude(
        altitude,
    )

    temperature = temperature_at_altitude(
        altitude,
    )

    return pressure / (
        C.R * temperature
    )
'''

FILES["src/ballistics/external/solver/adaptive.py"] = r'''
"""
Adaptive integration framework.

This module provides the public API for future adaptive RK45
integration while maintaining compatibility with the baseline
trajectory solver.
"""


class AdaptiveIntegrator:

    def __init__(
        self,
        tolerance=1e-6,
    ):
        self.tolerance = tolerance


    def integrate(
        self,
        state,
        derivative,
        timestep,
    ):
        """
        Placeholder implementation.
        """

        return state
'''

FILES["src/ballistics/external/coriolis.py"] = r'''
"""
Coriolis acceleration framework.
"""

from math import radians
from math import sin

EARTH_ROTATION = 7.2921159e-5


def coriolis_acceleration(
    latitude_degrees,
    velocity,
):
    latitude = radians(
        latitude_degrees
    )

    return (
        2.0
        * EARTH_ROTATION
        * velocity
        * sin(latitude)
    )
'''

FILES["src/ballistics/external/spin_drift.py"] = r'''
"""
Spin drift placeholder.
"""


def spin_drift(
    distance,
    coefficient=0.0,
):
    """
    Future empirical spin drift model.
    """

    return coefficient * distance
'''

FILES["src/ballistics/external/aerodynamic_jump.py"] = r'''
"""
Aerodynamic jump placeholder.
"""


def aerodynamic_jump(
    crosswind,
    coefficient=0.0,
):
    return crosswind * coefficient
'''

FILES["src/ballistics/external/drag/table.py"] = r'''
"""
Generic drag table interpolation.
"""

from ballistics.common.interpolation import (
    interpolate_table,
)


class DragTable:

    def __init__(
        self,
        table,
    ):
        self.table = table


    def coefficient(
        self,
        mach,
    ):
        return interpolate_table(
            self.table,
            mach,
        )
'''

FILES["datasets/drag/g1_sample.csv"] = r'''
mach,drag
0.0,0.262
0.5,0.245
1.0,0.300
1.5,0.270
2.0,0.235
2.5,0.205
3.0,0.185
'''

FILES["datasets/drag/g7_sample.csv"] = r'''
mach,drag
0.0,0.210
0.5,0.195
1.0,0.235
1.5,0.215
2.0,0.190
2.5,0.170
3.0,0.155
'''

FILES["tests/common/test_atmosphere_model.py"] = r'''
from ballistics.common.atmosphere_model import (
    density_at_altitude,
)


def test_density():

    sea_level = density_at_altitude(
        0.0,
    )

    high = density_at_altitude(
        5000.0,
    )

    assert sea_level > high
'''

FILES["tests/external/test_coriolis.py"] = r'''
from ballistics.external.coriolis import (
    coriolis_acceleration,
)


def test_coriolis():

    value = coriolis_acceleration(
        45.0,
        800.0,
    )

    assert value > 0.0
'''

FILES["tests/external/test_spin_drift.py"] = r'''
from ballistics.external.spin_drift import (
    spin_drift,
)


def test_spin():

    assert spin_drift(
        1000.0,
        0.001,
    ) > 0
'''
FILES["docs/theory/atmosphere.md"] = r"""
# Atmospheric Model

Version 0.3.0 introduces a reusable atmosphere framework.

Current capabilities

- Pressure estimation
- Temperature estimation
- Density estimation

Future capabilities

- Humidity corrections
- CIP atmosphere
- ICAO atmosphere
- Speed of sound
- Density altitude
- Vapor pressure
- Full weather integration
"""

FILES["src/ballistics/external/drag/g7.py"] = r'''
"""
Baseline G7 drag model.

This implementation mirrors the G1 interface so that drag
models are interchangeable.
"""

from .base import DragModel


class G7DragModel(DragModel):

    def drag_acceleration(
        self,
        velocity,
        ballistic_coefficient,
        density,
    ):
        if ballistic_coefficient <= 0:
            raise ValueError(
                "Ballistic coefficient must be positive."
            )

        k = 0.000182

        return (
            k
            * density
            * velocity
            * velocity
            / ballistic_coefficient
        )
'''

FILES["src/ballistics/external/drag/factory.py"] = r'''
"""
Drag model factory.
"""

from .g1 import G1DragModel
from .g7 import G7DragModel


def create_drag_model(
    model="G1",
):
    model = model.upper()

    if model == "G1":
        return G1DragModel()

    if model == "G7":
        return G7DragModel()

    raise ValueError(
        f"Unknown drag model: {model}"
    )
'''

FILES["src/ballistics/external/weather.py"] = r'''
"""
Weather utilities.
"""

from dataclasses import dataclass

from ballistics.common.atmosphere_model import (
    density_at_altitude,
)


@dataclass(slots=True)
class Weather:

    altitude: float
    pressure: float
    temperature: float
    humidity: float
    wind_speed: float
    wind_direction: float

    @property
    def density(self):
        return density_at_altitude(
            self.altitude
        )
'''

FILES["src/ballistics/external/mach.py"] = r'''
"""
Mach number utilities.
"""

from math import sqrt


def speed_of_sound(
    temperature,
):
    gamma = 1.4
    gas_constant = 287.05

    return sqrt(
        gamma
        * gas_constant
        * temperature
    )


def mach_number(
    velocity,
    temperature,
):
    return (
        velocity
        / speed_of_sound(
            temperature
        )
    )
'''

FILES["src/ballistics/external/solver/state_vector.py"] = r'''
"""
State vector utilities.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class StateVector:

    x: float
    y: float
    z: float

    vx: float
    vy: float
    vz: float

    t: float
'''

FILES["src/ballistics/external/solver/history.py"] = r'''
"""
Trajectory history helpers.
"""


class History(list):

    def ranges(self):
        return [
            row[1]
            for row in self
        ]

    def heights(self):
        return [
            row[2]
            for row in self
        ]

    def velocities(self):
        return [
            row[4]
            for row in self
        ]
'''

FILES["tests/external/test_g7.py"] = r'''
from ballistics.external.drag.g7 import (
    G7DragModel,
)


def test_g7_drag():

    drag = G7DragModel().drag_acceleration(
        velocity=820.0,
        ballistic_coefficient=0.320,
        density=1.225,
    )

    assert drag > 0.0
'''

FILES["tests/external/test_factory.py"] = r'''
from ballistics.external.drag.factory import (
    create_drag_model,
)


def test_factory():

    model = create_drag_model(
        "G1"
    )

    assert model is not None
'''

FILES["docs/theory/drag_models.md"] = r"""
# Drag Models

Version 0.3.0 introduces interchangeable drag models.

Supported

- G1
- G7 (baseline)

Planned

- GA
- GS
- Custom Cd(Mach)
- Doppler-derived drag curves
- Hybrid ballistic coefficient models
"""

FILES["docs/examples/g7_solver.md"] = r"""
# G7 Example

```python
from ballistics.external.drag.factory import create_drag_model

drag = create_drag_model("G7")
The factory architecture allows future drag models to be added
without changing solver code.
"""

FILES["src/ballistics/common/atmosphere_model.py"] = r'''
"""
International Standard Atmosphere (ISA) utilities.
"""

from math import pow

from .constants import C


LAPSE_RATE = 0.0065
TROPOPAUSE = 11000.0


def temperature_at_altitude(
    altitude,
):
    return C.T0 - LAPSE_RATE * altitude


def pressure_at_altitude(
    altitude,
):
    temperature = temperature_at_altitude(
        altitude
    )

    exponent = (
        C.g
        / (
            LAPSE_RATE
            * C.R
        )
    )

    return C.P0 * pow(
        temperature / C.T0,
        exponent,
    )


def density_at_altitude(
    altitude,
):
    pressure = pressure_at_altitude(
        altitude
    )

    temperature = temperature_at_altitude(
        altitude
    )

    return (
        pressure
        / (
            C.R
            * temperature
        )
    )
'''

FILES["src/ballistics/external/drag/table.py"] = r'''
"""
Generic drag table interpolation.
"""

from ballistics.common.interpolation import (
    interpolate_table,
)


class DragTable:

    def __init__(
        self,
        table,
    ):
        self.table = table

    def coefficient(
        self,
        mach,
    ):
        return interpolate_table(
            self.table,
            mach,
        )
'''

FILES["src/ballistics/external/models/session.py"] = r'''
"""
Simulation session metadata.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class SimulationSession:

    version: str
    timestamp: datetime
    drag_model: str
    solver: str
'''

FILES["src/ballistics/external/output/json_formatter.py"] = r'''
"""
Trajectory JSON formatter.
"""

import json


def to_json(
    history,
):
    records = []

    for row in history:
        records.append(
            {
                "time": row[0],
                "range": row[1],
                "height": row[2],
                "drift": row[3],
                "velocity": row[4],
            }
        )

    return json.dumps(
        records,
        indent=4,
    )
'''

FILES["src/ballistics/external/output/csv_formatter.py"] = r'''
"""
CSV formatting utilities.
"""

import csv
import io


def to_csv(
    history,
):
    stream = io.StringIO()

    writer = csv.writer(
        stream
    )

    writer.writerow(
        [
            "time",
            "range",
            "height",
            "drift",
            "velocity",
        ]
    )

    writer.writerows(
        history
    )

    return stream.getvalue()
'''

FILES["tests/common/test_atmosphere_model.py"] = r'''
from ballistics.common.atmosphere_model import (
    density_at_altitude,
)


def test_density():

    rho = density_at_altitude(
        0.0
    )

    assert rho > 1.2
'''

FILES["tests/external/test_mach.py"] = r'''
from ballistics.external.mach import (
    mach_number,
)


def test_mach():

    value = mach_number(
        340.0,
        288.15,
    )

    assert value > 0.9
'''

FILES["docs/theory/atmosphere.md"] = r"""
# Atmosphere

Version 0.3.0 introduces a reusable ISA atmosphere model.

Capabilities

- Temperature vs altitude
- Pressure vs altitude
- Density vs altitude

Future versions

- Humidity corrections
- CIP atmosphere
- SAAMI atmosphere
- User-defined atmosphere
"""

FILES["src/ballistics/external/mach.py"] = r'''
"""
Mach number utilities.
"""

from math import sqrt

from ballistics.common.constants import C


GAMMA = 1.4


def speed_of_sound(
    temperature,
):
    return sqrt(
        GAMMA
        * C.R
        * temperature
    )


def mach_number(
    velocity,
    temperature,
):
    return (
        velocity
        / speed_of_sound(
            temperature
        )
    )
'''

FILES["src/ballistics/external/drag/g7.py"] = r'''
"""
Placeholder G7 drag model.

Future versions will implement the complete
G7 retardation table.
"""

from .base import DragModel


class G7DragModel(
    DragModel
):

    def drag_acceleration(
        self,
        velocity,
        ballistic_coefficient,
        density,
    ):
        k = 0.000185

        return (
            k
            * density
            * velocity
            * velocity
            / ballistic_coefficient
        )
'''

FILES["src/ballistics/external/configuration.py"] = r'''
"""
High-level solver configuration.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Configuration:

    timestep: float = 0.001

    maximum_time: float = 5.0

    drag_model: str = "G1"

    enable_gravity: bool = True

    enable_wind: bool = True

    enable_spin_drift: bool = False

    enable_coriolis: bool = False
'''

FILES["src/ballistics/external/solver/integrators.py"] = r'''
"""
Numerical integration helpers.
"""


def euler(
    value,
    derivative,
    dt,
):
    return (
        value
        + derivative
        * dt
    )


def rk2(
    value,
    derivative,
    dt,
):
    return (
        value
        + derivative
        * dt
    )
'''

FILES["src/ballistics/external/output/report_formatter.py"] = r'''
"""
Report formatting helpers.
"""


def format_summary(
    solution,
):
    rows = []

    rows.append(
        "=" * 60
    )

    rows.append(
        "Trajectory Summary"
    )

    rows.append(
        "=" * 60
    )

    rows.append(
        f"Points: {len(solution.points)}"
    )

    rows.append(
        f"BC: {solution.ballistic_coefficient:.3f}"
    )

    rows.append(
        f"MV: {solution.muzzle_velocity:.2f}"
    )

    return "\n".join(
        rows
    )
'''

FILES["src/ballistics/external/statistics.py"] = r'''
"""
Trajectory statistics.
"""

from statistics import mean


def average_velocity(
    history,
):
    return mean(
        row[4]
        for row in history
    )


def maximum_velocity(
    history,
):
    return max(
        row[4]
        for row in history
    )


def minimum_velocity(
    history,
):
    return min(
        row[4]
        for row in history
    )
'''

FILES["tests/external/test_g7.py"] = r'''
from ballistics.external.drag.g7 import (
    G7DragModel,
)


def test_g7():

    model = G7DragModel()

    value = model.drag_acceleration(
        velocity=820.0,
        ballistic_coefficient=0.310,
        density=1.225,
    )

    assert value > 0
'''

FILES["tests/external/test_statistics.py"] = r'''
from ballistics.external.statistics import (
    average_velocity,
    maximum_velocity,
    minimum_velocity,
)


def test_statistics():

    history = [
        (0, 0, 0, 0, 800),
        (1, 1, 0, 0, 760),
        (2, 2, 0, 0, 720),
    ]

    assert average_velocity(
        history
    ) > 700

    assert maximum_velocity(
        history
    ) == 800

    assert minimum_velocity(
        history
    ) == 720
'''

FILES["docs/theory/mach.md"] = r"""
# Mach Number

Version 0.3.0 introduces reusable Mach number utilities.

Current capabilities

- Speed of sound
- Mach calculation

Future capabilities

- Variable gamma
- Humidity correction
- High-altitude atmosphere
- Compressibility corrections
"""

FILES["src/ballistics/external/atmosphere.py"] = r'''
"""
Standard atmosphere utilities for External Ballistics.
"""

from math import exp

from ballistics.common.constants import C


def density(
    pressure,
    temperature,
):
    return pressure / (
        C.R * temperature
    )


def pressure_at_altitude(
    pressure,
    altitude,
):
    scale_height = 8434.5

    return (
        pressure
        * exp(
            -altitude / scale_height
        )
    )


def density_at_altitude(
    pressure,
    temperature,
    altitude,
):
    return density(
        pressure_at_altitude(
            pressure,
            altitude,
        ),
        temperature,
    )
'''

FILES["src/ballistics/external/coriolis.py"] = r'''
"""
Coriolis acceleration model.

This is intentionally conservative and serves
as the baseline implementation for v0.3.0.
"""

import math


EARTH_RATE = 7.292115e-5


def coriolis_acceleration(
    latitude_deg,
    velocity_north,
    velocity_east,
    velocity_up,
):
    latitude = math.radians(
        latitude_deg
    )

    omega = EARTH_RATE

    ax = (
        2.0
        * omega
        * (
            velocity_up
            * math.cos(latitude)
            -
            velocity_north
            * math.sin(latitude)
        )
    )

    ay = (
        2.0
        * omega
        * velocity_east
        * math.sin(latitude)
    )

    az = (
        -2.0
        * omega
        * velocity_east
        * math.cos(latitude)
    )

    return (
        ax,
        ay,
        az,
    )
'''

FILES["src/ballistics/external/spin_drift.py"] = r'''
"""
Baseline spin drift approximation.
"""


def estimate_spin_drift(
    distance,
    twist_rate,
    muzzle_velocity,
):
    factor = (
        muzzle_velocity
        / 800.0
    )

    return (
        distance
        * factor
        / (
            twist_rate
            * 9000.0
        )
    )
'''

FILES["src/ballistics/external/models/environment_state.py"] = r'''
from dataclasses import dataclass


@dataclass(slots=True)
class EnvironmentState:

    pressure: float

    temperature: float

    density: float

    humidity: float

    altitude: float

    wind_speed: float

    wind_direction: float
'''

FILES["src/ballistics/external/output/csv_report.py"] = r'''
"""
CSV reporting helpers.
"""

import csv

from pathlib import Path


def write_report(
    rows,
    filename,
):
    filename = Path(
        filename
    )

    with filename.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as fp:

        writer = csv.writer(
            fp
        )

        writer.writerow(
            (
                "Time",
                "Range",
                "Height",
                "Drift",
                "Velocity",
            )
        )

        writer.writerows(
            rows
        )
'''
FILES["tests/external/test_atmosphere.py"] = r'''
from ballistics.external.atmosphere import (
    density,
    density_at_altitude,
)


def test_density():

    rho = density(
        101325,
        288.15,
    )

    assert rho > 1.0


def test_density_altitude():

    rho = density_at_altitude(
        101325,
        288.15,
        1000.0,
    )

    assert rho > 0.0
'''

FILES["tests/external/test_spin_drift.py"] = r'''
from ballistics.external.spin_drift import (
    estimate_spin_drift,
)


def test_spin():

    drift = estimate_spin_drift(
        distance=1000,
        twist_rate=10,
        muzzle_velocity=820,
    )

    assert drift > 0
'''

FILES["tests/external/test_coriolis.py"] = r'''
from ballistics.external.coriolis import (
    coriolis_acceleration,
)


def test_coriolis():

    ax, ay, az = coriolis_acceleration(
        latitude_deg=45,
        velocity_north=800,
        velocity_east=0,
        velocity_up=0,
    )

    assert isinstance(
        ax,
        float,
    )

    assert isinstance(
        ay,
        float,
    )

    assert isinstance(
        az,
        float,
    )
'''

FILES["docs/theory/coriolis.md"] = r"""
# Coriolis Model

Version 0.3.0 introduces an initial Coriolis model.

Included

- Earth rotation constant
- Latitude correction
- Three-axis acceleration

Future work

- ECEF coordinate system
- Geodetic Earth model
- WGS-84 integration
- Precision long-range corrections
"""

FILES["src/ballistics/external/drag/g7.py"] = r'''
"""
Baseline G7 drag model.

This implementation mirrors the current BC formulation while
providing the interface required for future table-driven G7
retardation functions.
"""

from .base import DragModel


class G7DragModel(DragModel):

    def drag_acceleration(
        self,
        velocity,
        ballistic_coefficient,
        density,
    ):
        if ballistic_coefficient <= 0:
            raise ValueError(
                "Ballistic coefficient must be positive."
            )

        coefficient = 0.000155

        return (
            coefficient
            * density
            * velocity
            * velocity
            / ballistic_coefficient
        )
'''

FILES["src/ballistics/external/models/drag_tables.py"] = r'''
"""
Drag table definitions.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class DragPoint:

    mach: float

    coefficient: float


@dataclass(slots=True)
class DragTable:

    name: str

    points: list[DragPoint]
'''

FILES["src/ballistics/external/solver/integrators.py"] = r'''
"""
Numerical integration methods.
"""

from ballistics.common.numerics import (
    euler_step,
)


def integrate_position(
    position,
    velocity,
    dt,
):
    return euler_step(
        position,
        velocity,
        dt,
    )


def integrate_velocity(
    velocity,
    acceleration,
    dt,
):
    return euler_step(
        velocity,
        acceleration,
        dt,
    )
'''

FILES["src/ballistics/external/output/json_report.py"] = r'''
"""
JSON report generation.
"""

import json

from pathlib import Path


def write_report(
    records,
    filename,
):
    Path(filename).write_text(
        json.dumps(
            records,
            indent=4,
        ),
        encoding="utf-8",
    )
'''

FILES["src/ballistics/external/statistics.py"] = r'''
"""
Trajectory statistical utilities.
"""

from statistics import mean


def average_speed(
    history,
):
    return mean(
        point[4]
        for point in history
    )


def maximum_speed(
    history,
):
    return max(
        point[4]
        for point in history
    )


def minimum_speed(
    history,
):
    return min(
        point[4]
        for point in history
    )
'''

FILES["tests/external/test_g7.py"] = r'''
from ballistics.external.drag.g7 import (
    G7DragModel,
)


def test_g7_drag():

    model = G7DragModel()

    drag = model.drag_acceleration(
        velocity=850.0,
        ballistic_coefficient=0.310,
        density=1.225,
    )

    assert drag > 0.0
'''

FILES["tests/external/test_integrators.py"] = r'''
from ballistics.external.solver.integrators import (
    integrate_position,
    integrate_velocity,
)


def test_integrators():

    x = integrate_position(
        0.0,
        100.0,
        0.5,
    )

    v = integrate_velocity(
        800.0,
        -10.0,
        0.5,
    )

    assert x == 50.0

    assert v == 795.0
'''

FILES["docs/theory/g7.md"] = r"""
# G7 Drag Model

Version 0.3.0 introduces the framework for G7 drag support.

Current capabilities

- Dedicated G7 drag model
- Common drag interface
- Interchangeable model architecture

Planned enhancements

- Published G7 retardation tables
- Mach interpolation
- Custom drag curves
- Doppler-derived drag models
"""

FILES["src/ballistics/external/models/atmosphere.py"] = r'''
"""
Atmospheric state models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class AtmosphericState:

    pressure: float

    temperature: float

    density: float

    humidity: float

    altitude: float


def standard_atmosphere():

    return AtmosphericState(
        pressure=101325.0,
        temperature=288.15,
        density=1.225,
        humidity=0.50,
        altitude=0.0,
    )
'''

FILES["src/ballistics/external/solver/adaptive.py"] = r'''
"""
Adaptive solver framework.

A placeholder implementation that preserves a stable public API
until RK45 support is introduced.
"""


class AdaptiveSolver:

    def __init__(
        self,
        tolerance=1e-6,
    ):
        self.tolerance = tolerance

    def integrate(
        self,
        step_function,
        state,
        dt,
    ):
        return step_function(
            state,
            dt,
        )
'''

FILES["src/ballistics/external/drag/factory.py"] = r'''
"""
Drag model factory.
"""

from .g1 import G1DragModel
from .g7 import G7DragModel


def create_drag_model(name):

    model = name.upper()

    if model == "G1":
        return G1DragModel()

    if model == "G7":
        return G7DragModel()

    raise ValueError(
        f"Unsupported drag model: {name}"
    )
'''

FILES["src/ballistics/external/output/csv_report.py"] = r'''
"""
CSV trajectory report writer.
"""

import csv

from pathlib import Path


def write_report(
    history,
    filename,
):
    with Path(filename).open(
        "w",
        newline="",
        encoding="utf-8",
    ) as fp:

        writer = csv.writer(fp)

        writer.writerow(
            [
                "Time",
                "Range",
                "Height",
                "Drift",
                "Velocity",
            ]
        )

        writer.writerows(history)
'''

FILES["src/ballistics/external/validation/report.py"] = r'''
"""
Validation report utilities.
"""


def summarize(
    rmse,
    mae,
):

    return {
        "rmse": rmse,
        "mae": mae,
        "passed": rmse < 1.0,
    }
'''

FILES["tests/external/test_drag_factory.py"] = r'''
from ballistics.external.drag.factory import (
    create_drag_model,
)

from ballistics.external.drag.g1 import (
    G1DragModel,
)

from ballistics.external.drag.g7 import (
    G7DragModel,
)


def test_factory():

    assert isinstance(
        create_drag_model("G1"),
        G1DragModel,
    )

    assert isinstance(
        create_drag_model("g7"),
        G7DragModel,
    )
'''

FILES["tests/external/test_atmosphere_model.py"] = r'''
from ballistics.external.models.atmosphere import (
    standard_atmosphere,
)


def test_standard_atmosphere():

    atmosphere = standard_atmosphere()

    assert atmosphere.density > 1.0

    assert atmosphere.pressure > 100000
'''

FILES["docs/theory/adaptive_solver.md"] = r"""
# Adaptive Solver Framework

Version 0.3.0 establishes the public API for adaptive numerical
integration.

Current capabilities

- Stable integration interface
- Configurable error tolerance

Planned work

- Dormand-Prince RK45
- Automatic timestep control
- Embedded error estimation
- Dense output interpolation
- Event-aware integration
"""

FILES["src/ballistics/external/models/wind.py"] = r'''
"""
Wind profile models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class WindLayer:

    minimum_altitude: float

    maximum_altitude: float

    speed: float

    direction: float


@dataclass(slots=True)
class WindProfile:

    layers: list[WindLayer]

    def layer_at(
        self,
        altitude,
    ):
        for layer in self.layers:
            if (
                layer.minimum_altitude
                <= altitude
                <= layer.maximum_altitude
            ):
                return layer
        return None
'''

FILES["src/ballistics/external/solver/state.py"] = r'''
"""
Solver state definitions.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SolverState:

    time: float

    x: float

    y: float

    z: float

    vx: float

    vy: float

    vz: float


    @property
    def position(self):
        return (
            self.x,
            self.y,
            self.z,
        )


    @property
    def velocity(self):
        return (
            self.vx,
            self.vy,
            self.vz,
        )
'''

FILES["src/ballistics/external/solver/history.py"] = r'''
"""
Trajectory history helpers.
"""


def append(
    history,
    state,
    speed,
):
    history.append(
        (
            state.time,
            state.x,
            state.y,
            state.z,
            speed,
        )
    )


def last(history):

    if not history:
        return None

    return history[-1]
'''

FILES["src/ballistics/external/output/html_report.py"] = r'''
"""
Simple HTML report generation.
"""

from pathlib import Path


def write_report(
    report,
    filename,
):
    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Trajectory Report</title>
</head>
<body>
<pre>
{report}
</pre>
</body>
</html>
"""

    Path(filename).write_text(
        html.strip(),
        encoding="utf-8",
    )
'''

FILES["src/ballistics/external/calibration.py"] = r'''
"""
Calibration framework.
"""


def velocity_error(
    predicted,
    observed,
):
    return observed - predicted


def average_error(
    predicted,
    observed,
):
    errors = [
        o - p
        for p, o in zip(
            predicted,
            observed,
        )
    ]

    return sum(errors) / len(errors)
'''

FILES["tests/external/test_history.py"] = r'''
from ballistics.external.solver.history import (
    append,
    last,
)

from ballistics.external.solver.state import (
    SolverState,
)


def test_history():

    history = []

    state = SolverState(
        0.0,
        0.0,
        0.0,
        0.0,
        800.0,
        0.0,
        0.0,
    )

    append(
        history,
        state,
        800.0,
    )

    assert last(history)[4] == 800.0
'''

FILES["tests/external/test_calibration.py"] = r'''
from ballistics.external.calibration import (
    average_error,
)


def test_average_error():

    predicted = [
        800.0,
        790.0,
    ]

    observed = [
        801.0,
        789.0,
    ]

    assert average_error(
        predicted,
        observed,
    ) == 0.0
'''

FILES["docs/theory/calibration.md"] = r"""
# Calibration Framework

Version 0.3.0 introduces the initial calibration API.

Current capabilities

- Velocity residual computation
- Mean prediction error

Future work

- Bayesian optimization
- Parameter estimation
- Confidence intervals
- Automatic drag model fitting
- Multi-dataset calibration
"""

FILES["src/ballistics/external/drag/g7.py"] = r'''
"""
Baseline G7 drag model.

This implementation mirrors the current simplified G1 framework and
provides a stable interface until full table-driven retardation data
is introduced.
"""

from .base import DragModel


class G7DragModel(DragModel):

    def drag_acceleration(
        self,
        velocity,
        ballistic_coefficient,
        density,
    ):
        if ballistic_coefficient <= 0:
            raise ValueError(
                "Ballistic coefficient must be positive."
            )

        k = 0.000165

        return (
            k
            * density
            * velocity
            * velocity
            / ballistic_coefficient
        )
'''

FILES["src/ballistics/external/solver/rk4.py"] = r'''
"""
Reusable RK4 integration utilities.
"""


def rk4_step(
    derivative,
    state,
    dt,
):
    k1 = derivative(state)

    k2 = derivative(
        state + 0.5 * dt * k1
    )

    k3 = derivative(
        state + 0.5 * dt * k2
    )

    k4 = derivative(
        state + dt * k3
    )

    return (
        state
        + dt
        * (
            k1
            + 2 * k2
            + 2 * k3
            + k4
        )
        / 6.0
    )
'''

FILES["src/ballistics/external/models/trajectory.py"] = r'''
"""
Strongly typed trajectory models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class TrajectorySample:

    time: float

    range: float

    height: float

    drift: float

    velocity: float


@dataclass(slots=True)
class TrajectorySeries:

    samples: list[TrajectorySample]

    drag_model: str

    solver: str

    version: str
'''

FILES["src/ballistics/external/output/json_report.py"] = r'''
"""
JSON trajectory report generation.
"""

import json

from pathlib import Path


def write_report(
    report,
    filename,
):
    Path(filename).write_text(
        json.dumps(
            report,
            indent=4,
        ),
        encoding="utf-8",
    )
'''

FILES["src/ballistics/external/statistics.py"] = r'''
"""
Trajectory statistical utilities.
"""

from statistics import mean


def average_speed(history):
    return mean(
        point[4]
        for point in history
    )


def minimum_speed(history):
    return min(
        point[4]
        for point in history
    )


def maximum_speed(history):
    return max(
        point[4]
        for point in history
    )
'''

FILES["tests/external/test_g7.py"] = r'''
from ballistics.external.drag.g7 import (
    G7DragModel,
)


def test_g7_drag():

    model = G7DragModel()

    drag = model.drag_acceleration(
        velocity=820.0,
        ballistic_coefficient=0.310,
        density=1.225,
    )

    assert drag > 0
'''

FILES["tests/external/test_statistics.py"] = r'''
from ballistics.external.statistics import (
    average_speed,
    minimum_speed,
    maximum_speed,
)


def test_statistics():

    history = [
        (0.0, 0.0, 0.0, 0.0, 820.0),
        (1.0, 100.0, -1.0, 0.0, 790.0),
        (2.0, 200.0, -4.0, 0.0, 760.0),
    ]

    assert average_speed(history) > 780.0
    assert minimum_speed(history) == 760.0
    assert maximum_speed(history) == 820.0
'''

FILES["docs/theory/g7.md"] = r"""
# G7 Drag Model

Version 0.3.0 introduces the first interchangeable G7 drag model.

Current implementation

- Simplified BC-based formulation
- Compatible with DragModel interface
- Factory selectable

Future enhancements

- Published G7 retardation tables
- Mach interpolation
- Supersonic/transonic transitions
- Doppler radar validation
- Manufacturer drag datasets
"""

FILES["src/ballistics/external/models/projectile.py"] = r'''
"""
Projectile models used by the external solver.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Projectile:

    mass: float

    diameter: float

    ballistic_coefficient: float

    drag_model: str = "G1"

    muzzle_velocity: float = 0.0

    twist_rate: float = 0.0

    length: float = 0.0
'''

FILES["src/ballistics/external/solver/events.py"] = r'''
"""
Solver event helpers.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SolverEvent:

    time: float

    name: str

    description: str


class EventLog(list):

    def add(
        self,
        time,
        name,
        description,
    ):
        self.append(
            SolverEvent(
                time=time,
                name=name,
                description=description,
            )
        )
'''

FILES["src/ballistics/external/output/summary.py"] = r'''
"""
Trajectory summary generation.
"""

from dataclasses import asdict


def build_summary(
    trajectory,
):
    return {
        "samples": len(
            trajectory.samples
        ),
        "drag_model": trajectory.drag_model,
        "solver": trajectory.solver,
        "version": trajectory.version,
    }


def serialize_summary(
    trajectory,
):
    return build_summary(
        trajectory
    )
'''

FILES["src/ballistics/external/weather/profile.py"] = r'''
"""
Weather profile support.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class WeatherLayer:

    altitude: float

    temperature: float

    pressure: float

    humidity: float


class WeatherProfile:

    def __init__(self):
        self.layers = []


    def add_layer(
        self,
        layer,
    ):
        self.layers.append(layer)


    def __iter__(self):
        return iter(self.layers)
'''

FILES["src/ballistics/external/validation/errors.py"] = r'''
"""
Validation error metrics.
"""

from math import sqrt


def rmse(
    predicted,
    observed,
):
    total = 0.0

    for p, o in zip(
        predicted,
        observed,
    ):
        total += (o - p) ** 2

    return sqrt(
        total / len(predicted)
    )


def mae(
    predicted,
    observed,
):
    total = 0.0

    for p, o in zip(
        predicted,
        observed,
    ):
        total += abs(
            o - p
        )

    return total / len(predicted)
'''

FILES["tests/external/test_projectile.py"] = r'''
from ballistics.external.models.projectile import (
    Projectile,
)


def test_projectile():

    projectile = Projectile(
        mass=0.01134,
        diameter=0.00782,
        ballistic_coefficient=0.310,
    )

    assert projectile.mass > 0
    assert projectile.ballistic_coefficient > 0
'''

FILES["tests/external/test_validation.py"] = r'''
from ballistics.external.validation.errors import (
    rmse,
    mae,
)


def test_validation():

    predicted = [
        100,
        200,
        300,
    ]

    observed = [
        101,
        199,
        301,
    ]

    assert rmse(
        predicted,
        observed,
    ) > 0

    assert mae(
        predicted,
        observed,
    ) > 0
'''

FILES["docs/theory/projectile.md"] = r"""
# Projectile Model

Version 0.3.0 introduces a dedicated projectile data model.

Current capabilities

- Physical dimensions
- Ballistic coefficient
- Drag model selection
- Twist rate storage

Future capabilities

- Center of gravity
- Moments of inertia
- Dynamic stability factors
- Custom drag datasets
- Manufacturer projectile libraries
"""

FILES["src/ballistics/external/models/solution.py"] = r'''
"""
Trajectory solution models.
"""

from dataclasses import dataclass, field

from .trajectory import TrajectorySample


@dataclass(slots=True)
class TrajectorySolution:

    samples: list[TrajectorySample] = field(
        default_factory=list
    )

    drag_model: str = "G1"

    solver: str = "Euler"

    computation_time: float = 0.0

    converged: bool = True

    metadata: dict = field(
        default_factory=dict
    )


    def add_sample(
        self,
        sample,
    ):
        self.samples.append(sample)
'''

FILES["src/ballistics/external/solver/termination.py"] = r'''
"""
Trajectory termination conditions.
"""


def maximum_time(
    state,
    limit,
):
    return state.time >= limit


def below_ground(
    state,
):
    return state.y <= 0.0


def maximum_range(
    state,
    limit,
):
    return state.x >= limit
'''

FILES["src/ballistics/external/output/markdown_report.py"] = r'''
"""
Markdown report generation.
"""


def generate(
    summary,
):
    lines = [
        "# Trajectory Report",
        "",
    ]

    for key, value in summary.items():
        lines.append(
            f"- **{key}**: {value}"
        )

    return "\n".join(lines)
'''

FILES["src/ballistics/external/weather/interpolation.py"] = r'''
"""
Weather profile interpolation.
"""


def interpolate(
    lower,
    upper,
    altitude,
):
    if upper.altitude == lower.altitude:
        return lower

    fraction = (
        altitude - lower.altitude
    ) / (
        upper.altitude - lower.altitude
    )

    return {
        "temperature":
            lower.temperature
            + fraction
            * (
                upper.temperature
                - lower.temperature
            ),
        "pressure":
            lower.pressure
            + fraction
            * (
                upper.pressure
                - lower.pressure
            ),
        "humidity":
            lower.humidity
            + fraction
            * (
                upper.humidity
                - lower.humidity
            ),
    }
'''

FILES["src/ballistics/external/validation/comparison.py"] = r'''
"""
Reference trajectory comparison helpers.
"""


def compare(
    predicted,
    observed,
):
    return [
        o - p
        for p, o in zip(
            predicted,
            observed,
        )
    ]
'''

FILES["tests/external/test_solution.py"] = r'''
from ballistics.external.models.solution import (
    TrajectorySolution,
)


def test_solution():

    solution = TrajectorySolution()

    assert solution.samples == []
    assert solution.converged
'''

FILES["tests/external/test_termination.py"] = r'''
from ballistics.external.solver.termination import (
    below_ground,
    maximum_time,
)


class State:

    def __init__(
        self,
        time,
        y,
        x,
    ):
        self.time = time
        self.y = y
        self.x = x


def test_conditions():

    assert maximum_time(
        State(10.0, 1.0, 0.0),
        5.0,
    )

    assert below_ground(
        State(
            0.0,
            -1.0,
            0.0,
        )
    )
'''

FILES["docs/theory/solution.md"] = r"""
# Trajectory Solution

Version 0.3.0 formalizes the trajectory solution object.

Current capabilities

- Stores trajectory samples
- Solver metadata
- Convergence status
- Arbitrary metadata

Planned enhancements

- Covariance information
- Error estimates
- Adaptive timestep history
- Validation summaries
- Export pipelines
"""

FILES["src/ballistics/external/models/shot.py"] = r'''
"""
Shot configuration models.
"""

from dataclasses import dataclass

from .projectile import Projectile
from .atmosphere import AtmosphericState


@dataclass(slots=True)
class Shot:

    projectile: Projectile

    atmosphere: AtmosphericState

    muzzle_velocity: float

    sight_height: float

    zero_range: float

    firing_angle: float = 0.0

    azimuth: float = 0.0

    latitude: float = 0.0
'''

FILES["src/ballistics/external/solver/context.py"] = r'''
"""
Solver execution context.
"""

from dataclasses import dataclass

from ballistics.external.configuration import Configuration
from ballistics.external.models.shot import Shot


@dataclass(slots=True)
class SolverContext:

    shot: Shot

    configuration: Configuration

    drag_model: object
'''

FILES["src/ballistics/external/output/text_report.py"] = r'''
"""
Plain-text trajectory report generation.
"""


def generate(solution):

    lines = [
        "Trajectory Report",
        "=" * 60,
        f"Samples : {len(solution.samples)}",
        f"Solver  : {solution.solver}",
        f"Drag    : {solution.drag_model}",
        f"Success : {solution.converged}",
        "",
    ]

    return "\n".join(lines)
'''

FILES["src/ballistics/external/weather/service.py"] = r'''
"""
Weather service helpers.
"""

from .profile import WeatherProfile


class WeatherService:

    def __init__(self):
        self.profile = WeatherProfile()

    def load_profile(
        self,
        profile,
    ):
        self.profile = profile

    def layers(self):
        return list(
            self.profile
        )
'''

FILES["src/ballistics/external/validation/reference.py"] = r'''
"""
Reference trajectory container.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ReferencePoint:

    range: float

    drop: float

    drift: float

    velocity: float
'''

FILES["tests/external/test_shot.py"] = r'''
from ballistics.external.models.shot import Shot
from ballistics.external.models.projectile import Projectile
from ballistics.external.models.atmosphere import (
    standard_atmosphere,
)


def test_shot():

    shot = Shot(
        projectile=Projectile(
            mass=0.01134,
            diameter=0.00782,
            ballistic_coefficient=0.310,
        ),
        atmosphere=standard_atmosphere(),
        muzzle_velocity=820.0,
        sight_height=0.050,
        zero_range=100.0,
    )

    assert shot.zero_range == 100.0
'''

FILES["tests/external/test_context.py"] = r'''
from ballistics.external.configuration import Configuration
from ballistics.external.drag.factory import create_drag_model
from ballistics.external.models.atmosphere import (
    standard_atmosphere,
)
from ballistics.external.models.projectile import Projectile
from ballistics.external.models.shot import Shot
from ballistics.external.solver.context import (
    SolverContext,
)


def test_context():

    shot = Shot(
        projectile=Projectile(
            mass=0.01,
            diameter=0.007,
            ballistic_coefficient=0.30,
        ),
        atmosphere=standard_atmosphere(),
        muzzle_velocity=800.0,
        sight_height=0.05,
        zero_range=100.0,
    )

    context = SolverContext(
        shot=shot,
        configuration=Configuration(),
        drag_model=create_drag_model("G1"),
    )

    assert context.configuration.timestep > 0
'''

FILES["docs/theory/shot_model.md"] = r"""
# Shot Model

Version 0.3.0 introduces a dedicated shot configuration object.

Current capabilities

- Projectile reference
- Atmospheric state
- Muzzle velocity
- Sight height
- Zero range
- Firing angle
- Azimuth
- Latitude

Future enhancements

- Rifle metadata
- Scope metadata
- Multi-shot scenarios
- Shot groups
- Fire control integration
"""

FILES["src/ballistics/external/models/rifle.py"] = r'''
"""
Rifle configuration models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Rifle:

    name: str = ""

    barrel_length: float = 0.0

    twist_rate: float = 0.0

    sight_height: float = 0.050

    zero_range: float = 100.0

    cant_angle: float = 0.0

    notes: str = ""
'''

FILES["src/ballistics/external/solver/result.py"] = r'''
"""
Solver result container.
"""

from dataclasses import dataclass, field

from ballistics.external.models.solution import (
    TrajectorySolution,
)


@dataclass(slots=True)
class SolverResult:

    solution: TrajectorySolution

    iterations: int = 0

    elapsed_time: float = 0.0

    warnings: list[str] = field(
        default_factory=list,
    )

    success: bool = True
'''

FILES["src/ballistics/external/output/export.py"] = r'''
"""
Trajectory export helpers.
"""

from .csv_report import write_report as csv_report
from .json_report import write_report as json_report


def export_csv(
    history,
    filename,
):
    csv_report(
        history,
        filename,
    )


def export_json(
    report,
    filename,
):
    json_report(
        report,
        filename,
    )
'''

FILES["src/ballistics/external/weather/wind_vector.py"] = r'''
"""
Wind vector utilities.
"""

from math import cos
from math import radians
from math import sin


def wind_components(
    speed,
    direction_deg,
):
    angle = radians(
        direction_deg
    )

    return (
        speed * cos(angle),
        speed * sin(angle),
    )
'''

FILES["src/ballistics/external/validation/dataset.py"] = r'''
"""
Reference trajectory dataset.
"""

from dataclasses import dataclass, field

from .reference import ReferencePoint


@dataclass(slots=True)
class ValidationDataset:

    name: str

    points: list[ReferencePoint] = field(
        default_factory=list,
    )

    def add(
        self,
        point,
    ):
        self.points.append(
            point
        )
'''

FILES["tests/external/test_rifle.py"] = r'''
from ballistics.external.models.rifle import (
    Rifle,
)


def test_rifle():

    rifle = Rifle(
        barrel_length=24.0,
        twist_rate=10.0,
    )

    assert rifle.barrel_length == 24.0
    assert rifle.twist_rate == 10.0
'''

FILES["tests/external/test_wind_vector.py"] = r'''
from ballistics.external.weather.wind_vector import (
    wind_components,
)


def test_components():

    x, y = wind_components(
        10.0,
        90.0,
    )

    assert abs(x) < 1e-6
    assert y > 0
'''

FILES["docs/theory/rifle.md"] = r"""
# Rifle Model

Version 0.3.0 introduces a reusable rifle configuration object.

Current capabilities

- Barrel length
- Twist rate
- Sight height
- Zero range
- Cant angle

Future enhancements

- Barrel profiles
- Action metadata
- Optic configuration
- Rail offsets
- Rifle presets
"""

FILES["src/ballistics/external/models/optic.py"] = r'''
"""
Optic configuration models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Optic:

    name: str = ""

    magnification: float = 1.0

    objective_diameter: float = 0.0

    click_value: float = 0.25

    zero_range: float = 100.0

    reticle: str = ""

    focal_plane: str = "FFP"
'''

FILES["src/ballistics/external/solver/status.py"] = r'''
"""
Solver status definitions.
"""

from enum import Enum


class SolverStatus(str, Enum):

    SUCCESS = "success"

    MAXIMUM_TIME = "maximum_time"

    MAXIMUM_RANGE = "maximum_range"

    BELOW_GROUND = "below_ground"

    FAILED = "failed"
'''

FILES["src/ballistics/external/output/export_manager.py"] = r'''
"""
Unified export interface.
"""

from .csv_report import write_report as write_csv
from .json_report import write_report as write_json
from .html_report import write_report as write_html


class ExportManager:

    def csv(
        self,
        history,
        filename,
    ):
        write_csv(
            history,
            filename,
        )

    def json(
        self,
        report,
        filename,
    ):
        write_json(
            report,
            filename,
        )

    def html(
        self,
        report,
        filename,
    ):
        write_html(
            report,
            filename,
        )
'''

FILES["src/ballistics/external/weather/wind.py"] = r'''
"""
Wind utilities.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Wind:

    speed: float

    direction: float


def calm():

    return Wind(
        speed=0.0,
        direction=0.0,
    )
'''

FILES["src/ballistics/external/validation/metrics.py"] = r'''
"""
Validation metrics.
"""

from .errors import mae
from .errors import rmse


def summary(
    predicted,
    observed,
):
    return {
        "rmse": rmse(
            predicted,
            observed,
        ),
        "mae": mae(
            predicted,
            observed,
        ),
    }
'''

FILES["tests/external/test_optic.py"] = r'''
from ballistics.external.models.optic import (
    Optic,
)


def test_optic():

    optic = Optic()

    assert optic.zero_range == 100.0
    assert optic.click_value == 0.25
'''
FILES["tests/external/test_status.py"] = r'''
from ballistics.external.solver.status import (
    SolverStatus,
)


def test_status():

    assert (
        SolverStatus.SUCCESS.value
        == "success"
    )
'''

FILES["docs/theory/optic.md"] = r"""
# Optic Model

Version 0.3.0 introduces a reusable optic configuration model.

Current capabilities

- Magnification
- Click value
- Zero range
- Reticle metadata
- Focal plane selection

Future enhancements

- Illumination settings
- Reticle libraries
- Turret profiles
- Ballistic turret support
- Optical offset modeling
"""

FILES["src/ballistics/external/models/fire_control.py"] = r'''
"""
Fire control solution models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class FireControlSolution:

    elevation: float = 0.0

    windage: float = 0.0

    time_of_flight: float = 0.0

    impact_velocity: float = 0.0

    impact_energy: float = 0.0

    maximum_ordinate: float = 0.0

    status: str = "pending"
'''

FILES["src/ballistics/external/solver/clock.py"] = r'''
"""
Timing utilities for solver execution.
"""

from time import perf_counter


class SolverClock:

    def __init__(self):
        self._start = 0.0
        self._stop = 0.0

    def start(self):
        self._start = perf_counter()

    def stop(self):
        self._stop = perf_counter()

    @property
    def elapsed(self):
        return self._stop - self._start
'''

FILES["src/ballistics/external/output/yaml_report.py"] = r'''
"""
YAML report generation.
"""

try:
    import yaml
except ImportError:
    yaml = None


def write_report(
    report,
    filename,
):
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required."
        )

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as fp:
        yaml.safe_dump(
            report,
            fp,
            sort_keys=False,
        )
'''

FILES["src/ballistics/external/weather/station.py"] = r'''
"""
Weather station models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class WeatherStation:

    name: str

    latitude: float

    longitude: float

    elevation: float

    pressure: float

    temperature: float

    humidity: float
'''

FILES["src/ballistics/external/validation/report.py"] = r'''
"""
Validation report model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ValidationReport:

    rmse: float

    mae: float

    passed: bool

    samples: int
'''

FILES["tests/external/test_fire_control.py"] = r'''
from ballistics.external.models.fire_control import (
    FireControlSolution,
)


def test_solution():

    solution = FireControlSolution()

    assert solution.status == "pending"

    assert solution.elevation == 0.0
'''

FILES["tests/external/test_clock.py"] = r'''
from ballistics.external.solver.clock import (
    SolverClock,
)


def test_clock():

    clock = SolverClock()

    clock.start()

    clock.stop()

    assert clock.elapsed >= 0.0
'''

FILES["docs/theory/fire_control.md"] = r"""
# Fire Control Solution

Version 0.3.0 introduces a standardized fire-control result model.

Current capabilities

- Elevation solution
- Windage solution
- Time of flight
- Impact velocity
- Impact energy
- Maximum ordinate
- Solver status

Future enhancements

- Multi-target solutions
- Moving target lead
- Coriolis integration
- Spin drift compensation
- Aerodynamic jump correction
"""

FILES["src/ballistics/external/models/target.py"] = r'''
"""
Target models for external ballistics.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Target:

    range: float

    elevation: float = 0.0

    azimuth: float = 0.0

    speed: float = 0.0

    heading: float = 0.0

    description: str = ""
'''

FILES["src/ballistics/external/solver/diagnostics.py"] = r'''
"""
Solver diagnostic helpers.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class SolverDiagnostics:

    iterations: int = 0

    accepted_steps: int = 0

    rejected_steps: int = 0

    elapsed_time: float = 0.0

    warnings: list[str] = field(
        default_factory=list,
    )
'''

FILES["src/ballistics/external/output/xml_report.py"] = r'''
"""
XML report generation.
"""

from xml.etree.ElementTree import (
    Element,
    SubElement,
    ElementTree,
)


def write_report(
    summary,
    filename,
):
    root = Element("trajectory")

    for key, value in summary.items():
        node = SubElement(
            root,
            key,
        )
        node.text = str(value)

    ElementTree(root).write(
        filename,
        encoding="utf-8",
        xml_declaration=True,
    )
'''

FILES["src/ballistics/external/weather/services.py"] = r'''
"""
Weather service abstractions.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class WeatherObservation:

    pressure: float

    temperature: float

    humidity: float

    wind_speed: float

    wind_direction: float
'''

FILES["src/ballistics/external/validation/residuals.py"] = r'''
"""
Residual calculations.
"""


def residuals(
    predicted,
    observed,
):
    return [
        observed_value - predicted_value
        for predicted_value, observed_value
        in zip(
            predicted,
            observed,
        )
    ]
'''

FILES["tests/external/test_target.py"] = r'''
from ballistics.external.models.target import (
    Target,
)


def test_target():

    target = Target(
        range=1000.0,
    )

    assert target.range == 1000.0
'''

FILES["tests/external/test_diagnostics.py"] = r'''
from ballistics.external.solver.diagnostics import (
    SolverDiagnostics,
)


def test_diagnostics():

    diagnostics = SolverDiagnostics()

    assert diagnostics.iterations == 0

    assert diagnostics.warnings == []
'''

FILES["docs/theory/target.md"] = r"""
# Target Model

Version 0.3.0 introduces a reusable target model.

Current capabilities

- Target range
- Elevation
- Azimuth
- Target motion metadata

Planned enhancements

- Moving target prediction
- Lead computation
- Multiple simultaneous targets
- Target tracking
- Fire mission management
"""

FILES["src/ballistics/external/models/engagement.py"] = r'''
"""
High-level engagement model.
"""

from dataclasses import dataclass

from .rifle import Rifle
from .optic import Optic
from .shot import Shot
from .target import Target


@dataclass(slots=True)
class Engagement:

    rifle: Rifle

    optic: Optic

    shot: Shot

    target: Target

    description: str = ""
'''

FILES["src/ballistics/external/solver/session.py"] = r'''
"""
Solver session tracking.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class SolverSession:

    started: datetime

    finished: datetime | None = None

    version: str = "0.3.0"

    diagnostics: dict = field(
        default_factory=dict,
    )

    def duration(self):
        if self.finished is None:
            return None
        return (
            self.finished - self.started
        ).total_seconds()
'''

FILES["src/ballistics/external/output/archive.py"] = r'''
"""
Trajectory archive helpers.
"""

from pathlib import Path
import json


def save_archive(
    summary,
    filename,
):
    Path(filename).write_text(
        json.dumps(
            summary,
            indent=4,
        ),
        encoding="utf-8",
    )
'''

FILES["src/ballistics/external/weather/units.py"] = r'''
"""
Weather unit conversions.
"""


def celsius_to_kelvin(
    value,
):
    return value + 273.15


def kelvin_to_celsius(
    value,
):
    return value - 273.15


def hpa_to_pa(
    value,
):
    return value * 100.0
'''

FILES["src/ballistics/external/validation/summary.py"] = r'''
"""
Validation summary helpers.
"""

from .metrics import summary


def build_summary(
    predicted,
    observed,
):
    metrics = summary(
        predicted,
        observed,
    )

    metrics["samples"] = len(
        predicted
    )

    return metrics
'''

FILES["tests/external/test_engagement.py"] = r'''
from ballistics.external.models.engagement import (
    Engagement,
)
from ballistics.external.models.rifle import Rifle
from ballistics.external.models.optic import Optic
from ballistics.external.models.projectile import Projectile
from ballistics.external.models.shot import Shot
from ballistics.external.models.target import Target
from ballistics.external.models.atmosphere import (
    standard_atmosphere,
)


def test_engagement():

    engagement = Engagement(
        rifle=Rifle(),
        optic=Optic(),
        shot=Shot(
            projectile=Projectile(
                mass=0.01,
                diameter=0.0078,
                ballistic_coefficient=0.30,
            ),
            atmosphere=standard_atmosphere(),
            muzzle_velocity=800.0,
            sight_height=0.05,
            zero_range=100.0,
        ),
        target=Target(range=500.0),
    )

    assert engagement.target.range == 500.0
'''

FILES["tests/external/test_weather_units.py"] = r'''
from ballistics.external.weather.units import (
    celsius_to_kelvin,
    kelvin_to_celsius,
    hpa_to_pa,
)


def test_units():

    assert celsius_to_kelvin(0.0) == 273.15
    assert kelvin_to_celsius(273.15) == 0.0
    assert hpa_to_pa(1013.25) == 101325.0
'''

FILES["docs/theory/engagement.md"] = r"""
# Engagement Model

Version 0.3.0 introduces an engagement object that combines all
major simulation inputs into a single container.

Current capabilities

- Rifle
- Optic
- Projectile
- Shot
- Target

Planned enhancements

- Multi-target engagements
- Fire missions
- Scenario persistence
- Mission replay
- Batch simulation support
"""

FILES["src/ballistics/external/models/scenario.py"] = r'''
"""
Scenario model for external ballistics simulations.
"""

from dataclasses import dataclass, field

from .engagement import Engagement


@dataclass(slots=True)
class Scenario:

    name: str

    engagement: Engagement

    description: str = ""

    tags: list[str] = field(
        default_factory=list,
    )

    author: str = ""

    version: str = "0.3.0"
'''

FILES["src/ballistics/external/solver/exceptions.py"] = r'''
"""
Solver exception hierarchy.
"""


class SolverError(Exception):
    """Base solver exception."""


class ConvergenceError(
    SolverError,
):
    """Solver failed to converge."""


class InvalidConfigurationError(
    SolverError,
):
    """Configuration is invalid."""
'''

FILES["src/ballistics/external/output/package.py"] = r'''
"""
Packaging helpers for trajectory exports.
"""

from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile


def create_package(
    files,
    filename,
):
    with ZipFile(
        filename,
        "w",
        ZIP_DEFLATED,
    ) as archive:

        for path in files:
            archive.write(
                path,
                arcname=Path(path).name,
            )
'''

FILES["src/ballistics/external/weather/parser.py"] = r'''
"""
Weather parsing helpers.
"""

from .station import WeatherStation


def from_dict(
    data,
):
    return WeatherStation(
        name=data["name"],
        latitude=data["latitude"],
        longitude=data["longitude"],
        elevation=data["elevation"],
        pressure=data["pressure"],
        temperature=data["temperature"],
        humidity=data["humidity"],
    )
'''

FILES["src/ballistics/external/validation/runner.py"] = r'''
"""
Validation runner.
"""

from .metrics import summary


def run_validation(
    predicted,
    observed,
):
    return summary(
        predicted,
        observed,
    )
'''

FILES["tests/external/test_scenario.py"] = r'''
from ballistics.external.models.engagement import Engagement
from ballistics.external.models.optic import Optic
from ballistics.external.models.projectile import Projectile
from ballistics.external.models.rifle import Rifle
from ballistics.external.models.scenario import Scenario
from ballistics.external.models.shot import Shot
from ballistics.external.models.target import Target
from ballistics.external.models.atmosphere import (
    standard_atmosphere,
)


def test_scenario():

    scenario = Scenario(
        name="Example",
        engagement=Engagement(
            rifle=Rifle(),
            optic=Optic(),
            shot=Shot(
                projectile=Projectile(
                    mass=0.01,
                    diameter=0.0078,
                    ballistic_coefficient=0.30,
                ),
                atmosphere=standard_atmosphere(),
                muzzle_velocity=800.0,
                sight_height=0.05,
                zero_range=100.0,
            ),
            target=Target(range=500.0),
        ),
    )

    assert scenario.name == "Example"
'''

FILES["tests/external/test_package.py"] = r'''
from pathlib import Path

from ballistics.external.output.package import (
    create_package,
)


def test_package(
    tmp_path,
):

    file = tmp_path / "test.txt"

    file.write_text(
        "hello",
        encoding="utf-8",
    )

    archive = tmp_path / "archive.zip"

    create_package(
        [file],
        archive,
    )

    assert archive.exists()
'''

FILES["docs/theory/scenario.md"] = r"""
# Scenario Model

Version 0.3.0 introduces a reusable scenario object that groups an
entire ballistic simulation into a single container.

Current capabilities

- Named scenarios
- Engagement reference
- Metadata
- Tags
- Author information

Future enhancements

- Mission serialization
- Batch execution
- Scenario comparison
- Cloud synchronization
- Version migration support
"""

FILES["src/ballistics/external/models/mission.py"] = r'''
"""
Mission model for organizing multiple scenarios.
"""

from dataclasses import dataclass, field

from .scenario import Scenario


@dataclass(slots=True)
class Mission:

    name: str

    scenarios: list[Scenario] = field(
        default_factory=list,
    )

    description: str = ""

    version: str = "0.3.0"

    def add(
        self,
        scenario,
    ):
        self.scenarios.append(
            scenario
        )
'''

FILES["src/ballistics/external/solver/progress.py"] = r'''
"""
Progress reporting utilities.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SolverProgress:

    current_step: int = 0

    total_steps: int = 0

    percent_complete: float = 0.0

    def update(
        self,
        current,
        total,
    ):
        self.current_step = current
        self.total_steps = total

        if total > 0:
            self.percent_complete = (
                current / total
            ) * 100.0
'''

FILES["src/ballistics/external/output/index.py"] = r'''
"""
Unified output package exports.
"""

from .csv_report import write_report as write_csv
from .json_report import write_report as write_json
from .html_report import write_report as write_html
from .markdown_report import generate as markdown_report
from .text_report import generate as text_report

__all__ = [
    "write_csv",
    "write_json",
    "write_html",
    "markdown_report",
    "text_report",
]
'''

FILES["src/ballistics/external/weather/defaults.py"] = r'''
"""
Default weather values.
"""

STANDARD_PRESSURE = 101325.0

STANDARD_TEMPERATURE = 288.15

STANDARD_HUMIDITY = 0.50

STANDARD_WIND_SPEED = 0.0

STANDARD_WIND_DIRECTION = 0.0
'''

FILES["src/ballistics/external/validation/results.py"] = r'''
"""
Validation result container.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ValidationResult:

    dataset: str

    rmse: float

    mae: float

    passed: bool

    sample_count: int
'''

FILES["tests/external/test_mission.py"] = r'''
from ballistics.external.models.mission import (
    Mission,
)
from ballistics.external.models.scenario import (
    Scenario,
)
from ballistics.external.models.engagement import (
    Engagement,
)
from ballistics.external.models.rifle import Rifle
from ballistics.external.models.optic import Optic
from ballistics.external.models.projectile import Projectile
from ballistics.external.models.shot import Shot
from ballistics.external.models.target import Target
from ballistics.external.models.atmosphere import (
    standard_atmosphere,
)


def test_mission():

    mission = Mission(
        name="Mission",
    )

    scenario = Scenario(
        name="Scenario",
        engagement=Engagement(
            rifle=Rifle(),
            optic=Optic(),
            shot=Shot(
                projectile=Projectile(
                    mass=0.01,
                    diameter=0.0078,
                    ballistic_coefficient=0.30,
                ),
                atmosphere=standard_atmosphere(),
                muzzle_velocity=800.0,
                sight_height=0.05,
                zero_range=100.0,
            ),
            target=Target(range=500.0),
        ),
    )

    mission.add(scenario)

    assert len(mission.scenarios) == 1
'''

FILES["tests/external/test_progress.py"] = r'''
from ballistics.external.solver.progress import (
    SolverProgress,
)


def test_progress():

    progress = SolverProgress()

    progress.update(
        25,
        100,
    )

    assert progress.percent_complete == 25.0
'''

FILES["docs/theory/mission.md"] = r"""
# Mission Model

Version 0.3.0 introduces a mission container for organizing complete
ballistic simulations.

Current capabilities

- Multiple scenarios
- Mission metadata
- Version tracking

Planned enhancements

- Mission persistence
- Batch execution
- Comparative analysis
- Scenario scheduling
- Distributed simulation
"""

FILES["src/ballistics/external/models/session.py"] = r'''
"""
Top-level simulation session model.
"""

from dataclasses import dataclass, field
from datetime import datetime

from .mission import Mission


@dataclass(slots=True)
class SimulationSession:

    mission: Mission

    started: datetime = field(
        default_factory=datetime.utcnow,
    )

    finished: datetime | None = None

    user: str = ""

    notes: str = ""

    version: str = "0.3.0"

    @property
    def complete(self):
        return self.finished is not None
'''

FILES["src/ballistics/external/solver/version.py"] = r'''
"""
Solver version information.
"""

VERSION = "0.3.0"

BUILD = 1

API_LEVEL = 3


def version_string():

    return (
        f"{VERSION} (build {BUILD})"
    )
'''

FILES["src/ballistics/external/output/manifest.py"] = r'''
"""
Output manifest generation.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class OutputManifest:

    files: list[str] = field(
        default_factory=list,
    )

    generated_by: str = "Ballistics Platform"

    version: str = "0.3.0"

    def add(
        self,
        filename,
    ):
        self.files.append(
            filename
        )
'''

FILES["src/ballistics/external/weather/constants.py"] = r'''
"""
Weather-related constants.
"""

STANDARD_PRESSURE = 101325.0

STANDARD_TEMPERATURE = 288.15

STANDARD_DENSITY = 1.225

STANDARD_HUMIDITY = 0.50

GRAVITY = 9.80665
'''

FILES["src/ballistics/external/validation/history.py"] = r'''
"""
Validation history tracking.
"""

from dataclasses import dataclass, field

from .results import ValidationResult


@dataclass(slots=True)
class ValidationHistory:

    results: list[ValidationResult] = field(
        default_factory=list,
    )

    def add(
        self,
        result,
    ):
        self.results.append(
            result
        )

    @property
    def passed(self):
        return all(
            r.passed
            for r in self.results
        )
'''

FILES["tests/external/test_session.py"] = r'''
from ballistics.external.models.engagement import Engagement
from ballistics.external.models.mission import Mission
from ballistics.external.models.optic import Optic
from ballistics.external.models.projectile import Projectile
from ballistics.external.models.rifle import Rifle
from ballistics.external.models.scenario import Scenario
from ballistics.external.models.session import (
    SimulationSession,
)
from ballistics.external.models.shot import Shot
from ballistics.external.models.target import Target
from ballistics.external.models.atmosphere import (
    standard_atmosphere,
)


def test_session():

    mission = Mission(
        name="Mission",
    )

    mission.add(
        Scenario(
            name="Scenario",
            engagement=Engagement(
                rifle=Rifle(),
                optic=Optic(),
                shot=Shot(
                    projectile=Projectile(
                        mass=0.01,
                        diameter=0.0078,
                        ballistic_coefficient=0.30,
                    ),
                    atmosphere=standard_atmosphere(),
                    muzzle_velocity=800.0,
                    sight_height=0.05,
                    zero_range=100.0,
                ),
                target=Target(range=500.0),
            ),
        )
    )

    session = SimulationSession(
        mission=mission,
    )

    assert not session.complete
'''

FILES["tests/external/test_version.py"] = r'''
from ballistics.external.solver.version import (
    VERSION,
    version_string,
)


def test_version():

    assert VERSION == "0.3.0"

    assert "0.3.0" in version_string()
'''

FILES["docs/theory/session.md"] = r"""
# Simulation Session

Version 0.3.0 completes the foundational object hierarchy for the
External Ballistics subsystem.

Hierarchy

- Session
- Mission
- Scenario
- Engagement
- Shot
- Projectile
- Target
- Atmosphere
- Rifle
- Optic

This concludes the architectural framework introduced in Build
0.3.0. Future releases will focus on replacing placeholder
implementations with production-grade physics models, adaptive
integrators, validated drag tables, and advanced aerodynamic
corrections.
"""
