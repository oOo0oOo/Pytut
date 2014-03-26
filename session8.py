#-------------------------------------------------
#
# Python Tutorial Session 8
# (c) Oliver Dressler, 2014
#
# ANOTHER COMPLETE WORKFLOW (RECAP)
#
#-------------------------------------------------


import csv
import numpy as np
from matplotlib import pyplot as plt

####
# Loading Data
####

## Load all values from a single column in a csv file into a Python list
filepath = 'example_s8.csv'
data = []

# Open the file
with open(filepath, 'rb') as file:

	# Wrap the file in a reader object
	reader = csv.reader(file)

	# Discard the first row (contains column labels)
	unused_row = reader.next()

	# Loop through all the rows
	for row in reader:

		# convert the entry in the second column into an integer
		value = int(row[1])

		# Append to list
		data.append(value)

# print data


## Getting all values; in short (feels a bit like a maze)
## USE THIS (if you think you will still get it a few months from now)...
with open('example_s8.csv', 'rb') as file:
	data = [ [int(r) for r in row] for row in list(csv.reader(file)) [1:] ]

# print data[0], data[-1]



####
# Basic Data Analysis (mean, std, selecting data)
####

# We are going to use numpy for this, here's the ubiquitous ndarray
data = np.array(data)

# The average of all areas (second column) or x positions (third column)
avg_area = data[:, 1].mean()
avg_x = data[:, 2].mean()

# print 'Average Area:', round(avg_area, 1), '+-', data[:, 2].std()

# Lets sort the data a bit we will only consider "front" cells
# (cells that are on the right of the average x position)

# np.where return the indices of all rows fullfilling the condition
rows = np.where(data[:,2] > 512)
# print rows

# Now we can select only these rows from the matrix
front_cells = data[rows, :]
# print front_cells
# print front_cells[:, 2].mean(), 'Variance:', front_cells[:, 2].var()

# A linear fit through the cell positions, 
# to check how they are focussed along the channel
params = np.polyfit(data[:,2], data[:,3], 1, full = True)
coeff, r_val = params[0], params[1]
# print 'Intercept: {}, Slope: {}, R-squared: {}'.format(coeff[1], coeff[0], r_val[0])



####
# Plotting the results
####

# First a scatter plot of all positions
# plt.scatter(data[:,2], data[:,3], color = 'b')

# Add the line fit
x = np.linspace(0, 1024, 100)
polynomial = np.poly1d(coeff)
y = polynomial(x)
# plt.plot(x, y, 'r')



####
# Moving average using numpy
####

# Sort cells according to x position, then collect y positions
# googled: http://stackoverflow.com/questions/2828059/sorting-arrays-in-numpy-by-column
sorted_data = data[data[:,2].argsort()]
x_sorted = sorted_data[:,2]
y_sorted = sorted_data[:,3]

# Moving Average (window size) 
# (googled: http://stackoverflow.com/questions/13728392/moving-average-or-running-mean)
def moving_avg(values, N):
	return np.convolve(values, np.ones((N,))/N)[(N-1):-N+1]

# We will use a new figure to display the results
# plt.figure()
x = range(len(y_sorted))
# plt.plot(moving_avg(x_sorted, 10), moving_avg(y_sorted, 10), 'r')
# plt.plot(moving_avg(x_sorted, 50), moving_avg(y_sorted, 50), color = 'green')
# plt.plot(moving_avg(x_sorted, 150), moving_avg(y_sorted, 150), color = 'orange')

# Add a title and a legend
# plt.title('Running Average Window Sizes')
# plt.legend(['10', '50', '150'])


## Now a moving average for the area
# plt.figure()
x_avg = moving_avg(sorted_data[:, 2], 10)
area_avg = moving_avg(sorted_data[:,1], 10)
# plt.plot(x_avg, area_avg)


plt.show()
