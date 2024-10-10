# setup.py
from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    author="eagle",
    author_email="eagle@42.fr",
    description="A simple Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eagle/ft_package",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
