# Solution 1a

# Collect all numbers
s1 = 0
for i in range(1000):
	if i%3 == 0 and i%5 == 0:
		s1 += i

# Next week you might use this one-liner:
s2 = sum([i for i in range(1000) if i%3 == 0 and i%5 == 0])

print 'Solution for 1 a) is:', s1

# Solution 1b
tests = range(16, 1, -1)
# print tests
for i in xrange(2, 1000000000):
	for j in tests:
		if i%j:
			break
	else:
		break

print 'Solution for 1 b) is:', i
