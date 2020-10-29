# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:10:48 2020

@author: Cecilia Bang Jensen
"""
import data_check as dc
#from data_functions import dataClass
import numpy as np  # can be removed
import pandas as pd  # can be removed




#test = [[0,30,60,90,120,180],[4,5,7,5,'Nan',4],[2,4,5,6,7,6]]
#test = ([0,30,60,90,120,180],['Nan','Nan','Nan','Nan','Nan','Nan'])
test = pd.DataFrame(np.array([[0,30,60,120,150,180],[4,6,9,5,np.nan,np.nan]]))  #check this. error now

test = pd.DataFrame(np.array([[0,30,60,120,150,180],[4,6,9,5,np.nan,3]]))
test = pd.DataFrame(np.array([[0,30,60,120,150,180],[4,6,9,5,'Nan',3]]))
#test = ([0,30,60,120],[4,5,8,4])
#test = ([0,30,60,120],[4,5,8,4])#,[1,2,3,4])
#test = ([0,'NA',60,120],[4,5,8,4])
#test = [[0,30,60,90,120],[4,5,8,7,4]]


# Make different test objects. tuple/listoflists and not this type. negative values
# imaginary?  missing values. only zeros. strings. dataframes. integers. 
# too many missing values. no missing values. Not same length of 1 and 2 element


# check if too many nans next to each other??
# more than two holes next to each other (I think i have.. or it is in general more than 2?)
# implement when there is both nan and a hole




def impute_data(postprandial_data, imputation_type=None):
	""" Imputes missing data or add imputed measures for unevenly distributed data """
	
	# Class object is created
	data_info = dc.dataClass(postprandial_data,imputation_type=imputation_type)
	
	# Data check is performed 
	dc.dataClass.data_check(data_info,nan=True)
	
	# Check if holes in time ()unevenly) and if so add extra imputed measurements
	dc.dataClass.insert_missing(data_info)	
	
	# Do imputation
	dc.dataClass.impute_data(data_info)	
	return(data_info)


resulting_data = impute_data(test,imputation_type='cubic')


print(resulting_data.num_timepoints)
print(resulting_data.input)    
print(resulting_data.imputation_type)
print(resulting_data.imputed)




# linear can not run if first element is nan?
# ValueError: A value in x_new is below the interpolation range.

