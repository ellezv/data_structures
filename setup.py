"""The setup for our data_structures project."""

from setuptools import setup

setup(
    name="Data structures",
    description="Implementations of various data structures in Python",
    version=0.1,
    author="Maelle Vance, Sera Smith",
    author_email="maellevance@gmail.com, seras37@gmail.ocom",
    license="MIT",
    py_modules=[
        'linked_list', 'stack',
    ],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        "test": ["tox", "pytest", "pytest-watch", "pytest-cov"]
    },
)
