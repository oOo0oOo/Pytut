#-------------------------------------------------
#
# Python Tutorial Session 10
# (c) Oliver Dressler, 2014
#
# Quantifying cell ordering
#
#-------------------------------------------------

from SimpleCV import VirtualCamera
from matplotlib import pyplot as plt
import time

PATH = '60ul_center.avi'

# We will load the video using the VirtualCamera from simplecv
video = VirtualCamera(PATH, 'video')
# video.getImage().show() ; time.sleep(10)

# Calculate average of first 100 frames
def average_image(video, num_frames = 100):
	avg = video.getImage()
	for i in range(num_frames - 1):
		# Some kind of running average
		avg = (avg + video.getImage()) / 2
	return avg

avg = average_image(video)
# avg.show() ; time.sleep(10)


# Open video again to be able to analyze full video
video = VirtualCamera(PATH, 'video')


# Loop over each frame to find cells
area, position = [], []

before = time.time()
for i in range(1000):
	# get image
	img = video.getImage()# ; img.show(); time.sleep(1)
	
	# subtract background (throws an error if no frames are left)
	try:
		img = img - avg
	except TypeError:
		break

	# use the oldschool threshold
	img = img.threshold(5)#; img.show(); time.sleep(1)

	# Extract blobs (cells)
	blobs = img.findBlobs(minsize = 100)

	if blobs:
		# blobs.show(); time.sleep(3)
		for b in blobs:
			area.append( b.area() )
			position.append( b.centroid() )


# Analyze the processing time
t = float(time.time() - before)
# print 'Processed {} frames @ {} frames/s, found {} cells.'.format(i, round(i/t,1), len(area))



## Plotting

# Cell Size Histogram
fig, ax = plt.subplots()
ax.hist(area)
ax.set_title('Extracted Cell Areas')
ax.set_ylabel('Cell Count')
ax.set_xlabel('Cell Area [px^2]')


# Cell Position Scatterplot
fig, axes = plt.subplots(3)
x, y = [p[0] for p in position], [p[1] for p in position]

axes[0].scatter(x, y)
axes[0].set_title('Cell Positions')

axes[1].hist(x, bins = 50)
axes[1].set_title('X Histogram')

axes[2].hist(y, bins = 50)
axes[2].set_title('Y Histogram')



# Does cell size affect y position
fig, ax = plt.subplots()
ax.scatter(area, y)
ax.set_ylabel('Y Position')
ax.set_xlabel('Cell Size')
ax.set_title('Cell Size vs. Y Position')




## Analyze (II): Is up and down equally distributed

middle = (max(y) - min(y)) / 2
top = [y_i for y_i in y if y_i > middle]
percentage = round( 100. * len(top) / len(y) , 1)
# print '{} % of the cells are on the top of the channel.'.format(percentage)


## Analyze (III): Check for cell packets
## Very simple: check how many times the side flips
flips = 0
is_top = False
for y_i in y:
	if (y_i < middle and is_top) or (y_i > middle and not is_top):
		flips += 1
		is_top = not is_top

# print 'Identified {} flips. On average {} cells per packet.'.format(flips, round( len(y)/ float(flips), 1) )


## Analyze (IV): Statistics
from scipy.stats import ttest_ind, ks_2samp

# Fit the normal distributions
bottom = [y_i for y_i in y if y_i < middle]

# Check whether the two means are independent
_, p_ind = ttest_ind(top, bottom)
# print 'P-val (independence of means):', p_ind

# Check each mean if value is acceptable
_, p_same_dist = ks_2samp(top, bottom)
# print 'P-val for Kolmogorov-Smirnov (values from same continuous distribution):', p_same_dist


# plt.show()