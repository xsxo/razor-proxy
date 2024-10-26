from setuptools import setup, find_packages
from os import path

README_FILE = open('README.md', 'r')
README = README_FILE.read()
README_FILE.close()


vers = {}
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'source', '__version__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), vers)

setup(
    name=vers['__title__'],
    author=vers['__author__'],
    url=vers['__url__'],
    version=vers['__version__'],
    description=vers['__description__'],
    license=vers['__license__'],
    long_description=README,
    long_description_content_type='text/markdown',
    package_data={'': ['LICENSE', 'NOTICE']},
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
        project_urls={
        'Source': vers['__url__'],
    },
    entry_points={
            'console_scripts': [
                'razor=source.razor:RazorProxy', 
            ],
        },
)