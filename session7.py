#-------------------------------------------------
#
# Python Tutorial Session 7
# (c) Oliver Dressler, 2014
#
#-------------------------------------------------

import time

## Image Processing (just a quick look)

from SimpleCV import Image


## Load an image from a filepath
## (Hong, deMello (2010): http://iopscience.iop.org/1748-605X/5/2/021001/fulltext/)
droplets = Image('data_s7.jpg')

## Once you have an image you can do a ton of stuff!
## URL (official documentation) about available methods: 
## http://simplecv.org/docs/SimpleCV.html#i/SimpleCV.ImageClass.Image


## Display the image & the image size
# droplets.show()
# time.sleep(5)
img_size = droplets.size()
# print 'Image size:', img_size


## Convert to black and white (applying a simple threshold value)
droplets = droplets.threshold(75)
# droplets.show()
# time.sleep(5)


## Cropping the image into the four pieces
## The x coords are always the whole size
x = 55
segment_height = img_size[1]/4
y_coords = [i * segment_height for i in range(4)]
# print segment_height, y_coords

avg_sizes = []

for y in y_coords:
	
	## Crop the image (x, y, width, height)
	channel = droplets.crop(x, y, img_size[0], segment_height)
	# channel.show()

	## Find droplets (blobs of color)
	blobs = channel.findBlobs()
	
	## If blobs found
	if blobs:
		## Keep only reasonably sized blobs
		blobs = [b for b in blobs if b.area() < 1000]

		## Get the coordinates of each blob if it is reasonably sized
		points = [b.coordinates() for b in blobs]

		## Draw the center point
		channel.drawPoints(points, color=(255, 0, 0), sz=3, width=-1)

		## Number of droplets and average droplet area
		areas = [b.area() for b in blobs]
		num = len(areas)
		avg =  int( sum(areas)/num )

		avg_sizes.append(avg)
		# print 'Average droplet area ({} droplets): {} px^2'.format(num, avg)

	# channel.show()
	# time.sleep(5)


## Correlate with flow rate ratios (found in paper)
ratios = [2, 3, 4, 5]

## Make a nice scatter plot
from matplotlib import pyplot as plt
plt.scatter(ratios, avg_sizes)
# And add some axis label
plt.xlabel('Oil/Water (Water fixed at 5 ul/min)')
plt.ylabel('Avg Area [px^2]')
# plt.show()