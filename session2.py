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


## Functions can return multiple values & value types
def test_value(value):
	return value < 10, [value]

a, b = test_value(15)
# print a, b


## Function can have (multiple) default arguments
def limit(value, threshold = 5, smaller_val = 0):
	if value >= threshold:
		return threshold
	else:
		return smaller_val

# print limit(4), limit(10, 10), limit(10, 15, 1), limit(5, smaller_val = 3)


## Functions can be stored in collections (e.g. lists)
def same(val):
	return val

def double(val):
	return 2.0 * val

def squared(val):
	return val ** 2

funcs = [same, double, squared]

#print funcs[0](5), funcs[1](6), funcs[2](7)

for f in funcs:
	a = f(5)
	# print a


## Functions do not have to return a value
## In that case the default return value is None

def better_print(val):
	print val, type(val)

# a = better_print(10)
# print a


####
# Some useful functions from the standard library
####

## Type Conversions (immutable types)
a = 10.5
#  print type(a)
# print int(a), float(a), str(a), bool(a), complex(a)
# print round(a)

## Functions for iterables
a = 'bAABcda'
# print len(a), max(a), min(a)
# print sorted(a)
# print sum(a)


####
# Lists II
####

## Extended indexing and concatenation
a = range(10)
# print a[-1], a[5:-2]

## List comprehension = For loop that creates a list
a = [i*2 for i in range(10)]
# print a


## List comprehensions work with if
a = [i**2 for i in range(10) if i%2]
# print a

## The in statement
b = 10
if b in a:
	print 'Found', b

## Pretty printing (should be in string chapter)
## WORKS WITH LISTS CONTAINING ONLY STRINGS!!
students = ['Che', 'Fidel', 'Raul']
attendance = ', '.join(students)
# print 'Students attending Revolution 101:', attendance
# print '\n'.join(students)


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

# tester(5)

# Produces this error message:

#Traceback (most recent call last):
#  File "C:\Code\Pytut\session2.py", line 80, in <module>
#    tester(5)
#  File "C:\Code\Pytut\session2.py", line 78, in tester
#    return val2
#NameError: global name 'val2' is not defined

# This catches the error
try:
	tester([1, 2, 3, 11])
except NameError:
	pass


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
both = a.items()
# print all_keys, '\n', all_values
# print both