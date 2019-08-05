"""
This script is an example that contains this documentation!
"""

import os
print(os.__file__) # Displayes location of the module e.g. '/anaconda3/lib/python3.6/os.py'

import glob2
glob2.glob('*')
glob2.glob('*.txt')

def this_method():
	"""This method prints 'this method'"""
	print('This method')

# import more_functionality
# more_functionality.__doc__ # Outputs the doc text at the top of the file
# more_functionality.this_method.__doc__