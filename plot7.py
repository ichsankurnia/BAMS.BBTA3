# Uncomment the next two lines if you want to save the animation
#import matplotlib
#matplotlib.use("Agg")

import numpy
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.animation as animation

from matplotlib import style

import time
import random

from datetime import datetime

# style.use('fivethirtyeight')

# Sent for figure
font = {'size'   : 9}
matplotlib.rc('font', **font)

# Setup figure and subplots
f0 = figure(num = 0, figsize = (12, 8))#, dpi = 100)
f0.suptitle("Oscillation decay", fontsize=12)
ax01 = subplot2grid((2, 2), (0, 0))
ax02 = subplot2grid((2, 2), (0, 1))
ax03 = subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
ax04 = ax03.twinx()
#tight_layout()

data = []
data1 = []
data2 = []
timestamp = []

# Data Update
xmin = 0.0
xmax = 10
x = 0.0

# Turn on grids
ax01.grid(True)
ax02.grid(True)
ax03.grid(True)


def updateData(self):
	global x
	date = datetime.now().strftime("%M:%S")

	random_data = random.randint(0,1024)

	if len(data) < 5:
	    data.append(float(random_data))
	    data1.append(random.randint(0,360))
	    data2.append(random.randint(0,180))
	    timestamp.append(date)
	else:
	    timestamp[:-1] = timestamp[1:]
	    timestamp[-1] = date
	    
	    data[:-1] = data[1:]
	    data[-1] = random_data

	    data1[:-1] = data1[1:]
	    data1[-1] = random.randint(0,360)
	    data2[:-1] = data2[1:]
	    data2[-1] = random.randint(0,180)


	ax01.set_title('Accelerometer 1')
	ax02.set_title('Accelerometer 2')
	ax03.set_title('Accelerometer 3')


	# set label names
	ax01.set_xlabel("Timestamp")
	ax01.set_ylabel("Data Acc1")
	ax02.set_xlabel("Timestamp")
	ax02.set_ylabel("Data Acc2")
	ax03.set_xlabel("Timestamp")
	ax03.set_ylabel("Data Acc3")
	ax04.set_ylabel("vy")

	print(data)
	print(timestamp)

	# set plots
	p011, = ax01.plot(timestamp,data,'b-', label="yp1")
	p012, = ax01.plot(timestamp,data1,'g-', label="yp2")

	p021, = ax02.plot(timestamp,data,'b-', label="yv1")
	p022, = ax02.plot(timestamp,data2,'g-', label="yv2")

	p031, = ax03.plot(timestamp,data1,'b-', label="yp1")
	p032, = ax03.plot(timestamp,data2,'g-', label="yv1")

	# set lagends
	ax01.legend([p011,p012], [p011.get_label(),p012.get_label()])
	ax02.legend([p021,p022], [p021.get_label(),p022.get_label()])
	ax03.legend([p031,p032], [p031.get_label(),p032.get_label()])

	x += 0.05

	p011.set_data(timestamp,data)
	p012.set_data(timestamp,data1)

	p021.set_data(timestamp,data)
	p022.set_data(timestamp,data2)

	p031.set_data(timestamp,data1)
	p032.set_data(timestamp,data2)

	if x >= xmax-1.00:
		p011.axes.set_xlim(x-xmax+1.0,x+1.0)
		p021.axes.set_xlim(x-xmax+1.0,x+1.0)
		p031.axes.set_xlim(x-xmax+1.0,x+1.0)
		p032.axes.set_xlim(x-xmax+1.0,x+1.0)

	return p011, p012, p021, p022, p031, p032

# interval: draw new frame every 'interval' ms
# frames: number of frames to draw
# simulation = animation.FuncAnimation(f0, updateData, blit=False, frames=200, interval=20, repeat=True)
simulation = animation.FuncAnimation(f0, updateData, frames=10, interval=20, repeat=True)

# Uncomment the next line if you want to save the animation
#simulation.save(filename='sim.mp4',fps=30,dpi=300)

plt.show()