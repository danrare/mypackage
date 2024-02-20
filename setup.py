from setuptools import setup, find_packages

setup(
    name = "my-package",
    version = "1.0",
    packages = find_packages(exclude = ["test"]),
    license = "MIT",
    description = "EDSA example python package",
    long_description = open("Readme.md").read(),
    install_requires = ["numpy"],
    url = "https://github.com/danrare/mypackage",
    author = "Daniel",
    author_email = "danrare81@gmail.com"
)
    
