# -*- coding: utf-8 -*-
import os.path
from setuptools import setup

project_name = 'weekday_field'
version = '0.1.0'

setup_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(setup_dir, 'requirements.txt')) as req_file:
    requirements = ["django"]
with open(os.path.join(setup_dir, 'README.md')) as readme_file:
    readme = readme_file.read()

setup(
    name=project_name,
    version=version,
    description='Django weekday field',
    long_description=readme,
    author='Convious',
    author_email='vytautas@convious.com',
    url='https://github.com/Convious/weekday_field',
    packages=[
        project_name,
    ],
    package_dir={project_name: project_name},
    include_package_data=True,
    install_requires=requirements,
    license="BSD Zero Clause",
    keywords='weekday_field',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 4 - Beta',
        'License :: Freely Distributable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
)
