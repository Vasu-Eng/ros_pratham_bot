from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['pratham_bot','hardware_interface','motor_drivers_interface','servo_drivers_interface'],
    package_dir={'': 'include'},
)

setup(**setup_args)
