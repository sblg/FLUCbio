# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:53:14 2020

@author: Cecilia Bang Jensen
"""

import numpy as np
import FLUCbio.data_functions as data_tools

def fluc_measure(postprandial_data):
	""" Calculates a measure of fluctuation expecting evenly distributed data """
	
	# Check data input
	data_info = data_tools.dataClass(postprandial_data)  
	data_tools.dataClass.data_check(data_info, nan=False)  
	
	# Extract variable measures
	pp_list = data_info.input[1]
	
	# Calculate measure of fluctuation
	differences,differences_of_diff = [],[] 
	
	temp_list = np.zeros(len(pp_list))
            
	for i,value in enumerate(pp_list):
	   if i != 0:
		   temp_list[i-1] = abs(pp_list[i] - pp_list[i-1])
		   differences.append(pp_list[i] - pp_list[i-1])
	for i,value in enumerate(differences):
	   if i != 0:
		   differences_of_diff.append(abs(differences[i] - differences[i-1]))
   
	fluc_result = sum(differences_of_diff)
	assert fluc_result >= 0, "Fluctuation should be positive"
	
	return(fluc_result)

