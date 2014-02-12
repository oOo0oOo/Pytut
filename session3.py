#-------------------------------------------------
#
# Python Tutorial Session 3
# (c) Oliver Dressler, 2013
#
#-------------------------------------------------


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

#print b


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
	tester( [1, 2, 3, 11] )
except NameError:
	pass



####
# Dictionaries (Key-Value Storage Container) 
####

a = {'asdfa': 12, 'asdffa': 151}
a[12] = 'blabla'
a['12'] = [1,2]
a['dict'] = {'another': 12}
#a[12] = 0.0
#print a

ages = {}
ages['oli'] = 'asdfasdfa'
ages['blabla'] = 'asdfasdga'
#print ages['oli']

# Example
all_keys = a.keys()
all_values = a.values()
both = a.items()
# print all_keys, '\n', all_values
# print both

## Use dict.get(key) if you are not sure that the key exists
# print a.get(12), a.get(13)
val = a.get(12)
if val:
	print val



####
# A dictionary example use case
####

## Some text (straight from wikipedia)
tragedies = '''Romeo and Juliet
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
Cymbeline'''

## Post processing: create a list with titles
## (each line of the multiline string a list element)
trag_list = tragedies.split('\n')
#print trag_list


## Post processing: Remove empty elements
trag_list = [t.lower() for t in trag_list]
#print trag_list


## Count letter frequency
freq = {}
for title in trag_list:
	for let in title:
		if let not in freq.keys():
			freq[let] = 1
		else:
			freq[let] += 1

print freq