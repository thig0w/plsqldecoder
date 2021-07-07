# -*- coding: utf-8 -*-
"""Installation script for disponible_api application."""
from distutils.util import convert_path
from pathlib import Path

from setuptools import setup, find_packages

main_ns = {}
ver_path = convert_path("src/plsqldecoder/_version.py")
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
requirements.remove(".")

DESCRIPTION = "Simple decoder for pl/sql developer password hash"
APP_ROOT = Path(__file__).parent
README = (APP_ROOT / "README.md").read_text()
AUTHOR = "Thiago Weidman"
AUTHOR_EMAIL = "tw@weidman.com.br"
PROJECT_URLS = {
    # todo: create a doc page
    "Documentation": "",
    "Bug Tracker": "",
    "Source Code": "",
}
EXTRAS_REQUIRE = {
    "dev": [
        "black",
        "flake8",
        "pre-commit",
        "pydocstyle",
        "pytest",
        "pytest-black",
        "pytest-clarity",
        "pytest-dotenv",
        "pytest-flake8",
        "pytest-flask",
        "tox",
    ]
}

setup(
    name="pslqldecoder",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    version=main_ns["__version__"],
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license="Apache 2.0",
    url="https://github.com/",
    project_urls=PROJECT_URLS,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require=EXTRAS_REQUIRE,
)
