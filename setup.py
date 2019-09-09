from setuptools import setup, find_packages

with open('requirements.txt') as reqsFile:
    requirements = reqsFile.read().splitlines()

setup(name='dictionary_navigator',
      version='1.0.0',
      description='Dictionary Navigator With Strings',
      url='https://github.com/leeransetton/dictionay_navigator',
      author='Leeran Setton',
      author_email='leeransetton@gmail.com',
      install_requires=requirements,
      packages=find_packages())
