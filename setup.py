# Based off https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html

from distutils.core import setup

setup(
    name='Template',
    version='0.1dev',
    packages=['template',],
    license='MIT',
    long_description=open('README.md').read(),
)
