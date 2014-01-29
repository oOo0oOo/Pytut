#-------------------------------------------------
#
# Python Tutorial Session 2
# (c) Oliver Dressler, 2013
#
#-------------------------------------------------


####
# Functions
####

## A simple function
def addition(arg1, arg2):
	result = arg1 + arg2
	return result

# print addition(3, 4)
# print result


## Functions can return multiple values
def test_value(value):
	return value < 10, value < 20

# print test_value(15) 


## Function can have (multiple) default arguments
def limit(value, threshold = 5, smaller_val = 0):
	if value >= threshold:
		return threshold
	else:
		return smaller_val

# print limit(4), limit(10, 10), limit(10, 15, 1), limit(5, smaller_val = 3)


####
# Lists II
####

## List comprehension = For loop that creates a list
a = [i*2 for i in range(10)]
# print a


## List comprehensions work with if
a = [i**2 for i in range(10) if i%2]
# print a


####
# Exceptions (Pythons Errors)
####

a = range(5)
# b = a[5]

# Produces this error (exception):

#Traceback (most recent call last):
#  File "C:\Code\Pytut\session2.py", line 58, in <module>
#    b = a[5]
#IndexError: list index out of range

# Lets catch it:
try:
	b = a[5]
except IndexError:
	b = 0

# print b


## Another example
def tester(val):
	return val2

tester(5)

# Produces this error message:

#Traceback (most recent call last):
#  File "C:\Code\Pytut\session2.py", line 80, in <module>
#    tester(5)
#  File "C:\Code\Pytut\session2.py", line 78, in tester
#    return val2
#NameError: global name 'val2' is not defined


####
# Dictionaries (Key-Value Storage Container)
####

# Example
a = {'blue': 12, 'green': 15.0, 'red': 1}
# print a['blue'], a['green'] + a['red']

# Example
a = {}
a[12] = 'blabla'
a['12'] = [1,2]
a['dict'] = {'another': 12}
# print a

# Example
all_keys = a.keys()
all_values = a.values()
# print all_keys, '\n', all_values