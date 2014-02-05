# Solution 1a

s1 = 0
for i in range(1000):
	if i%3 == 0 or i%5 == 0:
		s1 += i

# Next week you might use this one-liner:
s2 = sum( [i for i in range(1000) if i%3 == 0 or i%5 == 0] )

print 'Solution for 1 a) is:', s1


# Solution 1b
tests = range(16, 1, -1)
print tests

for i in xrange(2, 1000000000):
	for j in tests:
		if i%j != 0:
			break

	# This else is only reached if there was 
	# no break in previous loop (for j in tests:)
	else:
		break

print 'Solution for 1 b) is:', i
