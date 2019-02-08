import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heatmap4kmers",
    version="1.1.3",
    author="Rafal Urniaz",
    description="Visualization package dedicated to kmeRs similarity score matrix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RafalUrniaz/HeatMap4kmeRs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)