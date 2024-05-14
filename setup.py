from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A Python package for rotating images so that they are the right way up.'
LONG_DESCRIPTION = 'Rotates images 90, 180, or 270 degrees so that they are the right way up.'

setup(
    name="verbosetribble",
    version=VERSION,
    author="notteddydev",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'verbosetribble']
)