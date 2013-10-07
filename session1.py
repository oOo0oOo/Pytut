##
# Basics, Operators
##

# Ex 1
a = 15
b = 3
c = a + b
# print 'EX1:', c

# EX 2
c = (c + a) * b - (b / a)
# print 'EX2:', c

# EX 3
d = -3
d *= a # Means: d = d * a; Same: -=, += and /=

e = 48
f = e % 7 # Modulo: Remainder when divided by 7
print 'EX3:', d, f


##
# Datatypes: Integer, Float
##

# EX 4
a = 4
b = 13.0
# print 'EX4:', a+b, a/b

##
# Boolean
##

# EX 5
a = 4
b = a
c = ( a == b )
d = ( 4 == 4.0 )
e = ( c != d )
# print 'EX5:', c, d, e


##
# String
##

# EX 6
a = 'i am a string'
b = ', so what?'
c = a + b
# print 'EX6:', c

# EX 7
a = '12345'
b = a[0]
c = a[1:5]
# print 'EX7:', b, c, c + b, a[1:5] + a[0]

# EX 8
len_a = len(a)
# print 'EX8:', 'String a is', len_a, 'characters long\nindices: ', 0, '-', len_a - 1


##
# List
##

# EX 9
l1 = [1, 2, 3]
l2 = ['1', '2', '3']
l3 = l1 + l2
# print 'EX9:', l3, l3[1], l3[4:6]

# EX 10
len_before = len(l3)
l3.append('a')
l3.append(2.2222)
len_after = len(l3)
# print 'EX 10:', len_before, len_after, l3

# EX 11
item_at_ind_3 = l3.pop(3)
# print 'EX 11:', item_at_ind_3, l3[3], l3


##
# For loops
##

# EX 12
a = [0, 1, 2]
b = 0
for i in a:
	b += i
# print 'EX12:', b

# EX 13
l = []
for i in range(10):
	l.append(i)
# print 'EX13', l


##
# if statement
##

# EX 14
l = [0, 1, 2, 3, 4]
if range(5) == l:
	success = True
else:
	success = False
# print 'EX14:', success

# EX 15
l = []
num = 0
s = ''

num2 = 0.0
num3 = 3
if not l:
	if not num and not s:
		if not num2 or not num3:
			pass
			# print 'EX15: Works...'



