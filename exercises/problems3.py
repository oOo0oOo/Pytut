####
# PROBLEM 3_A (easy, just a long description...)
####

# We are working towards controlling devices via serial commands.
# This is done by sending commands as strings.
# Imagine a programm controlling a and a two-way valve

# The pump has the following commands:
#	pump, stop
# The valve has the following commands:
#	chip, waste

# Both devices have unique adresses (pump: 0, valve: 1) and a command is bult up as follows:
# command = '/adress/command\c\r' Notice the \c\r in the end of the command.
# E.g. Stop pump: '/0/stop\c\r'


# Make a list containing the commands to do the following operation
# 1. Set valve to waste, then start pump
# 2. Stop pump, then switch valve to chip
# 3. Pump some fluid through your chip
# 4. Stop pump, then switch valve back to waste
# 5. Pump some more, then stop pump.



####
# PROBLEM 3_B
####

# Make a function that returns the value from dictionary
# if the value is present otherwise return False.
# (this function is exctly what dictionary.get(key) does,
# so it is not allowed here.



####
# PROBLEM 3_C
####

# Count the number of times each word comes up in this text (use dictionary, ignore upper case).
# Make a list with all the words that come up more than 6 times...

text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pellentesque viverra convallis. Donec euismod eu orci quis ultrices. Sed non gravida enim. Phasellus pharetra nibh leo, sit amet lacinia leo egestas vitae. Cras sed neque sit amet eros laoreet feugiat eget at lorem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam tempus ante vitae lectus rhoncus, consequat mollis velit tempus. Sed nibh orci, tristique in fringilla sed, malesuada vitae nisl. Nunc imperdiet imperdiet rutrum. Pellentesque purus odio, fringilla in imperdiet a, blandit quis odio. In hac habitasse platea dictumst. Etiam faucibus dolor a mattis tincidunt.
Sed sodales at mi sed porta. In hac habitasse platea dictumst. Mauris adipiscing mollis consectetur. Aenean a porttitor lectus. Morbi magna turpis, iaculis sit amet interdum eu, sollicitudin laoreet augue. Ut ultrices rutrum auctor. Proin justo magna, vehicula ac varius nec, malesuada eget augue. Duis malesuada diam et felis sagittis rutrum eu sed sem. Sed ullamcorper, nisi pretium fermentum sollicitudin, eros velit aliquet tellus, hendrerit interdum dui arcu ac purus. Ut molestie gravida semper. Pellentesque condimentum placerat neque, lacinia gravida sapien aliquet mattis. Nam scelerisque ipsum ac vestibulum tincidunt. Pellentesque cursus ullamcorper consectetur.
Duis fringilla mattis arcu, nec tempor quam pretium vel. Phasellus quis lectus pellentesque, laoreet quam tempor, viverra sapien. Ut id mi lacinia, adipiscing magna ut, feugiat ante. Morbi eget rhoncus leo, sit amet hendrerit sapien. Nulla interdum tincidunt neque, vel lobortis elit laoreet vel. Pellentesque lectus magna, dapibus quis vulputate eu, adipiscing non felis. Cras quis vehicula urna. In pretium ultricies hendrerit. Sed blandit neque a orci venenatis ultricies.
Proin vehicula quam eros. Proin eu ultrices dui. Suspendisse imperdiet massa vitae erat malesuada, eget facilisis mauris iaculis. Integer eu magna cursus, ullamcorper diam ut, eleifend enim. Mauris laoreet nunc nunc, vel dapibus nisl interdum adipiscing. Cras accumsan erat libero, scelerisque sodales neque mattis ultrices. Cras nisi mi, gravida et felis sit amet, viverra hendrerit risus. Donec vel elit sollicitudin, placerat eros iaculis, feugiat enim. In ultrices urna at magna suscipit, non porttitor sem blandit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ultrices, felis a luctus pharetra, quam nunc bibendum mi, a commodo magna augue non risus. Vestibulum elementum velit in semper consectetur. Quisque bibendum gravida mauris, et gravida eros ultricies at. Suspendisse id ultrices lorem. Fusce ut blandit quam, ac accumsan mi.
Morbi mi odio, accumsan nec turpis quis, malesuada placerat eros. Cras a accumsan diam, non interdum libero. Mauris et ligula urna. Sed euismod suscipit porta. Aliquam erat volutpat. Proin ultrices pharetra magna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse hendrerit sollicitudin condimentum. Cras arcu ante, aliquam sed sem vitae, ultricies luctus tortor. Ut eu semper ante.
'''



####
# PROBLEM 3_D (recap of the previous topics)
####

# 1. Calculate remainder of 2^777 divided by 777

# 2. Why is 2/3 not the same as 2./3

# 3. How do you take all except the last element of a list?

# 4. Create a list containing all numbers below 10 and add another element to it

# 5. How can you permanently remove the second element in the list from 4.

# 6. Loop over each element in your list and show it to the user if it is a integer.

# 7. Make a function that takes one input value and returns 3 multiplied with the input value.

# 8. Convert 0.123456789 into an integer, convert that into a boolean, convert that into a string and then a list.

# 9. How do you convert a string into all lowercase / all uppercase letters.

# 10. How do you find the index where 'aj' first comes up in 'poaiu h.dfbc4nv1t;ml.sdfhg125sd5io pajklsdf79hpoiun b'.

# 11. Write a list comprehension that doubles every element in [1, 2, 3, 4, 5, 6].