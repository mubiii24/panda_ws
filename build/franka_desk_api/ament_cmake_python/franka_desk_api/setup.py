from setuptools import find_packages
from setuptools import setup

setup(
    name='franka_desk_api',
    version='3.4.1',
    packages=find_packages(
        include=('franka_desk_api', 'franka_desk_api.*')),
)
