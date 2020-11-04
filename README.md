
# Analysing fluctuation and/or variation in biological data

FLUCbio is a python toolbox package useful for obtaining measures of fluctuation/variation for longitudinal biological data. This can be particularly helpful if the data is to be used in certain methods/tools expecting the data to be independent of time (eg. using a Random Forest in Machine Learning). 

The package uses simple methods to obtain fluctuation measure both to keep it logical and to not overcompensate making it unusable for small data sets. The input must be measurements of the biological variable eg. blood marker and the time points at which these were taken (given in a time unit). For now all measures are based on evenly distributed data (consistent time interval between measurements) but if a few measurements are not taken due to clinical setup the missing data points can be imputed. Missing values can be imputed as well.


Describe measures that can be obtained by the package:

<b> fluc_measures </b>

$$fluc(y) = \sum_{i=2}^{len(x)-1} abs((y_i-y_{i-1})-(y_{i+1}-y_i))$$

<b> fluc_measure2 </b>



<b> sum_ones </b>

<b> clust_sum </b>


Functions for calculating a measure of fluctuation based on summing up a discrete second derivative thereby catching how peaky and volatile the observed measures are. 

Another function can turn the observed measures into a image like grid with binary values for where the observed values are located (true/1) and this “image” can in turn be evaluated for how peaky and volatile it is by summing up the number of true/1 values. 





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


## Quick Install
these has to be checked.. and implemented 
- install the latest version (from GitHub): `pip install git+git://github.com/sblg/FLUCbio.git#egg=FLUCbio`
- install the latest PyPI version: `pip install FLUCbio`
- install FLUCbio via conda-forge: `conda install FLUCbio -c conda-forge`




## Functions

***fluc_measure()***

latest update v0.8.8 ??

`FLUCbio.fluc_measure(data)`

Parameters | Description
------------ | -------------
`data` |Pandas dataframe, numpy array, list of list or tuple are accepted inputs




***impute_data()***



`FLUCbio.impute_data(data, imputation_type)`

Parameters | Description
------------ | -------------
`data` |Pandas dataframe, numpy array, list of list or tuple are accepted inputs
`imputation_type` |str or int 




***image_interpretation()***

`FLUCbio.image_interpretation(data, num_interp_pts, grid_size, interpolation_type, lower_bound, upper_bound)`

Parameters | Description
------------ | -------------
`data` |Pandas dataframe, numpy array, list of list or tuple are accepted inputs
`num_interp_pts` |int 
`grid_size` |int 
`interpolation_type` |str or int 
`lower_bound` |int or float
`upper_bound` |int or float 



***clust_sum()***


`FLUCbio.clust_sum(image)`

Parameters | Description
------------ | -------------
`image` |numpy array or list
 




## Examples

The example is based on a postprandial (after meal) variable blood glucose.

```python
>>> import FLUCbio
>>> glucose_sample = FLUCbio.getData(data='test_glucose').data
>>> imputed_glucose_sample = FLUCbio.impute_data(glucose_sample).imputed
>>> fluctuation = FLUCbio.fluc_measure(imputed_glucose_sample)
>>> image = FLUCbio.image_interpretation(imputed_glucose_sample).image
>>> cluster_sum, summed_ones = FLUCbio.clust_sum(image)
```

## Requirements
check requirements for different python versions???
- [Python](https://www.python.org) 3.7.3 (others?)           
- [NumPy](http://www.numpy.org) >= 1.16.4
- [SciPy](https://www.scipy.org/scipylib/index.html) >= 1.2.1
- [Pandas](http://pandas.pydata.org) >= 0.24.2


