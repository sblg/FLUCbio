# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:10:48 2020

@author: Cecilia Bang Jensen
"""
import FlucAnalysis.data_functions as data_tools
import numpy as np  # can be removed
import pandas as pd  # can be removed


# Make different test objects. tuple/listoflists and not this type. negative values
# imaginary?  missing values. only zeros. strings. dataframes. integers. 
# too many missing values. no missing values. Not same length of 1 and 2 element


# check if too many nans next to each other??
# more than two holes next to each other (I think i have.. or it is in general more than 2?)
# implement when there is both nan and a hole


def impute_data(postprandial_data, imputation_type=None):
	""" Imputes missing data or add imputed measures for unevenly distributed data """
	
	# Class object is created
	data_info = data_tools.dataClass(postprandial_data,imputation_type=imputation_type)
	
	# Data check is performed 
	data_tools.dataClass.data_check(data_info,nan=True)
	
	# Check if holes in time ()unevenly) and if so add extra imputed measurements
	data_tools.dataClass.insert_missing(data_info)	
	
	# Do imputation
	data_tools.dataClass.impute_data(data_info)	
	return(data_info)


resulting_data = impute_data(test,imputation_type='cubic')

# linear can not run if first element is nan?
# ValueError: A value in x_new is below the interpolation range.

