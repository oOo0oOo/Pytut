import csv
from random import randrange
from math import pi, sin

with open('example_s8.csv', 'wb') as file:
	writer = csv.writer(file)

	# Write Header
	writer.writerow(['Id', 'Area', 'X', 'Y'])

	# Create 500 entries
	for i in range(500):
		# Random x
		x = randrange(0, 1024)

		# Area and y are dependent on x
		area = str(x/2 + randrange(200, 500))
		y = sin(pi * x/220) * 75 + randrange(0, 120) - 60


		# Write the row into the file
		writer.writerow([str(i+1), area, str(x), str(int(y))])

