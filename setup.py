from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='mypastebot',
      description='A Python solution to creating pastes as a guest, listing new public pastes and more',
      long_description=long_description,
      long_description_content_type="text/markdown",
      version='0.1',
      url='https://github.com/jakestrouse00/pastebot',
      author='Jake Strouse',
      author_email='jakestrouse00@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      install_requires=['requests==2.22.0'],
      python_requires='>=3.6')
