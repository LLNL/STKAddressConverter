"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name = 'acs2internal',

    version = '1.0.1',

    description = 'Translates ACS / HLI-PRC address to internal address vice versa.',

    long_description = long_description,

    url = 'https://lc.llnl.gov/bitbucket/projects/DSG/repos/sl8500_acsls_converter/browse/SL8500-ACSLS_converter_python',

    author = 'Huy Le',

    author_email = 'le35@llnl.gov',

    license = 'Apache',

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries'
    ],

    keywords = 'ACS Internal address',

    packages = find_packages(exclude=['contrib', 'docs', 'tests'])

)
