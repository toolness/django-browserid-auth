#!/usr/bin/env python
from setuptools import setup, find_packages

PKG="browserid_auth"
verstr="0.1"

setup(name=PKG,
      version=verstr,
      description="Django app for BrowserID authentication",
      author="Atul Varma",
      author_email="avarma@mozilla.com",
      url="https://github.com/toolness/django-browserid-auth",
      packages = find_packages(),
      install_requires = ['Django'],
      license = "BSD3",
      keywords="browserid",
      zip_safe = True
      )