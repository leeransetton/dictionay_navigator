from setuptools import setup, find_packages

with open('requirements.txt') as reqsFile:
    requirements = reqsFile.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='dictionary_navigator',
      version='1.0.1',
      description='Dictionary Navigator With Strings',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/leeransetton/dictionay_navigator',
      author='Leeran Setton',
      author_email='leeransetton@gmail.com',
      install_requires=requirements,
      packages=find_packages())
