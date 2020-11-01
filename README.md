
# Analysing fluctuation and/or variation in biological data

FLUCbio is a python toolbox package useful for obtaining measures of fluctuation/variation for longitudinal biological data. This can be particularly helpful if the data is to be used in machine learning algorithms. 

Describe functions:

Functions for calculating a measure of fluctuation based on summing up a discrete second derivative thereby catching how peaky and volatile the observed measures are. Another function can turn the observed measures into a image like grid with binary values for where the observed values are located (true/1) and this “image” can in turn be evaluated for how peaky and volatile it is by summing up the number of true/1 values. 


The example is based on a postprandial variable blood glucose.



Input data is the longitudinal biological data for one sample and can be in a number of data types being numpy array, tuple, list of lists and pandas dataframe.

Data has to be evenly distributed meaning the same time interval between observations/measurements. If a data point is missing completely or is a NaN a function can impute the missing data point.





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


