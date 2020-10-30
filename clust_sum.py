# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:53:30 2020

@author: Cecilia Bang Jensen
"""

#import data_check as dc
#import FlucAnalysis.functions.data_functions as dc
#import FlucAnalysis.functions.image_interpretation as ii

import itertools


#test = ([0,5,30,60,120],[4,5,8,7,4])
#test = ([0,30,60,90,120],[4,6,9,5,3])
#test = ([0,30,60,90,120],[4,'hej',8,7,4])
#test = [[0,'hej',60,90,120],[4,5,8,7,4]]



#image = ii.image_interpretation(test).image
#print(image)


def clust_sum(image):
	"""  """
	
	
	# give either data or image ??
	
	
	
#	# Class object is created
#	data_info = dc.dataClass(test)
#	
#	# Data check is performed 
#	dc.dataClass.data_check(data_info,nan=False)
#	
#	# Create image
#	dc.dataClass.image(data_info)
#	
	
	### Clustering
	all_sums = []
	all_cluster = []
	
	all_sums.append(sum(image))
		
	count_dups = [sum(1 for _ in group) for _, group in itertools.groupby(image) if _ != 0]
	sum_ = 0
	for i in count_dups:
		if i > 1:
			sum_ += i
	all_cluster.append(sum_)
  
	
	return(all_cluster,all_sums)

#
#result_cluster,result_sum = clust_sum(image)
#print(result_cluster,result_sum)





