from setuptools import setup, find_packages
import sys

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys_error_args = CURRENT_PYTHON + REQUIRED_PYTHON
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of xspectre requires Python {}.{}, but you're trying to
install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install xspectre
This will install the latest version of xspecte which works on your
version of Python.
""".format(*sys_error_args))
    sys.exit(1)

EXCLUDE_FROM_PACKAGES = []

setup(
    name='xspectre',
    version='0.0.1',
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    url='',
    license='MIT License',
    author='Joe Durbak',
    author_email='durbak.3@gmail.com',
    description='Cross-Dispersed Spectra Reduction',
    scripts=[],
    include_package_data=True,
)
