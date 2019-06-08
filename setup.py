# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


#version = re.search(
#    '^__version__\s*=\s*"(.*)"',
#    open('donors/donors.py').read(),
#    re.M
#    ).group(1)


#with open("README.rst", "rb") as f:
#    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-donors-project",
    packages = ["donors"],
    entry_points = {
        "console_scripts": ['donors = donors.donors:main']
        },
    install_requires=[
   'click','requests','validate_email','prettytable','googlemaps'
    ],
    version = "0.1.0",
    description = "Python command line application for donors project.",
    #long_description = long_descr,
    author = "Vivek Sridhar",
    author_email = "vivsridh2@gmail.com",
    url = "https://www.linkedin.com/in/vivsridh/",
    )
