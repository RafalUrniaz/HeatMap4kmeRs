import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HeatMap4kmeRs",
    version="1.1.0",
    author="Rafal Urniaz",
    author_email="rafal.urniaz@gmail.com",
    description="Visualization package dedicated to kmeRs similarity score matrix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RafalUrniaz/HeatMap4kmeRs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
)