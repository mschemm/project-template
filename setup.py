#! /usr/bin/env python
"""A template for scikit-learn compatible packages."""

import codecs
import os

from setuptools import find_packages, setup

# get __version__ from _version.py
ver_file = os.path.join('fi', 'zvr', '_version.py')
with open(ver_file) as f:
    exec(f.read())

DISTNAME = 'zvrkiwi'
DESCRIPTION = 'Custom Estimator for KIWI'
with codecs.open('README.rst', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'FI'
MAINTAINER_EMAIL = 'matthias.schemm@extern.f-i.de'
VERSION = __version__
INSTALL_REQUIRES = ['numpy', 'scipy', 'scikit-learn', 'shap', 'xgboost']

EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov']
}

setup(name=DISTNAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      version=VERSION,
      long_description=LONG_DESCRIPTION,
      zip_safe=False,  # the package can run out of an .egg file
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE)
