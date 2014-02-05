#-------------------------------------------------
#
# Python Tutorial Session 5
# (c) Oliver Dressler, 2013
#
#-------------------------------------------------


####
# Basic matrix operations (as compared to MATLAB)
####

import numpy as np

## Creation: a = [1 2 3; 4 5 6]
a = np.array( [ [1, 2, 3], [3, 5, 6] ] )

## Range: b = [1 : 10]
b = np.arange(1, 11)
c = np.linspace(1, 10, 10) #Start, Stop (inclusive), Num Elements

## Reverse: c = reverse(b)
c = a[::-1]

## Transposition: c = a'
c = a.T

## Concatenation: c = [a a]
c = np.concatenate([a, a], axis = 0)

## Creation: c = zeros(3, 5)
size = (3, 5)
c = np.zeros(size)
c = np.ones(size)
c = np.empty(size)


## Indexing
## First Row: c = a(1, :)
c = a[0, :]

## Second Column: c = a(:, 2)
c = a[:, 1]

## Every Other Row: c = a(1:2:end, :)
c = a[::2, :]

## Size: c = size(a)
c = a.shape


####
# Data analysis (statistics)
####

a = np.array( [ [1, 2, 3], [3, 5, 6], [4, 5, 6], [7, 9, 8] ] )

## Unique values: unique(a)
# print np.unique(a)

## Mean: mean(a)
# print np.mean(a)

## Median: median(a)
# print np.median(a)

## Standard Deviation & Variance: std(a), var(a)
# print a.std(), a.var()

## Straight line: polyval(polyfir(x, y, 1), x)
x = a[:, 0]
y = a[:, 1]
# print np.polyfit(x, y, 1)

## Polynomial: polyfit(x, y, 3)
# print np.polyfit(x, y, 3)

## Fourrier transformation: fft(a)
# print np.fft.fft(a)


####
# Data Plotting
####


x = np.random.random( (100, 1) )
y = np.random.random( (100, 1) )

from matplotlib import pyplot as plt

## Scatter Plot
# plt.scatter(x, y)
# plt.show()

## Line Plot
# plt.plot(x, y)
# plt.show()

## Bar plot (use barh for horizontal bars)
dx = [1, 2, 3, 4]
dy = [10, 13, 8, 11]
# plt.bar(dx, dy)
# plt.show()

## Histogram
num_bins = 10
plt.hist(x, num_bins)
#plt.show()

## Save a figure: work with .jpg, .png, .svg, .eps, .pdf
plt.savefig('output.png')


####
# More Plot Examples
####

## Go to:
## http://matplotlib.org/gallery.html