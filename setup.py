"""The setup for our data_structures project."""

from setuptools import setup

setup(
    name="Data structures",
    description="Implementations of various data structures in Python",
    version=0.1,
    author="Maelle Vance, Sera Smith, Ben Shields, Joey DeRosa",
    author_email="maellevance@gmail.com, seras37@gmail.com",
    license="MIT",
    py_modules=[
        'linked_list',
        'stack',
        'dll',
        'queue',
        'deque',
        'priority_queue',
        'binheap',
        'simple_graph',
        'binary_search_tree',
        'hash_table',
        'trie_tree'
    ],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        "test": ["tox", "pytest", "pytest-watch", "pytest-cov"]
    },
)
