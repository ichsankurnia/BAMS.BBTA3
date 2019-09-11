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

# while 1:
def animate(i):
	with open("file.csv", "r") as csvfile: #with untuk streaming file, secara otomatis akan close bersihin file saat ga di pake lagi
	    csvreader = csv.DictReader(csvfile) #bentuk dictionary
	    array = list(csvreader)
	    print("total baris : ", csvreader.line_num, "\n")

	for x in array:
	    node = x["node"]
	    if len(acc1) < 10:
	    	acc1.append(double(x["acc1"]))
	    	timestamp.append(x["timestamp"])
	    else:
	    	acc1[:-1] = acc1[1:]
	    	acc1[-1] = double(x["acc1"])

	    	timestamp[:-1] = timestamp[1:]
	    	timestamp[-1] = x["timestamp"]

	    print(node)

	print(timestamp)
	print(acc1)
	# time.sleep(1)

	ax1.clear()
	# ax1.bar(timestamp, acc1)
	ax1.plot(timestamp, acc1)
	# ax1.scatter(timestamp, acc1)
	plt.ylabel('Accelerometer 1 (m/s^2)')
	plt.xlabel('Timestamp (H:M:S)')
	plt.title('Bridge Aeroelastic Monitoring System\nLive Data From Node : {}'.format(node))

def show_data():
	ani=animation.FuncAnimation(fig, animate, interval=5000)
	plt.show()

if __name__ == '__main__':
	show_data()