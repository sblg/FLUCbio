# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:10:48 2020

@author: Cecilia Bang Jensen
"""
import FLUCbio.data_functions as data_tools


def impute_data(postprandial_data, imputation_type='linear', adj_nan=2):
	""" Imputes missing data or add imputed measures for unevenly distributed data """
	
	# Class object is created
	data_info = data_tools.dataClass(postprandial_data, imputation_type=imputation_type)
	
	# Data check is performed 
	data_tools.dataClass.data_check(data_info, nan=True)
	
	# Check if holes in time (unevenly) and if so add extra imputed measurements
	data_tools.dataClass.insert_missing(data_info)	
	
	# Do imputation and return class
	data_tools.dataClass.impute_data(data_info, adj_nan=adj_nan)	
	return(data_info)

