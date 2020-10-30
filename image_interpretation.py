# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:52:55 2020

@author: Cecilia Bang Jensen
"""

import data_check as dc
import pandas as pd
import numpy as np

test = pd.DataFrame(np.array([[0,30,60,90,120],[4,6,9,5,3]]))



def image_interpretation(postprandial_data, num_interp_pts=100, grid_size=10, interpolation_type='linear', lower_bound=None, upper_bound=None):
	
	# do checks and tell to impute if necessary
	



	
	# Class object is created
	data_info = dc.dataClass(postprandial_data, num_interp_pts, grid_size, interpolation_type, lower_bound, upper_bound)
	
	# Data check is performed 
	dc.dataClass.data_check(data_info,nan=False)
	
	# Create image
	dc.dataClass.image(data_info)
	
	
	return(data_info)
	


#resulting_data = image_interpretation(test,100,10,'cubic')
resulting_data = image_interpretation(test)

#print(resulting_data.num_timepoints)
print(resulting_data.image)


