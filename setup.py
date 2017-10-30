import os
from setuptools import setup

setup(
    name="MATSU-bed-cli",
    version="0.1.0",
    description="MATSU-bed offline development tool",
    url='https://github.com/hardtail0112/MATSU-bed-cli',
    author='TAKAKI MATSUZAWA',
    author_email='takaaki0112@gmail.com',
    packages=["matsubed"],
    entry_points={
        'console_scripts': [
            'matsubed=matsubed.matsubed:main',
            'MATSU-bed-cli=matsubed.matsubed:main',
        ]
    },
)