# SPDX-License-Identifier: (BSD-3)
# LLNL-CODE-805542
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:author:
    Andrea Chiang (chiang4@llnl.gov), 2020
"""
import codecs
import os
import re
from setuptools import find_packages, setup


NAME = "mttime"
PACKAGES = find_packages(where="src")
META_PATH = os.path.join("src", "mttime", "__init__.py")
KEYWORDS = ["seismology","inversion","source"]
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: LGPL License",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.8",
    "Topic :: Scientific/Engineering :: Physics",
]
INSTALL_REQUIRES =[
    "obspy >= 1.0",
    "pandas >= 1.0",
]

ENTRY_POINTS = {
    "console_scripts": [
        "mttime-run = mttime.scripts.run:main",
    ]
}

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


VERSION = "1.0.0"


if __name__ == "__main__":
    setup(
        name=NAME,
        description="Time domain moment tensor inverse routine",
        license="BSD License",
        url="https://github.com/LLNL/mttime",
        version=VERSION,
        author="Andrea Chiang",
        author_email="andrea@llnl.gov",
        keywords=KEYWORDS,
        long_description_content_type="text/x-rst",
        packages=PACKAGES,
        package_dir={"": "src"},
        entry_points=ENTRY_POINTS,
        python_requires=">=3.6.*",
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        include_package_data=True,
        options={"bdist_wheel": {"universal": "1"}},
    )
