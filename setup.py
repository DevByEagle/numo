from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="numo",
    version="1.0.0-alpha.2",
    description="A powerful, lightweight Python library designed to provide a variety of functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',	
    'Topic :: Software Development',
  ],
    install_requires=required,
    license="MIT",
    url="https://github.com/DevByEagle/numo",
    python_requires=">=3.10",
)
