import setuptools
from os import path

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name='expresspay_python_sdk',
  version='1.0.0',
  description='Expresspay Python SDK',
  packages=setuptools.find_packages(),
  author='Jeffery Osei',
  author_email='jefferyosei@expresspaygh.com',
  long_description=long_description,
  long_description_content_type='text/markdown',
  zip_safe=False,
  url='https://github.com/expresspaygh/expresspay-python-sdk',
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.7.3',
)