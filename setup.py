import setuptools


long_description = ""

setuptools.setup(
    name="fun", # Put your username here!
    version="0.0.1", # The version of your package!
    author="None", # Your name here!
    author_email="none@example.com", # Your e-mail here!
    description="A web scraping package", # A short description here!
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject", # Link your package website here! (most commonly a GitHub repo)
    packages=setuptools.find_packages(), # A list of all packages for Python to distribute!
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Enter meta data into the classifiers list!
    python_requires='>=3.6', # The version requirement for Python to run your package!
)
