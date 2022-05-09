import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-ezuccarelli", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="ezucca@mit.edu",
    description="Sparse Regression",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jayzuccarelli/sparseregression",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
