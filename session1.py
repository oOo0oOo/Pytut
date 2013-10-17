#-------------------------------------------------
#
# Python Tutorial Session 1
# (c) Oliver Dressler, 2013
#
#-------------------------------------------------

####
# Basics, Operators
####

# Exercise 1: Variables
a = 15
b = 3
c = a + b
# print 'EX1:', c

# Exercise 2: Complex arithmetics
c = (c + a) * b - (b / a)
# print 'EX2:', c

# Exercise 3: Multiple assignment
x = y = z = 0
# print 'EX3:', x, y, z

# Exercise 4: Variables have to be defined
# print 'EX4:', q

# Exercise 5: Compound operations and modulo
d = -3
d *= a # Means: d = d * a; Same: -=, += and /=
e = 48
f = e % 7 # Modulo: Remainder when divided by 7
# print 'EX5:', d, f



####
# Datatypes: Integer, Float
####

# Exercise 6: Numbers default to floats if needed
a = 4
b = 13.
# print 'EX6:', a+b, a/b

# Exercise 7: Integers are rounded down
a = 11
# print 'EX7:', a/2, a/2.0



####
# Boolean
####

# Exercise 8: Getting to know booleans
a = 4
b = a
c = ( a == b )
d = ( 4 == 4.0 )
e = ( c != d )
# print 'EX8:', c, d, e



####
# String
####

# Exercise 9: Basic strings and string addition
a = 'i am a string'
b = ', so what?'
c = a + b
# print 'EX9:', c

# Exercise 10: Escaping characters
# print 'EX10:', 'i\'m a string', '\nme too\n\t!!!!!!!!!!!!!!!!!!'

# Exercise 11: Multiline strings
multiline_string = '''I am on the first line.
I\'m on the second line.
	I was last...'''
# print 'EX11:', multiline_string

# Exercise 12: String slices (parts)
a = '12345'
b = a[0]
c = a[1:5]
# print 'EX12:', b, c, c + b, a[1:5] + a[0]

# Exercise 13: Length of a string
len_a = len(a)
# print 'EX13:', 'String a is', len_a, 'characters long\nindices: ', 0, '-', len_a - 1

# Exercise 14: String formatting
a = 'The inserted string is: {}. It\'s length is: {}.'
inserted = 'LabView Sucks!'
# print 'EX14:', a.format(inserted, len(inserted))



####
# List
####

# Exercise 15: Lists and list addition
l1 = [1, 2, 3]
l2 = ['1', '2', '3']
l3 = l1 + l2
# print 'EX15:', l3, l3[1], l3[4:6]

# Exercise 16: Appending elements to a list, length of a list
len_before = len(l3)
l3.append('a')
l3.append(2.2222)
len_after = len(l3)
# print 'EX 16:', len_before, len_after, l3

# Exercise 17: Removing elements of a list
item_at_ind_3 = l3.pop(3)
# print 'EX 17:', item_at_ind_3, l3[3], l3



####
# For loops
####

# Exercise 18: Looping over a list
a = [0, 1, 2]
b = 0
for i in a:
	b += i
# print 'EX18:', b

# Exercise 19: The range() function
l = []
for i in range(10):
	l.append(i)
# print 'EX19', l



####
# if statement
####

# Exercise 20: A simple if statement
l = [0, 1, 2, 3, 4]
if range(5) == l:
	success = True
else:
	success = False
# print 'EX20:', success

# Exercise 21: If not only works with booleans!
l = []
num = 0
s = ''

num2 = 0.0
num3 = 3
if not l:
	if not num and not s:
		if not num2 or not num3:
			if True:
				pass
				# print 'EX21: Works...'

# Exercise 22: the xrange() function and the break statement
for i in xrange(1000000000):
	if i >= 9999:
		break
# print 'EX22:', i



####
# Combining what we have learned so far...
####

# Given a list with n items, how can we split this list into m separate lists?
# The result will be a list of lists

original = range(12)
num_sub_lists = 3
final = []

for i in range(num_sub_lists):
	final.append([])

# print 'Before:', final

for i in range(len(original)):
	sub_list = i % num_sub_lists
	element = original[i]
	final[sub_list].append(element)
	# print 'xxxxxxxxxxxxxxxxxxxxxxxx\nindex: {}\nlist index: {}\nelement: {}'.format(i, sub_list, element)

# print 'Final:', final



####
# PROBLEM 1_A (easier):
####

# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
 
# Find the sum of all the multiples of 3 or 5 below 1000.


####
# PROBLEM 1_B:
####

# https://projecteuler.net/problem=5 (variation)

# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 16?
