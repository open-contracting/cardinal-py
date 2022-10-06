from setuptools import find_packages, setup

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="ocdscardinal",
    version="0.0.1",
    author="Open Contracting Partnership",
    author_email="data@open-contracting.org",
    url="https://github.com/open-contracting/cardinal",
    description="Calculate red flags and procurement indicators from OCDS data",
    license="BSD",
    packages=find_packages(exclude=["tests", "tests.*"]),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=[
    ],
    extras_require={
        "test": [
            "coveralls",
            "pytest",
            "pytest-cov",
        ],
        "docs": [
            "furo",
            "sphinx",
            "sphinx-autobuild",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
