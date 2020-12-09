# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:52:55 2020

@author: Cecilia Bang Jensen
"""

import FLUCbio.data_functions as data_tools
import pandas as pd
import numpy as np


def image_interpretation(postprandial_data, num_interp_pts=100, grid_size=10, interpolation_type='linear', lower_bound=None, upper_bound=None, ignore_nan=False):
	
	# Class object is created
	data_info = data_tools.dataClass(postprandial_data, num_interp_pts, grid_size, interpolation_type, lower_bound, upper_bound)
	
	# Data check is performed 
	if ignore_nan is True:
		data_info.data_check(nan=True)
	if ignore_nan is False:
		data_info.data_check(nan=False)
	# Create image
	data_info.image()
	
	return(data_info)
	
