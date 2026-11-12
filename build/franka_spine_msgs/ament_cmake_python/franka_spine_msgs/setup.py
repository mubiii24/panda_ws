from setuptools import find_packages
from setuptools import setup

setup(
    name='franka_spine_msgs',
    version='2.7.1',
    packages=find_packages(
        include=('franka_spine_msgs', 'franka_spine_msgs.*')),
)
