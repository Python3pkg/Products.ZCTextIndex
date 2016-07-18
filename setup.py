##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from os.path import join
from setuptools import setup, find_packages, Extension

setup(name='Products.ZCTextIndex',
      version='3.0.dev0',
      url='http://pypi.python.org/pypi/Products.ZCTextIndex',
      license='ZPL 2.1',
      description="Full text indexing for ZCatalog / Zope 2.",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=(open('README.rst').read() + '\n' +
                        open('CHANGES.rst').read()),
      packages=find_packages('src'),
      namespace_packages=['Products'],
      package_dir={'': 'src'},
      ext_modules=[
          Extension(
              name='Products.ZCTextIndex.stopper',
              sources=[join('src', 'Products', 'ZCTextIndex', 'stopper.c')]),
          Extension(
              name='Products.ZCTextIndex.okascore',
              sources=[join('src', 'Products', 'ZCTextIndex', 'okascore.c')]),
      ],
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Framework :: Zope2",
          "License :: OSI Approved :: Zope Public License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2 :: Only",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: Implementation :: CPython",
      ],
      install_requires=[
          'setuptools',
          'AccessControl',
          'Acquisition',
          'BTrees',
          'transaction',
          'Persistence',
          'Products.ZCatalog',
          'zExceptions',
          'Zope2 >= 2.13.0dev',
          'ZODB',
          'zope.interface',
      ],
      include_package_data=True,
      zip_safe=False,
      )
