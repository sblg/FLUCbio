
# FLUCbio python package

## Analysing fluctuation and/or variation in biological data

FLUCbio is a python toolbox package useful for obtaining measures of fluctuation/variation for longitudinal biological data thereby avoiding the use of AUC as a single important measure. This can be particularly helpful if the data is to be used in certain methods/tools expecting the data to be independent of time (eg. using a Random Forest in Machine Learning). 

The package uses simple methods to obtain fluctuation measure both to keep it logical and to not overcompensate making it unusable for small data sets. The input measurements of the biological variable must be positive values with the corresponding time points at which these were taken (given in a time unit). For now all measures are based on evenly distributed data (consistent time interval between measurements) but if a few measurements are not taken due to clinical setup the missing data points can be imputed together with missing values (using interpolating function).


### Measures of fluctuation or variation

The package provides two main methods of measuring fluctuation
1. Calculated measures of fluctuation/variation
1. Imaging approach

It also includes the AUC so that there is the possibility of comparing



<b> Fluctuation measures using ***_fluc_measure()_*** </b>

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

Calling _fluc_measure()_, _impute_data()_ or _image_interpretation()_ a dataClass object is created. From this some information on data as well as default or chosen setting can be retrieved:
- _.input_
- _.num_timepoints_
- _.imputation_type_
- _.grid_size_
- _.lower_bound_
- _.upper_bound_
- _.interpolation_type_
- _.num_interp_pts_



***_fluc_measure()_***

`FLUCbio.fluc_measure(data)`

The auc is calculated as the integral along the time axis using the composite trapezoidal rule. Numpy's trapz function is used for this. 

Parameters | Type | Description
------------ | -------------  | ---------------------
`input_data` |_pandas dataframe, numpy array, list of list or tuple_ |2-D input with time points being the first dimension and measurements being the second. Expects evenly distributed data with no missing values.

returns a dataClass object including extra variables _.auc_, _.fluc_meas_, _.var_meas_


***_impute_data()_***

`FLUCbio.impute_data(data, imputation_type, adj_nan)`

The impute function is used before the other tools in case of missing data or unevenly distanced data points. 
There is an upper limit for imputation of 25% missing data. If more missing data than this the function will raise an error. Furthermore is it possible to put a limit on how many missing values can be next to each other. If too many are next to each other, it is hard to impute getting a realistic output. The _adj_nan_ parameter is choosing how many adjacent nan or missing values can be accepted. The imputation is done using scipy.interpolate.interp1d and therefore accepts input that this function would take.


Parameters | Type | Description
------------ | ------------- | ---------------------
`input_data` |_pandas dataframe, numpy array, list of list or tuple_ |2-D input with time points being the first dimension and measurements being the second
`imputation_type` |_str or int, optional_ |(from scipy.interpolate.interp1d: Specifies the kind of interpolation as a string (‘linear’, ‘nearest’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’, ‘previous’, ‘next’, where ‘zero’, ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of zeroth, first, second or third order; ‘previous’ and ‘next’ simply return the previous or next value of the point) or as an integer specifying the order of the spline interpolator to use. Default is ‘linear’.) For 'slinear' and 'linear' border values (first and last time point) cannot be imputed. 
`adj_nan` |_int, optional_ |Maximum number of adjacent nan/missing values. Default is 2.

returns a dataClass object with _.input_ being the data input, _.imputed_ being the resulting data and _.adj_nan_ the chosen or default number of maximum adjacent missing values. 

***_image_interpretation()_***

`FLUCbio.image_interpretation(data, num_interp_pts, grid_size, interpolation_type, lower_bound, upper_bound)`

Parameters | Type | Description
------------ | ------------- | ---------------------
`input_data` |_pandas dataframe, numpy array, list of list or tuple_ |2-D input with time points being the first dimension and measurements being the second. Expects evenly distributed data with no missing values.
`num_interp_pts` |_int, optional_ |Default is 100.
`grid_size` |_int, optional_ |The value is used for creating a _n_ x _n_ grid. Default value for _n_ is 10. The higher value of _n_ the finer is the grid. To catch fluctuation make sure to have a high number of interpolated points when using a fine grid. 
`interpolation_type` |_str or int, optional_ |Default is 'linear'
`lower_bound` |_int or float, optional_ |A value for lower boundary of the grid. Default is minimum measured value of input data.
`upper_bound` |_int or float, optional_ |A value for upper boundary of the grid. Default is maximum measured value of input data.

returns a dataClass object with _.image_ being the image vector

***_clust_sum()_***

`FLUCbio.clust_sum(class)`

Parameters | Type | Description
------------ | ------------- | ----------------
`image` |_class_ | class object obtained from _image_interpretation()_
 
returns a dataClass object with _.all_sums_ and _.all_cluster_ being the two outcome measures

## Examples

The example data is based on a postprandial (after meal) variable blood glucose. NB! The input data has to have time measures as first dimension and measures as second.

```python
>>> import FLUCbio
>>> glucose_sample = FLUCbio.getData(data='test_glucose').data
>>> imputed_glucose_sample = FLUCbio.impute_data(glucose_sample).imputed

>>> dataObject = FLUCbio.fluc_measure(imputed_glucose_sample)
>>> print(dataObject.fluc_meas)
>>> print(dataObject.var_meas)
>>> print(dataObject.auc)

>>> dataObject = FLUCbio.image_interpretation(imputed_glucose_sample,interpolation_type='cubic')
>>> print(dataObject.image)
>>> dataObject = FLUCbio.clust_sum(dataObject)
>>> print(dataObject.all_sums)
>>> print(dataObject.all_cluster)
```

## Requirements
check requirements for different python versions???
- [Python](https://www.python.org) 3.7.3 (others?)           
- [NumPy](http://www.numpy.org) >= 1.16.4
- [SciPy](https://www.scipy.org/scipylib/index.html) >= 1.2.1
- [Pandas](http://pandas.pydata.org) >= 0.24.2


