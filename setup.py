"""Setup script for adjspecies3. Use `pip install .` in this directory."""

from setuptools import setup
import adjspecies3

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='adjspecies3',
    version='0.1.4',
    description=adjspecies3.__doc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/tavallaie/adjspecies/',
    license='BSD 2-Clause',
    author='Ali Tavallaie',
    author_email='a.tavallaie@gmail.com',
    packages=['adjspecies3'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'adjspecies = adjspecies:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
