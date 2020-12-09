# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:53:14 2020

@author: Cecilia Bang Jensen
"""

import numpy as np
import FLUCbio.data_functions as data_tools

def fluc_measure(postprandial_data, ignore_nan=False):
	""" Calculates a measure of fluctuation expecting evenly distributed data """
	
	# Check data input
	data_info = data_tools.dataClass(postprandial_data)  
	if ignore_nan is True:
		data_info.data_check(nan=True)
	if ignore_nan is False:
		data_info.data_check(nan=False)  
	data_info.fluctuation()
	
	return(data_info)

