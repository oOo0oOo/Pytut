# PROBLEM 1_A:
# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
 
# Find the sum of all the multiples of 3 or 5 below 1000.
s = 0
for i in range(1000):
	if i%3 == 0 or i%5 == 0:
		s += i

print 'Sum of multiples:', s

# PROBLEM 1_B:
# https://projecteuler.net/problem=5 (variation)

# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 16?

for i in xrange(1,1000000):
	found = 0
	for j in range(1, 17):
		if i%j == 0:
			found += 1
		else:
			break

	if found == 16:
		print 'Found number:', i
		break
