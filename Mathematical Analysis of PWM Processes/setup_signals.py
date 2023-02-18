from setuptools import find_packages, setup

setup(
    name='signals',
    packages=find_packages(include=['signals']),
    version="0.1.0",
    description="This packages contains the signals used to emulate carriers, and sine waves",
    author="Yasuo Ignacio Maidana Perez",
    install_requires=['numpy', 'scipy']
)
