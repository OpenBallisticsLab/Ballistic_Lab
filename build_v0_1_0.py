#!/usr/bin/env python3
"""
build_v0_1_0.py

Ballistics Platform v0.1.0
Scientific Foundation Repository Generator

This generator creates the initial repository structure and writes the
scientific core files for Milestone 1.
"""

from __future__ import annotations

from pathlib import Path
import textwrap

VERSION = "0.1.0"
PROJECT_NAME = "BallisticsPlatform"


FILES = {

"pyproject.toml": """
[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "ballistics-platform"
version = "0.1.0"
description = "Research-grade modular ballistics platform"
readme = "README.md"
requires-python = ">=3.11"

authors = [
    {name = "Eric W"}
]

dependencies = [
    "numpy>=2.0",
    "scipy>=1.13",
    "pandas>=2.2",
    "matplotlib>=3.9",
    "pydantic>=2.8",
    "pint>=0.24",
    "pyyaml>=6.0",
    "rich>=13.7"
]

[project.optional-dependencies]

dev = [
    "pytest",
    "pytest-cov",
    "black",
    "ruff",
    "mypy",
    "mkdocs"
]

[tool.black]
line-length = 88

[tool.pytest.ini_options]
testpaths = ["tests"]
""",

"README.md": """
# Ballistics Platform

Version 0.1.0

Research-grade scientific framework for

- Internal Ballistics
- External Ballistics
- Terminal Ballistics
- Bayesian Calibration
- Validation
- Document AI

This repository was generated automatically.
""",

"requirements.txt": """
numpy>=2.0
scipy>=1.13
pandas>=2.2
matplotlib>=3.9
pydantic>=2.8
pint>=0.24
pyyaml>=6.0
rich>=13.7
""",

"requirements-dev.txt": """
pytest
pytest-cov
black
ruff
mypy
mkdocs
""",

"LICENSE": """
Copyright (c) 2026

All Rights Reserved.
""",

"CHANGELOG.md": """
# Changelog

## v0.1.0

Initial Scientific Foundation
""",

".gitignore": """
__pycache__/
*.pyc
*.pyo
*.pyd
.pytest_cache/
.mypy_cache/
.ruff_cache/
.venv/
build/
dist/
*.egg-info/
""",

"src/ballistics/__init__.py": '''
"""
Ballistics Platform
"""

__version__ = "0.1.0"
''',

"src/ballistics/common/constants.py": '''
from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:

    g = 9.80665

    gas_constant = 8.314462618

    standard_pressure = 101325.0

    standard_temperature = 288.15

    lapse_rate = -0.0065

    earth_rotation = 7.292115e-5

    earth_radius = 6378137.0

    gamma_air = 1.4

    molar_mass_air = 0.0289644


C = Constants()
''',

"src/ballistics/common/units.py": '''
from pint import UnitRegistry

ureg = UnitRegistry()

Q = ureg.Quantity
''',

"src/ballistics/common/vector.py": '''
from dataclasses import dataclass
import numpy as np

@dataclass(slots=True)
class Vector3:

    x: float
    y: float
    z: float

    def array(self):
        return np.array([self.x, self.y, self.z])

    @property
    def magnitude(self):
        return np.linalg.norm(self.array())

    def __add__(self, other):
        return Vector3(*(self.array() + other.array()))

    def __sub__(self, other):
        return Vector3(*(self.array() - other.array()))

    def __mul__(self, scalar):
        return Vector3(*(self.array() * scalar))
''',

"src/ballistics/common/state.py": '''
from dataclasses import dataclass

@dataclass(slots=True)
class SimulationState:
    time: float
''',

"src/ballistics/common/config.py": '''
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DATASETS = ROOT / "datasets"

BENCHMARKS = ROOT / "benchmarks"

DOCS = ROOT / "docs"

TESTS = ROOT / "tests"
''',

"src/ballistics/common/logger.py": '''
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("ballistics")
''',

"src/ballistics/common/atmosphere.py": '''
from dataclasses import dataclass

from .constants import C

@dataclass(slots=True)
class Atmosphere:

    altitude: float
    pressure: float
    temperature: float
    density: float

def standard_atmosphere(altitude: float) -> Atmosphere:

    T = C.standard_temperature + C.lapse_rate * altitude

    exponent = -C.g / (C.lapse_rate * C.gas_constant / C.molar_mass_air)

    P = C.standard_pressure * (T / C.standard_temperature) ** exponent

    rho = (P * C.molar_mass_air) / (C.gas_constant * T)

    return Atmosphere(
        altitude,
        P,
        T,
        rho,
    )
''',

"src/ballistics/common/integrators.py": '''
from typing import Callable

def rk4(f: Callable, y, t, dt):

    k1 = f(t, y)

    k2 = f(
        t + dt / 2,
        y + dt * k1 / 2,
    )

    k3 = f(
        t + dt / 2,
        y + dt * k2 / 2,
    )

    k4 = f(
        t + dt,
        y + dt * k3,
    )

    return (
        y
        + dt
        * (
            k1
            + 2 * k2
            + 2 * k3
            + k4
        )
        / 6
    )
''',

"tests/common/test_atmosphere.py": '''
from ballistics.common.atmosphere import standard_atmosphere

def test_sea_level():

    atm = standard_atmosphere(0)

    assert abs(atm.pressure - 101325) < 1
    assert abs(atm.temperature - 288.15) < 0.01
    assert abs(atm.density - 1.225) < 0.01
''',

"tests/common/test_units.py": '''
from ballistics.common.units import Q

def test_feet():

    assert round(
        Q(1, "foot").to("meter").magnitude,
        4,
    ) == 0.3048

def test_grains():

    assert round(
        Q(1, "grain").to("gram").magnitude,
        5,
    ) == 0.06480
'''
}


DIRECTORIES = [
    "docs",
    "docs/architecture",
    "docs/theory",
    "docs/validation",
    "docs/api",
    "docs/references",
    "datasets",
    "datasets/bullets",
    "datasets/cartridges",
    "datasets/powders",
    "datasets/atmospheres",
    "datasets/validation",
    "benchmarks",
    "benchmarks/external",
    "benchmarks/internal",
    "benchmarks/regression",
    "examples",
    "tests",
    "tests/common",
    "tests/internal",
    "tests/external",
    "tests/validation",
    "src",
    "src/ballistics",
    "src/ballistics/common",
    "src/ballistics/internal",
    "src/ballistics/external",
    "src/ballistics/terminal",
    "src/ballistics/validation",
    "src/ballistics/api",
    "src/ballistics/cli",
    "src/ballistics/data",
]


def write_file(root: Path, relative_path: str, contents: str) -> None:
    destination = root / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        textwrap.dedent(contents).strip() + "\n",
        encoding="utf-8",
    )


def main():

    root = Path(PROJECT_NAME)

    root.mkdir(exist_ok=True)

    for directory in DIRECTORIES:
        (root / directory).mkdir(parents=True, exist_ok=True)

    for filename, contents in FILES.items():
        write_file(root, filename, contents)

    print()
    print("=" * 60)
    print(" Ballistics Platform Repository Generator")
    print("=" * 60)
    print(f"Version : {VERSION}")
    print(f"Location: {root.resolve()}")
    print(f"Files   : {len(FILES)}")
    print(f"Folders : {len(DIRECTORIES)}")
    print()
    print("Generation Complete.")
    print()


if __name__ == "__main__":
    main()
