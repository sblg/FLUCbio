
# FLUCbio python package

## Analysing fluctuation and/or variation in biological data

FLUCbio is a python toolbox package useful for obtaining measures of fluctuation/variation for longitudinal biological data thereby avoiding the use of AUC as a single important measure. This can be particularly helpful if the data is to be used in certain methods/tools expecting the data to be independent of time (eg. using a Random Forest in Machine Learning). 

The package uses simple methods to obtain fluctuation measure both to keep it logical and to not overcompensate making it unusable for small data sets. The input measurements of the biological variable must be positive values with the corresponding time points at which these were taken (given in a time unit). For now all measures are based on evenly distributed data (consistent time interval between measurements) but if a few measurements are not taken due to clinical setup the missing data points can be imputed together with missing values (using interpolating function).


### Measures of fluctuation or variation

The package provides two main methods of measuring fluctuation
1. Calculated measures of fluctuation/variation
1. Imaging approach

It also includes the AUC so that there is the possibility of comparing

<b> Fluctuation measures using ***_fluc_measure()_*** function</b>

The first measure uses the discrete second derivative as a measure of volatility. Summing up every turn the curve takes gives the wanted measure:

<img src="https://latex.codecogs.com/svg.latex?\fn_jvn&space;fluc(y)&space;=&space;\sum_{i=2}^{len(x)-1}abs((y_i-y_{i-1})-(y_{i&plus;1}-y_i))" title="fluc(y) = \sum_{i=2}^{len(y)-1}abs((y_i-y_{i-1})-(y_{i+1}-y_i))" />

Another measure can provide information on variation rather than fluctuation: 

<img src="https://latex.codecogs.com/svg.latex?\fn_jvn&space;var(y)&space;=&space;\frac{\sum_{i=2}^{len(y)}abs(y_i-y_{i-1})}{len(y)}" title="var(y) = \frac{\sum_{i=2}^{len(y)}abs(y_i-y_{i-1})}{len(y)}" />



<b> Imaging approach </b>



Another function can turn the observed measures into an image using a grid, curvefitting+interpolation and a grid search returning a vector with binary values (0 for pixels/grid squares with no observed value and 1 for pixels with observed value). This “image” can in turn be evaluated for how peaky and volatile it is by looking at the pattern of and number of 1's. 


<b> Sum of ones </b>

From the image a measure of fluctuation can be achieved by summing up all the 1's in the vector. The higher the number, the more fluctuating a curve.


<b> Clustered sum of ones </b>

Another way of summing the 1's from the image vector is to not sum all 1's but only those where two or more consecutive 1's exist. This way the sum will depend more on sudden steep rises or declines and less on big smooth curves. The grid size is an important parameter for this measure. 







Data has to be evenly distributed meaning the same time interval between observations/measurements. If a data point is missing completely or is a NaN a function can impute the missing data point.

Using various input arguments the user can get specialized output. It is possible to choose a number of points to
interpolate between true samples, a type of interpolation and some ways to handle missing data. 


## Quick Install
these has to be checked.. and implemented 
- Install the latest version (from GitHub): `pip install git+git://github.com/sblg/FLUCbio.git#egg=FLUCbio`
- Install the latest PyPI version: `pip install FLUCbio`
- Install via conda-forge: `conda install FLUCbio -c conda-forge`


## Functions

`FLUCbio.fluc_measure(data)`

Parameters | Type | Description
------------ | -------------  | ---------------------
`data` |_pandas dataframe, numpy array, list of list or tuple_ |Data will be 



`FLUCbio.impute_data(data, imputation_type)`

Missing data 
•	Percentage limit 
•	Different ways to impute?
•	Error messages if too much missing? And information on what has been imputed on


Parameters | Type | Description
------------ | ------------- | ---------------------
`data` |_pandas dataframe, numpy array, <br/>list of list or tuple_ |blablabla
`imputation_type` |_str or int, optional_ |default


`FLUCbio.image_interpretation(data, num_interp_pts, grid_size, interpolation_type, lower_bound, upper_bound)`

Parameters | Type | Description
------------ | ------------- | ---------------------
`data` |_pandas dataframe, numpy array,<br/> list of list or tuple_ |blablabla
`num_interp_pts` |_int, optional_ |blablabla
`grid_size` |_int, optional_ |blablabla
`interpolation_type` |_str or int, optional_ |blablabla
`lower_bound` |_int or float, optional_ |blablabla
`upper_bound` |_int or float, optional_ |blablabla


`FLUCbio.clust_sum(image)`

Parameters | Type | Description
------------ | ------------- | ----------------
`image` |_numpy array or list_ | blablabla
 

## Examples

The example data is based on a postprandial (after meal) variable blood glucose.

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


