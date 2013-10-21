## Example 21: A lot of stuff defaults to False!
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
				# print 'It works...'