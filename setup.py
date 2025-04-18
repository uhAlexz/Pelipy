from setuptools import setup, find_packages

setup(
    name="pelipy",
    version="1.0",
    description="A Python wrapper for the Pelican Panel",
    author="uhalexz",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.7",
)
