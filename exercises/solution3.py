## 3_A
def make_cmd(device, command):
	'''
		Makes command according to template: 
		/adress/command\\c\\r 
		(notice the escaped \ character)
	'''

	command = '/{}/{}\\c\\r'.format(device, command)
	return command

p_pump = make_cmd(0, 'pump')
p_stop = make_cmd(0, 'stop')
v_chip = make_cmd(1, 'chip')
v_waste = make_cmd(1, 'waste')

# print p_pump, v_waste

commands = [
	v_waste, p_pump,
	p_stop, v_chip,
	p_pump,
	p_stop, v_waste,
	p_pump, p_stop
]

print '3_A list of commands:\n', commands



## 3_B
def getter(dictionary, key):
	try:
		value = dictionary[key]
	except KeyError:
		value = False

	return value

a = {'a': 10, 'b': 20}
templ = '\nSolution 3_B; dict: {}\ngetter(dict, \'a\'): {}, getter(dict, \'c\'): {}'
print templ.format(a, getter(a, 'a'), getter(a, 'c'))



## 3_C

text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pellentesque viverra convallis. Donec euismod eu orci quis ultrices. Sed non gravida enim. Phasellus pharetra nibh leo, sit amet lacinia leo egestas vitae. Cras sed neque sit amet eros laoreet feugiat eget at lorem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam tempus ante vitae lectus rhoncus, consequat mollis velit tempus. Sed nibh orci, tristique in fringilla sed, malesuada vitae nisl. Nunc imperdiet imperdiet rutrum. Pellentesque purus odio, fringilla in imperdiet a, blandit quis odio. In hac habitasse platea dictumst. Etiam faucibus dolor a mattis tincidunt.
Sed sodales at mi sed porta. In hac habitasse platea dictumst. Mauris adipiscing mollis consectetur. Aenean a porttitor lectus. Morbi magna turpis, iaculis sit amet interdum eu, sollicitudin laoreet augue. Ut ultrices rutrum auctor. Proin justo magna, vehicula ac varius nec, malesuada eget augue. Duis malesuada diam et felis sagittis rutrum eu sed sem. Sed ullamcorper, nisi pretium fermentum sollicitudin, eros velit aliquet tellus, hendrerit interdum dui arcu ac purus. Ut molestie gravida semper. Pellentesque condimentum placerat neque, lacinia gravida sapien aliquet mattis. Nam scelerisque ipsum ac vestibulum tincidunt. Pellentesque cursus ullamcorper consectetur.
Duis fringilla mattis arcu, nec tempor quam pretium vel. Phasellus quis lectus pellentesque, laoreet quam tempor, viverra sapien. Ut id mi lacinia, adipiscing magna ut, feugiat ante. Morbi eget rhoncus leo, sit amet hendrerit sapien. Nulla interdum tincidunt neque, vel lobortis elit laoreet vel. Pellentesque lectus magna, dapibus quis vulputate eu, adipiscing non felis. Cras quis vehicula urna. In pretium ultricies hendrerit. Sed blandit neque a orci venenatis ultricies.
Proin vehicula quam eros. Proin eu ultrices dui. Suspendisse imperdiet massa vitae erat malesuada, eget facilisis mauris iaculis. Integer eu magna cursus, ullamcorper diam ut, eleifend enim. Mauris laoreet nunc nunc, vel dapibus nisl interdum adipiscing. Cras accumsan erat libero, scelerisque sodales neque mattis ultrices. Cras nisi mi, gravida et felis sit amet, viverra hendrerit risus. Donec vel elit sollicitudin, placerat eros iaculis, feugiat enim. In ultrices urna at magna suscipit, non porttitor sem blandit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ultrices, felis a luctus pharetra, quam nunc bibendum mi, a commodo magna augue non risus. Vestibulum elementum velit in semper consectetur. Quisque bibendum gravida mauris, et gravida eros ultricies at. Suspendisse id ultrices lorem. Fusce ut blandit quam, ac accumsan mi.
Morbi mi odio, accumsan nec turpis quis, malesuada placerat eros. Cras a accumsan diam, non interdum libero. Mauris et ligula urna. Sed euismod suscipit porta. Aliquam erat volutpat. Proin ultrices pharetra magna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse hendrerit sollicitudin condimentum. Cras arcu ante, aliquam sed sem vitae, ultricies luctus tortor. Ut eu semper ante.'''

# Clear up text
text = text.lower()
text = text.replace('.', '')
text = text.replace(',', '')
# Replace new lines with spaces
text = text.replace('\n', ' ')

# Split text into list of words
words = text.split(' ')
# print words

# Count occurence of each word
count = {}

for word in words:
	if word not in count.keys():
		count[word] = 1
	else:
		count[word] += 1

# print count

# Make a list with all the words that come up more than 6 times
common = [k for k, v in count.items() if v > 6]
print '\n3_C words that come up more than 6 times:\n', common



####
# PROBLEM 3_D (recap of the previous topics)
####
print '\n3_D RECAP:'

# 1. Calculate remainder of 2^777 divided by 777
# print (2**777)%777

# 2. Why is 2/3 not the same as 2./3
# int/int = int, float/int = float, int/float = float

# 3. How do you take all except the last element of a list?
a = range(5)
# print a[:-1]

# 4. Create a list containing all numbers below 10 and add two strings ('abc' and 'cba').
a = range(10)
a.append('abc')
a.append('cba')
# OR
b = range(10) + ['abc', 'cba']
# print a, b

# 5. How can you permanently remove the second element in the list from 4.
b.pop(1)
# print b

# 6. Loop over each element in your list and show it to the user if it is a string.
for element in b:
	if type(element) == str:
		# print element
		pass

# 7. Make a function that takes one input value and returns 3 multiplied with the input value.
def tripple(val):
	return val * 3.0
# print tripple(1), tripple(111.111)

# 8. Convert 0.123456789 into an integer, convert that into a boolean, convert that into a string and then a list.
# print list(str(bool(int(0.123456789))))

# 9. How do you convert a string into all lowercase / all uppercase letters.
a = 'AbCdEfGh aBcDeFgH'
# print a.lower(), a.upper()

# 10. How do you find the index where 'aj' first comes up in 'poaiunv1t;ml.s25sd5io paj9hpoiun b'.
# print 'poaiunv1t;ml.s25sd5io paj9hpoiun b'.find('aj')

# 11. Write a list comprehension that doubles every element in the list [1, 2, 3, 4, 5, 6].
# print [r*2 for r in range(1, 7)]