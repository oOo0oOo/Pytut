#-------------------------------------------------
#
# Python Tutorial Session 3
# (c) Oliver Dressler, 2013
#
#-------------------------------------------------


####
# Object-oriented programming (very superficial)
####

## Imagine a blueprint for a car (called a class in python)
## Each car has a color and a maximal speed

class Car:
	def __init__(self, color, max_speed):
		self.color = color
		self.max_speed = max_speed


## We can create a new car (instance of the class Car)
## The input arguments are the arguments passed, self is mandatory (ignore it)
audi = Car('silver', 150)
ferrari = Car('red', 250)


## We can access its elements
# print audi.color ## refers to self.color of the audi instance
# print ferrari.color, ferrari.max_speed
# print ferrari


## You can add functions that are generic for each car 
## but use the specific car parameters (e.g. accelerate)
## A function in a class is called a METHOD of this class

class BetterCar:
	def __init__(self, color, max_speed):
		self.color = color
		self.max_speed = max_speed

		# Current speed is always 0.0 in the beginning
		self.current_speed = 0.0

	def	accelerate(self, amount):
		self.current_speed += amount

		if self.current_speed > self.max_speed:
			self.current_speed = self.max_speed

	def paint(self, new_color):
		self.color = new_color


## An example
audi = BetterCar('black', 200)
ferrari = BetterCar('white', 300)

# print audi.current_speed
audi.accelerate(50)
audi.accelerate(-20)
# print audi.current_speed

audi.paint('silver')
# print audi.color

audi.color = 'black'
# print audi.color

## All of this has absolutely no effects on the ferrari
# print ferrari.current_speed, ferrari.color



## A microfluidics example (device control)
class Pump:
	def __init__(self, device_id, connection = []):
		self.device_id = device_id
		self.connection = connection

	def run_cmd(self, command):
		'''
			Template: /device_id/command/s
		'''
		cmd = '/{}/{}/s'.format(self.device_id, command)
		
		# Send over connection (append to connection list)
		self.connection.append(cmd)

	def pump(self):
		self.run_cmd('pump')

	def stop(self):
		self.run_cmd('stop')


# The serial connection is SIMULATED as a list
# list.append() means the command is sent to the devices

connection = []

pump0 = Pump(0, connection)
pump1 = Pump(1, connection)

pump1.pump()
pump0.pump()
pump1.stop()
pump0.stop()
pump1.pump()

# print connection



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
	position = [random.randrange(1, 11), random.randrange(1, 11)]

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

num_pos = float(len(x))
avg_pos = [sum(x)/num_pos, sum(y)/num_pos]
print avg_pos





####
# Prompting the user
####


# user_input = raw_input('What is the weather like?\n')
# print user_input, type(user_input)

## Take care when prompting other than string
# user_input = raw_input('What is the weather like? (1-10)\n')
# print int(user_input)




####
# Reading Data From File
####

file = open('s3_data.txt', 'r')

## This is the tricky part, a file always needs to be closed
## This is a problem, when an error happens (the program exits)
## before closing properly.
file.close()

## ALWAYS USE EITHER with 
with open('s3_data.txt', 'r') as file:
	# Do something with file
	pass


##OR try: finally: with files to make sure they close
file = open('s3_data.txt', 'r')
try:
	#do something with file
	pass

# File gets closed even if an error happens in do something
finally:
	file.close()



with open('s3_data.txt', 'r') as file:
	pass
	## Reading Complete file
	#complete_file = file.read()
	#print len(complete_file)

	## Reading Line by line
	#for line in file:
	#	if len(line) > 6:
	#		print line


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
angle = math.pi * 0.25
# print math.degrees(angle), math.radians(90)
# print math.sin(angle), math.asin(angle)
# print math.cos(angle), math.acos(angle)

## Other usefull stuff
# print math.ceil(1.0001), math.floor(9.9999)
# print math.sqrt(65536)
# print math.log(10), math.e ** math.log(10)
# print math.factorial(5)



####
# Special import statements
####

## Using code from another file
import session2
# print session2.addition(2, 3)

## Specific imports
from session2 import addition
# print addition(5, 6)

## Wildcard imports (do not use in final versions of program)
from math import *
# print floor(e)

## Changing names when importing
from session2 import addition as add
# print add(17, -11)