## 2_A
s = sum([int(i) for i in str(2**1000)])
print 'Solution for 2a) is:', s

## 2_B 
consonants = list('bcdfghjklmnpqrstvwxz')

def translate(text):
	# Clean Text (all lowercase)
	text = text.lower()
	
	# Assemble the final text
	final = ''
	# loop over every character in the text
	for c in text:
		# Add the letter anyway
		final += c
		# If its a consonant add o and letter again
		if c in consonants:
			final += 'o' + c
	return final

print 'Solution 3_B:', translate('Solution 3_B')

## 2_C
def overlapping(list1, list2):
	for element in list1:
		if element in list2:
			return True
	return False

print '2 Tests for 2_C:'
print overlapping([0, 1, 'a'], ['b', 1, 2])
print overlapping(['a', 'b'], ['abc'])

## 2_D
def add_row(results):
	# Each new row starts with a 1
	r = [1]

	# Get the last added row
	prev = results[len(results)-1]

	# Next number is sum of two numbers in previous row
	for j in range(0, len(prev)-1):
		r.append(prev[j] + prev[j+1])

	# Each row ends with a 1
	r.append(1)

	# Add the row to the results list
	results.append(r)

	# Return the list with an added element
	return results

# Start with the first row and add 13 others
results = [ [1] ] 
for i in range(13):
	results = add_row(results)

print 'Solution for 2 d):'
# Use nice printing (formating) with pprint
from pprint import pprint
pprint(results)