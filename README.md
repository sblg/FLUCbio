# fluctuation_modelling-
Python package for fluctuation modelling on longitudinal biological data

The package includes a main function ‘fluctuations’ for pre-processing of longitudinal fluctuating biological data to make it useful for machine learning setups. 

A sample class is first created and then the function can be
run on the class to calculate the various information
measures. The input data has to be a pandas dataframe (or
numpy matrix?).


Worth to mention in the script
•	IDs need to have the same number of measurements.
•	If dataframe has more than 3 columns, everything is ignored from the 4th column

To do
Normalization? Image vector

Using various input arguments the user can get specialized
output. It is possible to choose a number of points to
interpolate between true samples, a type of interpolation
and some ways to handle missing data. 

Describe input/output
Output  → result$cluster_sum  (R annotation but something similar)
Input type checks w. error messages

Missing data 
•	Percentage limit 
•	Different ways to impute?
•	Error messages if too much missing? And information on what has been imputed on

Imputation

Interpolation
•	which is default? Should it always be the same or should we make a check and then do most appropriate one? Maybe a function to check for this.

