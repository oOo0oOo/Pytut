#-------------------------------------------------
#
# Python Tutorial Session 9
# (c) Oliver Dressler, 2014
#
#-------------------------------------------------

## Todays lesson is heavily based on:
# http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-3-Scipy.ipynb


## Optimization (find minima or maxima of a function)

from scipy import optimize
from matplotlib import pyplot as plt
import numpy as np


# A simple function
def f(x):
	return 4*x**3 + (x-2)**2 + x**4


# Plotting the function
# fig, ax  = plt.subplots()
x = np.linspace(-5, 3, 100)
# ax.plot(x, f(x))


# Calculate the minimum y value
result = optimize.minimize(f, -2)
# Retrieve the x coordinate (there are a lot more results available)
x_min = result.x[0]
# ax.plot((x_min, x_min), (-50, 50), color = 'r')



## Interpolation

from scipy.interpolate import *

# create some noisy sine data
def f(x):
    return np.sin(x)

n = np.arange(0, 10)  
x = np.linspace(0, 9, 100)

y_meas = f(n) + 0.1 * np.random.randn(len(n)) # simulate measurement with noise
y_real = f(x)


# Some interpolations
linear_interpolation = interp1d(n, y_meas)
y_interp1 = linear_interpolation(x)

cubic_interpolation = interp1d(n, y_meas, kind='cubic')
y_interp2 = cubic_interpolation(x)

# Plot the stuff
# fig, ax = plt.subplots(figsize=(10,4))

# ax.plot(n, y_meas, 'bs', label='noisy data')
# ax.plot(x, y_real, 'k', lw=2, label='true function')
# ax.plot(x, y_interp1, 'r', label='linear interp')
# ax.plot(x, y_interp2, 'g', label='cubic interp')

# ax.legend(loc=3)



## Statistics (Poisson)

from scipy import stats

# create a (discreet) random variable with poissionian distribution
n = np.arange(0,15)

# fig, ax = plt.subplots()

for i in range(4):
	# encapsulation probability with max at 1 - 4
	X = stats.poisson(i+1) 

	# plot the probability mass function (PMF)
	# ax.step(n, X.pmf(n), lw=3)

# ax.set_title('Poisson Distributions for Different Max')
# ax.legend([str(i) for i in range(1, 5)])



## Lets do some poisson math: Co-encapsulate two cells
## Probability = prob_first(1) * prob_second(1)
poiss = stats.poisson(1)
prob = poiss.pmf(1) * poiss.pmf(1)
# print 'Percentage of perfect co-encapsulation: {}%'.format(round(prob * 100,2))


## Now lets calculate all possibilities of co-encapsulation up to three
optimal = [stats.poisson(i).pmf(i) for i in range(1,5)]

results = []
for cell1 in range(4):
	row = []
	for cell2 in range(4):
		row.append(optimal[cell1] * optimal[cell2])

	results.append(row)

# print results
results = np.array(results)


## Plot a heatmap
'''
fig, ax = plt.subplots()
heatmap = ax.pcolor(results, cmap=plt.cm.Blues)

# Fix the labels
ax.set_xticks([0.5, 1.5, 2.5, 3.5])
ax.set_yticks([0.5, 1.5, 2.5, 3.5])
ax.set_xticklabels([str(i) for i in range(1, 5)])
ax.set_yticklabels([str(i) for i in range(1, 5)])

# fig.colorbar(heatmap)
ax.set_title('Percentage of perfect co-encapsulations')
'''



## Fitting a distribution
from scipy.stats import norm, expon, uniform

# Here is some normal distributed data data
data = norm.rvs(10.0, 2.5, size=500)
# print data

# Fit a normal distribution to the data
mu, std = norm.fit(data)

# print mu, std, data.mean(), data.std()

## Plot the histogram and fit
# fig, ax = plt.subplots()
# ax.hist(data, bins=25, normed=True, alpha=0.6, color='g')

# Plot the PDF
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

p = norm.pdf(x, mu, std)
# ax.plot(x, p, 'k', linewidth=2)



## A simple T-test (for two independent samples)
# (e.g. Girls and boys taking the same test)

from scipy.stats import ttest_ind

t_statistic, p_value = stats.ttest_ind(norm.rvs(10.0, 1.0, size=200), norm.rvs(10.0, 1.0, size=200))

# Null hypothesis: two samples have the same mean (rejected if small p-value)
# print "p-value =", p_value


plt.show()