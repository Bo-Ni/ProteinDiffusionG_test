from setuptools import setup, find_packages

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/Bo-Ni/ProteinDiffusionG_test',
    author='Bo Ni',
    author_email='boni.mechanics@gmail.com',

    py_modules=find_packages(),
)
