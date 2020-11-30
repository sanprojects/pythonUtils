from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="utils",
    version="0.0.1",
    author="san",
    description="Utilities",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/sanprojects/pythonUtils/",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
