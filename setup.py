from setuptools import setup, find_packages
import pathlib

# Learn more: https://github.com/kennethreitz/setup.py (2012)
# 
# Read the contents of your README file for the long description
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    # Package metadata
    name="py-fun",                  # Name of your package on PyPI
    version="1.0.0",                    # Package version
    author="sgraupner",
    author_email="sgraupner@bht-berlin.de",
    description="A fun Python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/my_project",

    # Package structure configuration for src/ layout
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",

    # Dependencies (packages required at runtime)
    install_requires=[
        # "requests>=2.25.0",
        # "numpy>=1.20.0",
    ],

    # Optional development dependencies (e.g., pip install my_package[dev])
    extras_require={
        "dev": [
            # "pytest>=6.0",
            # "flake8>=3.9",
        ],
    },

    # Command line scripts / CLI tools (optional)
    # entry_points={
    #     "console_scripts": [
    #         "my-cli=my_package.main:cli_entrypoint",
    #     ],
    # },
)
