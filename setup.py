# coding: utf-8

"""
    College Football Risk API

    Companion API for College Football Risk  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: admin@collegefootballdata.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "college-football-risk"
VERSION = "1.2.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="College Football Risk API",
    author="OpenAPI Generator community",
    author_email="admin@collegefootballdata.com",
    url="https://github.com/bluescar/college-football-risk-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "College Football Risk API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Companion API for College Football Risk  # noqa: E501
    """
)
