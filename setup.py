# coding=utf-8
import sys
from setuptools import setup, find_packages

NAME = 'tolerance'
VERSION = '1.0.0'


def read(filename):
    import os
    from io import open
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r', encoding='utf-8') as fi:
        return fi.read()


def readlist(filename):
    rows = read(filename).split("\n")
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)


setup(
    name=NAME,
    version=VERSION,
    description=('A function decorator which makes a function tolerant ('
                 'the function fail silently).'),
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='function decorator, decorator, fail silently',
    author='Alisue',
    author_email='lambdalisue@hashnote.net',
    url='https://github.com/lambdalisue/%s' % NAME,
    download_url='https://github.com/lambdalisue/%s/tarball/master' % NAME,
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        '': ['LICENSE',
             'README.rst',
             'TEST.rst',
             'requirements.txt',
             'requirements-test.txt',
             'requirements-docs.txt'],
    },
    zip_safe=True,
    install_requires=readlist('requirements.txt')
)
