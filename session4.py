#-------------------------------------------------
#
# Python Tutorial Session 3
# (c) Oliver Dressler, 2013
#
#-------------------------------------------------



####
# Using other modules (the import statement)
####

## The random Module
## This module is imported from the standard library 
## (it's available with every installation of python 2.7.x )
import random

## Random float from uniform distribution [0.0, 1.0)
# print random.random()

## Random integer in range
# print random.randrange(5, 11)

## Random choice from list
# print random.choice(['jc paper 1', 'jc paper 2', 'jc paper 3'])

## Make a random, weighted decision
# E.g. Do something in 33% of cases
if random.random() < 0.33:
	amount = random.randrange(50, 100)
	# print 'You won {}$!'.format(amount)


## A full example: Creating some fake worm data
## (to test your nice statistics routine)

directions = list('NESW')

def create_random_worm_data():
	'''
	Example C. elegans Datapoint

	index: an integer identifying a specific worm
	position: a list containing the x and y coordinates
	orientation: a string of either N, E, S or W
	'''

	# You are observing 10 worms
	index = random.randrange(10)

	# The coordinate system is 10 x 10
	position = [random.randrange(1, 11) for i in range(2)]

	orientation = random.choice(directions)

	return index, position, orientation

# print create_random_worm_data()

# Create data set
data_set = [create_random_worm_data() for i in range(50)]
# print data_set


## Example data processing: Average worm position
positions = [data[1] for data in data_set]
x, y = [], []

for dx, dy in positions:
	x.append(dx)
	y.append(dy)

num_pos = len(x)
avg_pos = [sum(x)/num_pos, sum(y)/num_pos]
# print avg_pos



####
# The csv module (also standard library)
####

import csv

#with open('worm_data.csv', 'w') as file:
	
	## Create the writer (this is a simple interface for writing csv files)	
#	writer = csv.writer(file)

	## Write the header (not necessary but most csv have the column names in the first row)
#	writer.writerow( ('Index', 'Pos X', 'Pos Y', 'Orientation') )

	## Write the rest of the data
#	for i, pos, ori in data_set:
#		writer.writerow( (i, pos[0], pos[1], ori) )

# print open('worm_data.csv', 'rt').read()


####
# The math module
####

import math

## Constants
# print math.pi, math.e

## Trigonometry
#math.radians(), math.degrees()
#math.sin(), math.asin()
#math.cos(), math.acos()

#math.ceil()
#math.floor()

#math.sqrt()
#math.log()
#math.factorial()
