#-------------------------------------------------
#
# Python Tutorial Session 1
# (c) Oliver Dressler, 2013
#
#-------------------------------------------------

####
# Python vs. MATLAB
####

# + Learning Curve, Readability, Flexibility, Development Speed
# - Performance, Matlab Standard Library, (Scientific) Community


####
# Arithmetics
####

## Example 1: Variables
a = 15
b = -3
c = a + b
# print c


## Example 2: Complex arithmetics
c = (c + a) * b - (b / a)
# print c


## Example 3: Multiple assignments
x = y = z = 0
# print x, y, z
# Try: print first z then x on one line


## Example 4: Variables have to be defined
# print q
# Try: print q, a or print a, q


## Example 5: Compound operations and modulo
d = -1
d *= a # Means: d = d * a; Same: -=, += and /=
e = 48
f = e % 7 # Modulo: Remainder when divided by 7
# print d, f



####
# Datatypes: Integers, Floats
####


## Example 6: Numbers default to floats if needed
a = 4
b = 13.
# print a+b, a/b
# Try: b/a, b*a


## Example 7: Integers are rounded down
a = 11
# print a/2, a/2.0



####
# Booleans
####


## Example 8: Getting to know booleans
boolean = True

a = 4
b = a
c = ( a == b )
d = ( 4 == 4.0 )
e = ( c != d )
# print boolean, c, d, e



####
# Strings
####


## Example 9: Basic strings and string concatenation
a = 'i am a string'
b = ', so what?'
c = a + b
# print c, a, b


## Example 10: Escaping characters
# print 'i\'m a string', '\nme too\n\t!!!!!!!!'


## Example 11: Multiline strings
multiline_string = '''I am on the first line.
I\'m on the second line.
	I was last...'''
# print multiline_string


## Example 12: String slices (parts)
a = '12345'
b = a[0]
c = a[1:5]
# print b, c, c + b, a[1:5] + a[0]


## Example 13: Length of a string
len_a = len(a)
# print 'String a is', len_a, 'characters long\nindices: 0 -', len_a - 1


## Example 14: String formatting
a = 'The inserted string is: {}. It\'s length is: {}.'
inserted = 'LabView Sucks!'
final = a.format(inserted, len(inserted))
# print final



####
# Lists
####


## Example 15: Lists and list concatenation
l1 = [1, 2, 3]
l2 = ['1', '2', '3']
l3 = l1 + l2
# print l3, l3[1], l3[4:6]


## Example 16: Appending elements to a list, length of a list
len_before = len(l3)
l3.append('a')
l3.append(2.2222)
len_after = len(l3)
# print len_before, len_after, l3


## Example 17: Removing elements of a list
item_at_ind_3 = l3.pop(3)
# print item_at_ind_3, l3[3], l3



####
# For loops
####


## Example 18: Looping over a list
a = [0, 1, 2, 6]
b = 0
for i in a:
	b += i
# print b


## Example 19: The range() function
l1, l2 = [], []
num = range(10)

for i in num:
	l1.append(i)

for i in range(10):
	l2.append(i)

# print num, l1, l2, l1 == l2 == num



####
# if statements
####


## Example 20: A simple if statement
a = False

if a:
	t1 = True

if not a:
	t2 = True

l = [0, 1, 2, 3, 4]

if len(l) == 5:
	t2 = True
elif len(l) == 6:
	t2 = True
else:
	t2 = False

# print t1, t2


## Example 22: the break statement & the xrange function
for i in xrange(1000000000):
	if i >= 9999:
		break
# print i



####
# Summary
####

# Given a list with n items, how can we distribute the items 
# into m separate lists of equal length? 
# The result should be a list of lists

# Define the original list (to be split)
# and the number of sub lists
original = [2, 3, 4, 5, 6, 10, 11, 12, 12, 14]
num_sub_lists = 3

# Create the final list (a list containing num_sub_lists empty lists)
# E.g. final = [ [], [], [] ]
final = []
for i in range(num_sub_lists):
	final.append([])

# print 'Before:', final

# loop over the indices of each item in the original list
for i in range(len(original)):
	# Get the element at this index
	element = original[i]
	# Find the sub list it should be moved to (remainder of index/num_sub_lists) 
	sub_list = i % num_sub_lists
	# Append the item to this specific list
	final[sub_list].append(element)
	# Show the user what you just did:
	# print 'index: {}\nlist index: {}\nelement: {}\n{}\n'.format(i, sub_list, element, '_._' * 16)

# print 'Final:', final