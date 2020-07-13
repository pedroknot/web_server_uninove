from setuptools import setup

"""
web server
"""

#####################################################################
#####################DEFINE HERE THE PARAMETERS######################
project_name = 'web-server-uninove'
description = 'web-server-uninove'
version = '0.1'
author = 'pedroknot'
author_email = 'pedroknots@gmail.com'
url = 'https://github.com/'
#####################################################################

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name=project_name,
      version=version,
      description=description,
      author=author,
      author_email=author_email,
      url=url,
      packages=find_packages(),
      package_data={'app': ['**/*.py'],
                    'test': ['**/*.py'],
                      '.': ['README.md',
                            'config.py',
                            '.covaragerc',
                            '.pylintrc',
                            'run_tests.sh',
                            'requirements.txt']})