
# Analysing fluctuation and/or variation in biological data

Python package for fluctuation modelling on longitudinal biological data

The package includes a main function ‘fluctuations’ for pre-processing of longitudinal fluctuating biological data to make it useful for machine learning setups. 

A sample class is first created and then the function can be
run on the class to calculate the various information
measures. The input data has to be a pandas dataframe (or
numpy matrix?).




Worth to mention in the script
•	IDs need to have the same number of measurements.
•	If dataframe has more than 3 columns, everything is ignored from the 4th column
•	Time points need to be evenly distributed - we can add missing data which is after imputed - minimum 4 time points

To do
Normalization? Image vector

Using various input arguments the user can get specialized
output. It is possible to choose a number of points to
interpolate between true samples, a type of interpolation
and some ways to handle missing data. 

Describe input/output
Output  → result$cluster_sum  (R annotation but something similar)
Input type checks w. error messages

Missing data 
•	Percentage limit 
•	Different ways to impute?
•	Error messages if too much missing? And information on what has been imputed on

Imputation

Interpolation
•	which is default? Should it always be the same or should we make a check and then do most appropriate one? Maybe a function to check for this.

## Functions

***fluc_measure()***



***impute_data()***



***image_interpretation()***



***clust_sum()***


## Examples

```python
>>> import FLUCbio
>>> glucose_sample = FLUCbio.data_functions.getData(data='test_glucose').data
>>> imputed_glucose_sample = FLUCbio.impute_data(glucose_sample)
>>> fluctuation = FLUCbio.fluc_measure(imputed_glucose_sample)
>>> image = FLUCbio.image_interpretation(imputed_glucose_sample).image
>>> cluster_sum, summed_ones = FLUCbio.clust_sum(image)
```

## Quick Install
these has to be checked.. and implemented 
- install the latest version (from GitHub): `pip install git+git://github.com/sblg/FLUCbio.git#egg=FLUCbio`
- install the latest PyPI version: `pip install FLUCbio`
- install FLUCbio via conda-forge: `conda install FLUCbio -c conda-forge`

#### Requirements
check requirements for different python versions???
- [Python](https://www.python.org) 3.7.3 (others?)           
- [NumPy](http://www.numpy.org) >= 1.16.4
- [SciPy](https://www.scipy.org/scipylib/index.html) >= 1.2.1
- [Pandas](http://pandas.pydata.org) >= 0.24.2


