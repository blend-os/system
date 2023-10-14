"""Minimal setup.py to let tox run."""

from setuptools import find_packages, setup

setup(
    name="system",
    packages=find_packages(exclude=["tests"])
)