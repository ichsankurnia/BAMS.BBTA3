import csv
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits.mplot3d import Axes3D

import random
from datetime import datetime

style.use('fivethirtyeight')
# plt.rcParams['animation.html'] = 'jshtml'

# Sent for figure
font = {'size'   : 9}
matplotlib.rc('font', **font)


fig = plt.figure(dpi=70, num="BAMS Data Accelerometer 1") # num = 2, figsize = (2, 3)
ax1 = fig.add_subplot(111)

# data = []

array = [] #array

node = ""
acc1, acc2, acc3, ane1, ane2, ane3 = [], [], [], [], [], []
timestamp = []
data_ke = []

# while 1:
def animate(i):
	with open("csvfile/file.csv", "r") as csvfile: #with untuk streaming file, secara otomatis akan close bersihin file saat ga di pake lagi
	    csvreader = csv.DictReader(csvfile) #bentuk dictionary
	    array = list(csvreader)

	for x in array:
	    node = x["node"]
	    timestamp = x["timestamp"]
	    if len(acc1) < 100:
	    	acc1.append(double(x["acc1"]))
	    	data_ke.append(i)	# nilai i dari function animate(i)
	    else:
	    	acc1[:-1] = acc1[1:]
	    	acc1[-1] = double(x["acc1"])

	    	data_ke[:-1] = data_ke[1:]
	    	data_ke[-1] = data_ke(i)


	print(node, timestamp)
	print(acc1)
	print(data_ke)
	# time.sleep(1)

	ax1.clear()
	# ax1.bar(timestamp, acc1)
	ax1.plot(data_ke, acc1)
	# ax1.scatter(timestamp, acc1)
	plt.ylabel('Accelerometer 1 (m/s^2)')
	plt.xlabel('Number Of Data')
	plt.title('Bridge Aeroelastic Monitoring System\nLive Data From Node : {}\n Timestamp: {}'.format(node, timestamp))

def show_data():
	ani=animation.FuncAnimation(fig, animate, interval=5000)
	plt.show()

if __name__ == '__main__':
	show_data()