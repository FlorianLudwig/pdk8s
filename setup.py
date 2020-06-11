#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

setup_requirements = []

test_requirements = []

setup(
    author="Florian Ludwig",
    author_email="f.ludwig@greyrook.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Use python to define kubernetes charts",
    entry_points={
        "console_scripts": ["pdk8s=pdk8s.cli:main"]
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    name="pdk8s",
    packages=find_packages(include=["pdk8s"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/FlorianLudwig/pdk8s",
    version="0.1.0",
    zip_safe=False,
)
