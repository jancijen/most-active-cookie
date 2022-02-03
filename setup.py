from setuptools import setup, find_packages
from io import open
from os import path

import pathlib

WORKING_DIR = pathlib.Path(__file__).parent
README = (WORKING_DIR / 'README.md').read_text()

# Required modules from requirements.txt
with open(path.join(WORKING_DIR, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup (
 name = 'most_active_cookie',
 description = 'Command line app for finding the most active cookie from given logs.',
 version = '1.0.0',
 packages = find_packages(),
 install_requires = install_requires,
 python_requires='>=3.7',
 entry_points='''
        [console_scripts]
        most_active_cookie=src.most_active_cookie.__main__:main
    ''',
 author='Jan Jendrusak',
 long_description=README,
 long_description_content_type='text/markdown',
 url='https://github.com/jancijen/most-active-cookie',
)
