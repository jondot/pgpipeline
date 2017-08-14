# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pgpipeline',
    version='0.4.0',
    description='Pgpipeline: An automatic postgres item pipeline for Scrapy',
    long_description=readme,
    author='Dotan Nahum',
    author_email='jondotan@gmail.com',
    url='https://github.com/jondot/pgpipeline',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['dataset'])
