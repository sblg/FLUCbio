# -*- coding: utf-8 -*-

from setuptools import setup
import FlucAnalysis

with open("README.md", "r") as fh:
		long_description = fh.read()
		
setup(name='FlucAnalysis',
      version=FlucAnalysis.__version__,
      # metadata
      author='Cecilia Bang Jensen',
      author_email='ceciliabjensen@gmail.com',
      description='Fluctuation analysis toolkit',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='XXX',
      url='http://.github.io/',
      packages=['flucAnalysis',],
      zip_safe=False,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
       ],

      install_requires=['pandas', 'numpy', 'matplotlib', 'scipy', 'scikit-learn', 'seaborn', 'matplotlib_venn',
                        'tabulate', 'statsmodels', 'textwrap3', 'adjustText'],
      )



# An example of a setup file using setuptools package


'''

from setuptools import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='an_example_package',
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown'
)

'''

