#-------------------------------------------------
#
# Python Tutorial Session 11
# (c) Oliver Dressler, 2014
#
# GUI & User Interaction
#
#-------------------------------------------------


## Simple Commandline interface

# Ask for an input from the user
'''
answer = raw_input('End program (y/N): ')

# Check if input fulfills criterion
if answer in ('y', 'Y'):
	# end program
	import sys
	sys.exit()



## Repeatedly query an input
stopped = False

# Endless loop
while True:
	# Get input
	next_key = raw_input('Input: ')

	# If no key: end endless loop
	if next_key == '':
		break

	# Else ECHO
	print 'Output: ' + next_key.upper()

'''


## Graphical user interface: external library guidata

# Imports and necessary boilerplate
import guidata
_app = guidata.qapplication()

from guidata.dataset.datatypes import DataSet
import guidata.dataset.dataitems as di



'''
# We are creating a class by inheriting from another class
# Just ignore this for now...
class ChocolateGUI(DataSet):
	"""A Simple GUI"""
	# now we can define the different parameters we want to
	like = di.BoolItem('Do you like chocolate?')
	amount = di.IntItem('How much?', min=0, max=10)

choco = ChocolateGUI()
choco.edit()

print 'Like: {}, Amount: {}'.format(choco.like, choco.amount)
'''

'''
class DataEvaluation(DataSet):
	"""Data Evaluation Parameters"""
	# now we can define the different parameters we want to
	
	file_path = di.FileOpenItem('Video File')
	num_frames = di.IntItem('Num Frames', min=0, max=1000, default=1000)
	processing = di.ChoiceItem('Pre-processing',
                         ('None', 'Erode', 'Morph Gradient'))
	threshold = di.FloatItem('Threshold', min=0, max=255, default = 50.0)
	use_filter = di.BoolItem('Use Filter')


param = DataEvaluation()

# you can also change the items 
param.use_filter = True
param.edit()

print 'Loading {} frames from: {}'.format(param.num_frames, param.file_path)
print 'Pre-Processing Option: {} --> Thresholding: {} --> Filter: {}'.format(
	param.processing, param.threshold, param.use_filter)

'''

'''

## Our last bit of Python: acessing the web, libraries

from urllib import urlopen, urlencode # get the data
import json # transform the data into python dictionary
from pprint import pprint


#  Construct the url
url = 'http://online.fahrplan.zvv.ch//bin/stboard.exe/dn?requestType=0&start=yes&L=vs_widgets&maxJourneys=10&'
url += urlencode({'input': 'Zuerich, ETH Hoenggerberg'})
# print url


# Get the data form the web
timetableData = urlopen(url)
try:
	timetableDataString = timetableData.read().decode(encoding='UTF-8')
except UnicodeDecodeError:
	print 'Did not receive expected json data from api. (DecodeError)'

timetableDataStringTrunc = timetableDataString[14:]


# Convert data to dictionary
data = json.loads(timetableDataStringTrunc)


# Annoying but necessary to clean up the data
def clean_str(input):
	t = repr(input)[2:-1]
	t = t.replace('\\xfc', 'ue')
	t = t.replace('\\xf6', 'oe')
	t = t.replace('\\xe4', 'ae')
	return t

# Print all the data nicely
for j in data['journey']:
	print 'Line {} to {} in {} minutes'.format(j['pr'],
		clean_str(j['st']), j['countdown_val'])

'''