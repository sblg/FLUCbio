# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:53:30 2020

@author: Cecilia Bang Jensen
"""

import itertools


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

