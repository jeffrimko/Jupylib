from setuptools import setup, find_packages

setup(
    name = "jupylib",
    version = "0.1.0",
    author = "Jeff Rimko",
    author_email = "jeffrimko@gmail.com",
    description = "Python library for helper functions when working with Jupyter notebooks.",
    license = "MIT",
    keywords = "utility library",
    url = "https://github.com/jeffrimko/Jupylib",
    py_modules=["jupylib"],
    long_description=open("README.rst").read() or "",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
)
