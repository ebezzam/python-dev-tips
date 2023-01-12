import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydevtips",
    version="0.0.2",
    author="Eric Bezzam",
    author_email="ebezzam@gmail.com",
    description="Functions and scripts to demonstrate Python development tips.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ebezzam/python-dev-tips",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    include_package_data=True,
)
