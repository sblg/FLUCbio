# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:29:48 2020

@author: Cecilia Bang Jensen
"""
import numpy as np
import pandas as pd
import scipy.interpolate 
import itertools

class dataClass:
	
	"""
	Collection of data tools for analysis of fluctuation/variation. Initiation of dataClass object includes a data check ensuring data 
	credibility and quality. 
	
	Callable functions included in the dataClass class is one for imputation of data, one for calculating fluctuation measures, 
	one for interpreting the data as an image and lastly one for summing up 1s and adjacent 1s from the image result of previously mentioned function.

	How to use help
	
	
	"""	
	
	def __init__(self, input_data, num_interp_pts=100, grid_size=10, interpolation_type='linear', lower_bound=None, upper_bound=None, imputation_type=None):
		
		self.input = input_data
		
		# Check kind of input data
		if type(self.input) in [list,tuple,np.ndarray,pd.core.frame.DataFrame]:
			pass
		else:
			raise TypeError(" Input must be of type tuple, list of lists, numpy array or pandas DataFrame")
		
		# if list check dimensions
		if type(self.input) in [list,tuple]:
			assert len(self.input)==2, 'Expected length of input is two. Lists of times of measurement and measurements.'
			
		# if DataFrame check dimensions
		if type(self.input) == pd.core.frame.DataFrame:
			if len(self.input) == 2:
				self.input = self.input.to_numpy().tolist()
				
			elif len(self.input.columns) == 2:
				self.input = self.input.transpose().to_numpy().tolist()
				
			else: 
				raise TypeError('Dimensions of dataframe is not correct.')
		
		
		
		# run more checks on input arg here end less in functions ???
		
		self.imputation_type = imputation_type
		self.num_interp_pts = num_interp_pts
		self.grid_size = grid_size
		self.interpolation_type = interpolation_type		
		self.lower_bound = lower_bound
		self.upper_bound = upper_bound
		self.num_timepoints = len(np.unique(self.input[0]))
		
	
	def data_check(self,nan=True):
		
		"""
		Function checks that data has same number of observations for time and measurements, then converts all possible nan values into np.nan type.
		Data is checked for consisting of only positive, numerical values. Lastly the data is checked for being sorted and for its time intervals. 
		If the time intervals cannot be made evenly by simple insertion of data points an error is raised.
		
		"""
		self.anyNan = False
		
		assert len(self.input[0])==len(self.input[1]), 'Number of values does not match for time and measurements.'
		
		# Using function on data containing Nan or missing values
		if nan == True:
			if any(value in ['NaN','nan','NA','na','Nan','NAN'] or value != value for variable in self.input for value in variable):
				
				self.anyNan = True
				# Convert any NaN type to np.nan
				self.input = [np.nan if value in ['NaN','nan','NA','na','Nan','NAN'] or value != value else float(value) for variable in self.input for value in variable] 
				
				# Convert back to tuple type
				self.input = (self.input[0:self.num_timepoints],self.input[self.num_timepoints:len(self.input)])
				
				# Get indices of missing data points from the data
				nan_id = [index for index,value in enumerate(self.input[1]) if value is np.nan]
				
				# Now remove the values (time and missing value) from tuple
				self.input = ([value for index,value in enumerate(self.input[0]) if index not in nan_id],[value for index,value in enumerate(self.input[1]) if index not in nan_id])
				self.num_timepoints = len(np.unique(self.input[0]))
				
				# check for too many nans 
				assert sum(np.isnan(element) for element in self.input[0]) <= int(len(self.input[0])/4), 'Too many missing time values'
				assert sum(np.isnan(element) for element in self.input[1]) <= int(len(self.input[1])/4), 'Too many missing measurement values'
			elif any(type(value)==str for variable in self.input for value in variable):
				raise ValueError('String not accepted datatype')
			
			# test if all values are positive
			bool_values_positive = [elements >= 0 or np.isnan(elements) == True for variables in self.input for elements in variables]
			assert all(element == bool_values_positive[0] for element in bool_values_positive) and bool_values_positive[0]==True, 'Negative values in input!'
		
		
		# Using function on ready data
		if nan == False:
			if any(value in ['NaN','nan','NA','na','Nan','NAN'] or value != value for variable in self.input for value in variable):
				raise ValueError('Data contains NaN.')
			elif any(type(value)==str for variable in self.input for value in variable):
				raise ValueError('String not accepted datatype')
			# test if all values are positive
			bool_values_positive = [elements>=0 for variables in self.input for elements in variables]
			assert all(element == bool_values_positive[0] for element in bool_values_positive) and bool_values_positive[0]==True, 'Negative or NaN values in input'
		
		# Change to np.array using floats
		if type(self.input) in [list,tuple]:
			self.input = np.array(self.input, dtype=np.dtype(float)) 
		
		# Check if time values are sorted using a filtered timelist (no nan)
		filtered_list = np.isnan(self.input[0])		
		filtered_list = self.input[0][(~filtered_list)]
		assert all(filtered_list[i] <= filtered_list[i + 1] for i in range(len(filtered_list)-1)), 'Data is not sorted after time.'
		
		# Check time value intervals
		self.time_intervals = [-(filtered_list[i-1]-time) for i,time in enumerate(filtered_list) if i!=0 ]
		self.MIN_TIME_INT = abs(min(self.time_intervals))
		
		if nan == False:
			assert all(element == self.time_intervals[0] for element in self.time_intervals), "Unevenly distributed data. Make sure data is sorted after time and if unevenly use imputeData function first."
				
		# check for non-numerical values (np.nan is seen as numerical)
		try:
			[measurement+0.1 for variable in self.input for measurement in variable]
		except:
			raise ValueError('Non-numerical data in input')
		
		self.imputed = self.input.copy()
		self.evenly_dist = self.input.copy()
	
	def insert_missing(self,adj_nan):
		
		"""
		The missing values existing as a cause of missing measurements are checked for here and time points with negative values are inserted 
		for these to prepare for the imputation function.
		
		"""
		
		# Error check for need of imputation
		assert(any(time_interval != self.time_intervals[0] for time_interval in self.time_intervals) 
		or self.anyNan == True),'No need for imputation. It was not implemented. See help(FlucAnalysis.dataClass.insert_missing) for how to use function.' # OBS help
		
		# Use remainder to see if the intervals are possible to make evenly
		bool_no_remainder = [time_interval % self.MIN_TIME_INT == 0 for time_interval in self.time_intervals] 
		
		if False in bool_no_remainder:
			raise ValueError('The interval sizes are too random and cannot be made evenly. ')
		
		else:
			# Check for skipped interval steps that should be inserted. If several are skipped insert time points in a loop
			index_counter = -1
			for skipped_int in [time_interval/self.MIN_TIME_INT-1 for time_interval in self.time_intervals]:
				
				index_counter = index_counter+1						
				if skipped_int == 0:
					continue
				
				elif adj_nan > skipped_int > 0:
					for missing in range(1,int(skipped_int)+1):
						# First the missing observation(s) is added by time point value in both time point and measurement series
						self.evenly_dist = np.insert(self.evenly_dist, [index_counter+missing], self.evenly_dist[0][index_counter] + missing*self.MIN_TIME_INT, axis=1)
						# Secondly the measurement value(s) are exchanged for negative values that can later be imputed 
						self.evenly_dist[1][index_counter+missing] = -1				
					index_counter = index_counter+missing
					
				else:
					raise NotImplementedError('Too many missing time measurements in a row.')
					
		self.time_intervals = [-(self.input[0][i-1]-time) for i,time in enumerate(self.input[0]) if i!=0 ]
		self.imputed = self.evenly_dist.copy()
		self.num_timepoints = len(np.unique(self.evenly_dist[0]))
		
	def impute_data(self,adj_nan):
		
		""" 
		First a check that the amount of missingness is not above threshold and that imputation type is implemented. 
		Then the imputation is done using spline interpolation with extrapolation feature ensuring possibility of imputing end measures.
		"""
		
		# Check how many nan are adjacent
		bool_nan = np.isnan(self.imputed)		
		count_dups = [sum(True for _ in group) for _, group in itertools.groupby(bool_nan[1]) if _ == True]
		adj_nans = 0
		for i in count_dups:
			if i > 1:
				adj_nans += i
		assert adj_nans <= adj_nan, 'Too many nan next to each other'
		
		# Check argument for imputation
		assert self.imputation_type != None, 'Missing argument for imputation_type'
		if self.imputation_type not in ['slinear','quadratic','cubic','linear','nearest']:
			raise NotImplementedError('%s is unsupported for imputation using interpolation' % self.imputation_type) 
		
		# Imputation using spline
		for timeindex, measurement in enumerate(self.imputed[1]):
				
			if measurement < 0 or np.isnan(measurement) == True:   
					
				# Use data filtered for missing values and nan to interpolate				
				ppData_filt = pd.DataFrame(self.imputed)
				filter_criteria = ppData_filt.iloc[1,:] >= 0 
				ppData_filt = ppData_filt[filter_criteria.index[filter_criteria]]
				
				# Interpolation function
				f = scipy.interpolate.interp1d(np.asarray(ppData_filt.iloc[0]),np.asarray(ppData_filt.iloc[1]), kind=self.imputation_type, fill_value="extrapolate")
				
				# Imputation using function
				impValue = f(self.imputed[0][timeindex])
				if impValue > 0:
					self.imputed[1][timeindex] = impValue
				else:
					raise ValueError('Negative value imputed')
				
	def fluctuation(self):
		
		"""
		Fluctuation and variation measures are calculated together with area under the curve. 
		"""
		# Extract variable measures
		pp_list = self.imputed[1]
		
		# Calculate measure of fluctuation
		differences,diff_of_diff = [],[] 
		
		temp_list = np.zeros(len(pp_list)-1)
            
		# Calculation of the fluctuation by summing up differences of differences
		for index in range(len(pp_list)):
			if index != 0:
				temp_list[index-1] = abs(pp_list[index] - pp_list[index-1])
				differences.append(pp_list[index] - pp_list[index-1])
		for index in range(len(differences)):
			if index != 0:
				diff_of_diff.append(abs(differences[index] - differences[index-1]))
		self.fluc_meas = sum(diff_of_diff)
		self.var_meas = sum(temp_list)/len(pp_list)
		self.auc = np.trapz(pp_list)
		
		assert self.fluc_meas >= 0, "Fluctuation should be positive"
		assert self.var_meas >= 0, "Variation should be positive"
		
	
	def image(self):
		
		"""
		The imaging is done in four steps:
		1. Boundaries are defined as lower boundaries for both time (x) and measures (y)
		2. Extra time points are added using interpolation 
		3. For the observation pairs (time, measurement) the lower boundary for both axis are saved
		4. Going through the grid using the lower boundaries of each observation pair to read if data exists in grid square or not
		assigning 1 to image if exists indeed and 0 if not
		"""
		
		# check arguments for imaging
		assert self.grid_size > 0, 'Grid size cannot be negative'
		
		if self.interpolation_type not in ['slinear','quadratic','cubic','linear','nearest']:
			raise NotImplementedError('%s is unsupported for interpolation for creating an image vector' % self.interpolation_type)
		
		assert self.num_interp_pts >= 0, 'Negative values not allowed for number of extra interpolation points'
		
		
		
		# Define interpolation function
		
		# OBS do we need to use input or evenly or imputed? input for in this case imputed would be a new input?! check this
		x_lbounds,y_lbounds = lower_bounds(self)
		
		
		time_points = np.arange(len(self.input[0]))+1
		time_values = self.input[1]
		extra_time_points = np.linspace(1, self.num_timepoints, num=self.num_interp_pts, endpoint=True)
		f = scipy.interpolate.interp1d(time_points, time_values, kind=self.interpolation_type)
		
		# Empty grid vector for all the "columns" in the graph/plot:
		self.image = np.zeros(self.grid_size*self.grid_size)                
		coordinate_pair = {}
            
		# Pairing x and y values of our interpolated points
		for value in extra_time_points:
			coordinate_pair[value] = float(f(value))
		
		
		# For x,y check through the boundaries and save the index of lower bound
		all_tempx_ids = np.zeros(self.num_interp_pts)
		all_tempy_ids = np.zeros(self.num_interp_pts)
		
		   
		j=-1
		for key, value in coordinate_pair.items():
			j += 1
			flag_x = False
			flag_y = False
                
			# First check in which column (x-value) the point belongs
                
			# OBS consider making it a while loop that will break when it is true
			
			
			
			
			for i in range(0,len(x_lbounds)):
				# First if statement most probable if i = 0
				if key == x_lbounds[i] and flag_x is False:
					flag_x = True
					tempx_id = i
					
					
				if key >= x_lbounds[i-1] and key < x_lbounds[i] and flag_x is False:
					flag_x = True
					tempx_id = i-1
						
						
				# IF last case ~ x > last boundary
				if key >= x_lbounds[-1] and flag_x is False:
					flag_x = True
					tempx_id = len(x_lbounds)-1
						
						
				# Now check the rows (y-value)
				if value == y_lbounds[i] and flag_y is False:  # change here
					flag_y = True
					tempy_id = i
						
				if value >= y_lbounds[i-1] and value < y_lbounds[i] and flag_y is False:
					flag_y = True
					tempy_id = i-1
						
						
				# IF last case ~ y > last boundary
				if value >= y_lbounds[-1] and flag_y is False:
					flag_y = True
					tempy_id = len(x_lbounds)-1 
						
						
				# When both boundaries for x and y are found we break the inner loop
				if flag_x and flag_y:
					break
					
				
				
			# Here we need to save the values in vectors
			all_tempx_ids[j] = x_lbounds[tempx_id]
			all_tempy_ids[j] = y_lbounds[tempy_id]
			# For each point we got the lower boundaries of where to find them
            
			
		image_dict = {}
		for value in x_lbounds:
			image_dict[value] = set()
            
		### Create image vector
		for i,value in enumerate(all_tempx_ids):
			
			# for each value x of interpolated data - add the y value to dict 
			image_dict[value].add(all_tempy_ids[i])
						   
		# To be able to sort the y grid the type is changed back to list
		for key,value in image_dict.items():
			
			image_dict[key] = sorted(set(value))
                
		# We now check for all grid boundaries whether if they are in our dict or not
		# and most importantly we create the vector from it
			
		j = 0
		for value in x_lbounds:
			for yl in y_lbounds:
				if yl in image_dict[value]:
					self.image[j] = 1
					j += 1
				else:
					self.image[j] = 0
					j += 1
		
		
		# OBS test with given upper or lower bounds
		
		
		# OBS check if image is correct!

		
	def clustering(self):
		"""
		
		"""
		self.all_sums=[]
		self.all_cluster=[]
		self.all_sums.append(sum(self.image))
		
		count_dups = [sum(1 for _ in group) for _, group in itertools.groupby(self.image) if _ != 0]
		sum_ = 0
		for i in count_dups:
			if i > 1:
				sum_ += i
		self.all_cluster.append(sum_)




def lower_bounds(self):
	
	if not self.lower_bound:
		y_min = min(self.input[1])
	else:
		y_min = self.lower_bound
	if not self.upper_bound:
		y_max = max(self.input[1])
	else:
		y_max = self.upper_bound
			
	y_range = y_max-y_min
	x_lbounds = [1]
	y_lbounds = [y_min]
	j = 0	
    
	
	# CREATE GRID LOWER BOUNDARIES 
	# OBS. explain this here - is loop necessary or can this be combined with above
	for i in np.arange(1+(self.num_timepoints-1)/self.grid_size, self.num_timepoints-(self.num_timepoints-1)/self.grid_size, (self.num_timepoints-1)/self.grid_size):
		x_lbounds.append(i)
		temp_y = y_lbounds[j]
		y_lbounds.append(temp_y+y_range/self.grid_size)
		j+=1
	return x_lbounds, y_lbounds



class getData:
	def __init__(self, data=None):
		if data=='test_glucose':
			self.data = pd.read_csv('./FLUCbio/test_data.csv', header=None)   # give a github link https://.github.io/assets/posts/reg/test_reg.csv")
		elif data=='another_example':
			self.data = pd.read_csv('https://.github.io/assets/posts/reg/boston.csv')   
		else:
			print('Error: Provide correct parameter for data\n') 

		
