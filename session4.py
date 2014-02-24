#-------------------------------------------------
#
# Python Tutorial Session 3
# (c) Oliver Dressler, 2013
#
#-------------------------------------------------


## It's not too late:
## STUDY PAST SESSIONS UNTIL YOU HAVE NO PROBLEMS SOLVING 3_D

# Feel free to contact me if you get stuck!
# Always remember: Google is your best friend...

# The next lesson is going to be the last general lesson.
# We have barely scratched the surface of Python but
# from now on we are going to look at specific applications of Python
# more or less in order of popularity in poll (image processing can be tricky):

# Plotting data																	7
# Interfacing with external devices (USB/Serial) 								8
# Image Processing																everyone
# Parallel code execution, parallel device control								7
# Advanced data handling: fft, interpolation, integration, clustering, ...		5

# I would recommend to come but the sessions are going to be independent.



##  FIND A PROJECT TO APPLY WHAT YOU HAVE LEARNED



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
## The input arguments are the arguments passed when initiating the instance
## self is mandatory (ignore it)

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

# print audi.color
audi.paint('silver')
# print audi.color

audi.color = 'black'
# print audi.color

## All of this has absolutely no effects on the ferrari
# print ferrari.current_speed, ferrari.color



## A microfluidics example (device control)
# Interface with several pumps in Python

# The serial connection is SIMULATED as a list
connection = []
# connection.append() means the command is sent to all devices

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

	def start(self):
		self.run_cmd('start')

	def stop(self):
		self.run_cmd('stop')


pump0 = Pump(0, connection)
pump0.run_cmd('start')

# print connection

pump1 = Pump(1, connection)

pump1.start()
pump1.stop()
pump0.stop()

# print connection

for i in range(10):
	pump1.start()
	pump1.stop()

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
papers = ['jc paper 1', 'jc paper 2', 'jc paper 3']
# print random.choice(papers)

## Make a random, weighted decision
# E.g. Do something in 33% of cases
if random.random() < 0.33:
	amount = random.randrange(50, 101)
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
	position = [ random.randrange(1, 11), random.randrange(1, 11) ]

	orientation = random.choice(directions)

	return index, position, orientation

# print create_random_worm_data()

# Create data set
data_set = [ create_random_worm_data() for i in range(1000000) ]
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
# The csv module (also standard library)
####

import csv
with open('worm_data.csv', 'w') as file:
	
	## Create the writer (this is a simple interface for writing csv files)	
	writer = csv.writer(file)

	## Write the header (not necessary but most csv have the column names in the first row)
	writer.writerow( ('Index', 'Pos X', 'Pos Y', 'Orientation') )

	## Write the rest of the data
	for index, pos, ori in data_set:
		writer.writerow( (index, pos[0], pos[1], ori) )

# print open('worm_data.csv', 'rt').read()