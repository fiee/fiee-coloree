# -*- coding:utf-8 -*-
from __future__ import absolute_import
# from __future__ import unicode_literals
from setuptools import setup, find_packages

setup(name='fiee-coloree',
      version='0.2.1',
      description='color conversion tools',
      keywords='color picker widget RGB CMYK conversion',
      author='Henning Hraban Ramm',
      author_email='hraban@fiee.net',
      license='BSD',
      url='https://github.com/fiee/fiee-coloree',
      download_url='https://github.com/fiee/fiee-coloree/tarball/master',
      package_dir={'coloree': 'coloree',},
      packages=find_packages(),
      include_package_data = True,
      # fails with unicode_literals
      package_data = {'': [
            '*.rst',
            'locale/*/LC_MESSAGES/*.*',
            'templates/*/*.*',
            'templates/*/*/*.*', ]},
      # see http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities',
                   'Natural Language :: English',
                   'Natural Language :: German', ],
      install_requires=['Django>=1.6', ],
      zip_safe=False,
      )
