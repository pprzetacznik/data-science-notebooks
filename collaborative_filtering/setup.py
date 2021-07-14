import os
from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name="cf",
    version="1.0",
    description="collaborative filtering",
    author="John Doe",
    author_email="my.email@collaborative-filtering.pl",
    url="https://github.com/my_profile/cf",
    license="Apache 2.0",
    packages=find_packages(),
    install_requires=read("requirements.txt").splitlines(),
    long_description=read("README.md"),
    python_requires=">=3.6",
)
