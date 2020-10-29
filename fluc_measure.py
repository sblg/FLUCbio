# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:53:14 2020

@author: Cecilia Bang Jensen
"""

import numpy as np
import data_check as dc

#test = ([0,5,30,60,120],[4,5,8,7,4])
#test = ([0,30,60,90,120],[4,5,8,7,4])
test = ([0,30,60,90,120],[4,'hej',8,7,4])
#test = [[0,'hej',60,90,120],[4,5,8,7,4]]


def flucMeasure(postprandial_data):
	""" Calculates a measure of fluctuation expecting evenly distributed data """
	
	# Check data input
	data_info = dc.dataClass(postprandial_data)  
	postprandial_data = dc.dataClass.data_check(data_info,nan=False)  
	
	# Extract variable measures
	pp_list = postprandial_data[1]
	
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
   
	flucResult = sum(differences_of_diff)
	assert flucResult >= 0, "Fluctuation should be positive"
	
	return(flucResult)


result = flucMeasure(test)
print(result)
