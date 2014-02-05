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
# A dictionary example use case
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



####
# Reading Data From File
####

file = open('s3_data.txt', 'r')

## This is the tricky part, a file always needs to be closed
## This is a problem, when an error happens (the program exits)
## before closing properly.
file.close()

## ALWAYS USE EITHER with 
with open('s3_data.txt', 'r') as file:
	# Do something with file
	pass


##OR try: finally: with files to make sure they close
file = open('s3_data.txt', 'r')
try:
	#do something with file
	pass

# File gets closed even if an error happens in do something
finally:
	file.close()



with open('s3_data.txt', 'r') as file:
	pass
	## Reading Complete file
	#complete_file = file.read()
	#print len(complete_file)

	## Reading Line by line
	#for line in file:
	#	if len(line) > 6:
	#		print line



####
# Prompting the user
####


# user_input = raw_input('What is the weather like?\n')
# print user_input, type(user_input)

## Take care when prompting other than string
# user_input = raw_input('What is the weather like? (1-10)\n')
# print int(user_input)



####
# Object-oriented programming 
####




####
# Everything is an object
####