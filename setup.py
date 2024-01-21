import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Rohan-102103108",
    version="1.1",
    description="Topsis-Rohan-102103108",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gandhi25samar/Topsis-Rohan-102103108.git",
    author="Rohan Gulati",
    author_email="gulatirohan2003@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["Topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "Topsis=Topsis.__main__:main",
        ]
    },
)