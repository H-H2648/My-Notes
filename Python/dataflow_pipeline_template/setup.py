import setuptools


requires = [
    "apache-beam[gcp]==2.36.0",
    "possibly other packages"
]

# needs this if we want to run dataflow pipeline from kfp
# but the actual component for triggering is not anywhere within this note so probably don't need this
extra_files = [(".", ["main.py"])]

setuptools.setup(
    name="pipeline_name",
    version="1.0.0",
    packages=setuptools.find_packages(),
    install_requires=requires,
    data_files=extra_files,
)
