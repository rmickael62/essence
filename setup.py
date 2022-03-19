import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = ""

# This call to setup() does all the work
setup(
    name="Prix-Carburant-FR-rmickael62-Client",
    version="0.0.2",
    description="StationEssence client by Rmickael62",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rmickael62/essence",
    author="Maxime Wantiez, Yann RITTER",
    author_email=" ",
    license="MIT",
    packages=["prixCarburantClient"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
