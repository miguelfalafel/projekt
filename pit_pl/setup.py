import setuptools
from setuptools import find_packages

setup(
    name='pit_p',
    version='1.00',
    license='BSD 2-clause',
    author='Michał Jachimiak',
    author_email='m.jachmiak3@student.uw.edu.pl',
    packages=find_packages(),
    install_requires=["pandas", "numpy", "matplotlib", "openpyxl", "xlrd", "os"]
)