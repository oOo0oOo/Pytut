#-------------------------------------------------
#
# Python Tutorial Session 2
# (c) Oliver Dressler, 2013
#
#-------------------------------------------------

####
# Poll
####

topics = [
'Interfacing with external devices (USB/Serial)', 							#
'Plotting data',															#
'Advanced statistics (tests & stuff)',										#
'Matrix computating (similar to MATLAB)',									#
'Image Processing',															#
'Making a graphical user interface',										#
'Single phase flow simulation (only on simulation pc)',						#
'Databases and large scale data handling',									#
'Symbolic computation (Mathematica / Wolfram alpha)',						#
'Advanced data handling: fft, interpolation, integration, clustering, ...'	#
]

title = 'Do you want to know about:'
# print title + '\n\n-' + '\n\n-'.join(topics)

####
# Datatype: Tuple (immutable list)
####

## A tuple is much like a list
t = (1, 2, 'number 3')
# print t, len(t), t[:2]


## But immutable (can not be changed after creation)
# t[1] = 'number 2'
# t.append(10)



####
# Functions
####

## A simple function
def addition(arg1, arg2):
	result = arg1 + arg2
	return result

a = addition(3, 4)
# print a


## Functions have their own namespace
## (Variables defined within a function are unavailable once the function has returned)
# print result


## Functions can return multiple values & value types
def test_value(value):
	return value < 10, [value]

a, b = test_value(15)
# print a, b


## Or multiple values in a tuple
results = test_value(15)
# print results, results[1] == b


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


## Functions can return other functions
## (Because Python is awesome...)

def make_scale(scaling_factor):

	def scale_func(value):
		return value * scaling_factor

	return scale_func

scaler = make_scale(1.1)
# print scaler(2.55), make_scale(1.1)(2.55)


####
# Some useful functions from the standard library
####

## Type Conversions (immutable types)
a = 10.5
# print type(a)
# print int(a), float(a), str(a), bool(a), complex(a)
# print round(a)


## Functions for iterables
a = 'bAABcda'

# Conversions
# print list(a), tuple(a)

# Some usefull operations
# print len(a), max(a), min(a)
# print sorted(a)
# print sum(a) # Only works for lists of "numbers"


## String specific
a = 'aSDf, Fdsa, Asdf, fdsa'

# print a.split(', ')
# print a.find('fdsa') # Returns index of first occurence (or -1)
# print a.upper()
# print a.lower()
# print a.title()
# print a.replace(', ', ' ... ')


## Pretty printing (should be in string chapter)
## WORKS WITH LISTS CONTAINING ONLY STRINGS!!
students = ['Che', 'Fidel', 'Raul']
attendance = ', '.join(students)
# print 'Students attending Revolution 101:', attendance
# print '\n'.join(students)


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


## Lets catch it:
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


## This catches the error
try:
	tester([1, 2, 3, 11])
except NameError, e:
	pass
	# print e



####
# Dictionaries (Key-Value Storage Container) 
####

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

## Use dict.get(key) if you are not sure that the key exists
# print a.get(12), a.get(13)
val = a.get(13)
if val:
	print val



####
# Quick summary
####

## Some text (straight from wikipedia)
tragedies = '''
Romeo and Juliet
Coriolanus
Titus Andronicus
Timon of Athens
Julius Caesar
Macbeth
Hamlet
Troilus and Cressida
King Lear
Othello
Antony and Cleopatra
Cymbeline
'''

## Post processing: create a list with titles
## (each line of the multiline string a list element)
trag_list = tragedies.split('\n')
# print trag_list


## Post processing: Remove empty elements
trag_list = [t.lower() for t in trag_list if t]
# print trag_list

## Count letter frequency
freq = {}
for t in trag_list:
	for let in t:
		if let not in freq.keys():
			freq[let] = 1
		else:
			freq[let] += 1

# print freq