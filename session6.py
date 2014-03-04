#-------------------------------------------------
#
# Python Tutorial Session 6
# (c) Oliver Dressler, 2014
#
#-------------------------------------------------



####
# To manage the serial connection you need the pyserial module
# Windows; download installer from: https://pypi.python.org/pypi/pyserial
# Mac (with pip installed): "sudo pip install pyserial" in terminal
# 		If you dont have pip do "sudo easy_install pip" first
####


####
# Solenoid Valve Control
####

import time
from serial import Serial
from struct import pack


def prepare_controller(port = 'COM5'):
	## To open a new serial connection we have to know the port
	## our device is connected to...
	connection = Serial(port)


	## how does a command for the controller look like:
	## pack creates a string with all arguments packed as
	## specified using the first argument ('B' in this case means Byte)
	cmd  = pack('B', 1)
	# print repr(cmd), cmd
 
 
	## This command puts all pins in output mode
	## Now we just need to send it to the connected controller
	connection.write(cmd)


	## Now we have to put all the pins in output mode
	for port in ['A', 'B', 'C']:
		cmd = pack('ccB', '!', port, 0)
		connection.write(cmd)

	return connection



# connection = prepare_controller()



## To adress individual pins the controller uses a numbering system
## Here is a translation function
def get_pin_num(port, pin):
	''' 
		Pin can be 1-8, port can be A, B or C.
		Pins on port A are numbered 0-7, B are 8-15 and C are 16-23
	'''
	if port not in ('A', 'B', 'C') or pin not in range(1, 9):
		raise Exception('Invalid Port or Pin...')

	if port == 'A': num = 0
	elif port == 'B': num = 8
	elif port == 'C': num = 16
	return num + (pin - 1)

# print get_pin_num('A', 1), get_pin_num('B', 1), get_pin_num('C', 8)


## Two functions to turn pin high (activate valve) or low
def set_pin_high(port, pin):
	## Construct command
	cmd = pack('cB', 'H', get_pin_num(port, pin))
	# print cmd, repr(cmd)
	connection.write(cmd)

def set_pin_low(port, pin):
	## Construct command
	cmd = pack('cB', 'L', get_pin_num(port, pin))
	# print cmd, repr(cmd)
	connection.write(cmd)


for i in xrange(10):
	# set_pin_high('A', 1)
	time.sleep(0.025)
	# set_pin_low('A', 1)
	time.sleep(0.025)


## Always close a serial connection when you're done
# connection.close()




####
# Controlling a continuous pump
####

class MilliGAT:

	'''
	This is a very simple controller class for a milliGAT low flow pump.
	It enables pumping at constant speed and stopping flow (pumping at speed 0).
	
	A list of all commands is available from (page 42):
	http://www.globalfia.com/index.php?option=com_docman&task=doc_download&gid=8&Itemid=48

	This example only implements the slew command and is able to read a response from the device.

    '''

	def __init__(self, serial_connection, adress):
		'''
		serial connection: is the serial connection used to transmit the commands
		adress: is the specific adress of the pump (daisy chained)
		'''
		self.ser = ser
		self.adress = adress

	def read_response(self):
		'''
		Wait 50 ms then read response from device.
		'''
		resp = ''
		time.sleep(0.05)
		while self.ser.inWaiting() > 0:
			resp += self.ser.read(1)
		return resp

	def slew(self, pump_rate):
		'''
		Start pumping at constant rate [ul/min].
		'''
		# convert from ul/min to microsteps/
		pump_rate = int(round(pump_rate * 2432/60))

		# set pump rate
		command = self.adress + 'SL=' + str(pump_rate) + '\r\n'
		# print command

		# Execute the command (send over serial connection)
		self.ser.write(command)

		resp = self.read_response()
		# print resp

	def stop(self):
		'''
		Stop the pump.
		'''
		self.slew(0)


## A simple example:
# Initialize connection and pump
'''
connection = Serial('COM5')
pump = MilliGAT(connection, 'A')

# Pump at 50 ul/min for 10 s
pump.slew(50)
time.sleep(10)
pump.stop()
'''

# Check if we still have an open connection:
# the close...
try:
	connection.close()
except Exception:
	pass