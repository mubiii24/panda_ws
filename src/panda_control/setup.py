from setuptools import find_packages, setup

package_name = 'panda_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mubii',
    maintainer_email='you@example.com',
    description='Panda arm control scripts',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_arm = panda_control.move_arm:main',
            'pick_place = panda_control.pick_place:main',
            'manual_path = panda_control.manual_path:main',
            'record_path = panda_control.record_path:main',
            'play_path = panda_control.play_path:main',
            'pick_place_object = panda_control.pick_place_object:main',
        ],
    },
)
