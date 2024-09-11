import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heatmap4kmers",
    version="2.2.1",
    author="Rafal Urniaz",
    description="Visualization package for kmeRs similarity score matrix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/urniaz/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)