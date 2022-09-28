from setuptools import setup

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name="handycam",
    version="v1.0.0",
    packages=["handycam"],
    install_requires=_requires_from_file('requirements.txt'),
)