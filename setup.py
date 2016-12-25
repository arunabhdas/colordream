# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='colordream',
    version='0.1.1',
    description='Dream up pleasing color palettes with ML',
    long_description=readme,
    author='Swaathi Kakarla',
    author_email='swaathi@skcript.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=(
    	['pybrain']
    )
)
