from setuptools import find_packages
from setuptools import setup

setup(
    name='franka_mobile_sensors',
    version='2.7.1',
    packages=find_packages(
        include=('franka_mobile_sensors', 'franka_mobile_sensors.*')),
)
