#!/usr/bin/env python
import os
from datetime import datetime
import io
import re
import shutil
import sys
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = (
"""GluonCV Python Package
=========================
`GluonCV <https://gluon-cv.mxnet.io>`_ provides implementations of the state-of-the-art (SOTA) deep learning models in computer vision.

It is designed for engineers, researchers, and students to fast prototype products and research ideas based on these models.

Installation
------------

To install, use:

.. code-block:: bash

    pip install gluoncv mxnet>=1.2.0

To enable different hardware supports such as GPUs, check out  `mxnet variants <https://pypi.org/project/mxnet/>`_.

For example, you can install cuda-9.0 supported mxnet alongside gluoncv:

.. code-block:: bash

    pip install gluoncv mxnet-cu90>=1.2.0

""")

VERSION = find_version('gluoncv', '__init__.py')

if 'TRAVIS_TAG' in os.environ and os.environ['TRAVIS_TAG'].startswith('patch-'):
    VERSION = os.environ['TRAVIS_TAG'].split('-')[1]
elif 'APPVEYOR_REPO_TAG_NAME' in os.environ and os.environ['APPVEYOR_REPO_TAG_NAME'].startswith('patch-'):
    VERSION = os.environ['APPVEYOR_REPO_TAG_NAME'].split('-')[1]
elif 'TRAVIS_TAG' in os.environ or 'APPVEYOR_REPO_TAG_NAME' in os.environ:
    pass
else:
    VERSION += 'b{0}'.format(datetime.today().strftime('%Y%m%d'))

requirements = [
    'numpy',
    'tqdm',
    'requests',
    # 'mxnet',
    'matplotlib',
    'Pillow',
    'scipy',
]

setup(
    # Metadata
    name='gluoncv',
    version=VERSION,
    author='Gluon CV Toolkit Contributors',
    url='https://github.com/dmlc/gluon-cv',
    description='MXNet Gluon CV Toolkit',
    long_description=long_description,
    license='Apache-2.0',

    # Package info
    packages=find_packages(exclude=('docs', 'tests', 'scripts')),

    zip_safe=True,
    include_package_data=True,
    install_requires=requirements,
)
