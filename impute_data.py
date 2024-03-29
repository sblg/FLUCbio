# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:10:48 2020

@author: Cecilia Bang Jensen
"""
import FLUCbio.data_functions as data_tools


def impute_data(postprandial_data, imputation_type='linear', adj_nan=2, nan=True):
	""" Imputes missing data and/or add imputed measures for unevenly distributed data """
	
	# Class object is created
	data_info = data_tools.dataClass(postprandial_data, imputation_type=imputation_type)
	
	# Data check is performed 
	data_info.data_check(nan)
	
	# Check if holes in time (unevenly) and if so add extra imputed measurements
	data_info.insert_missing(adj_nan)	
	
	# Do imputation and return class
	data_info.impute_data(adj_nan)	
	return(data_info)

