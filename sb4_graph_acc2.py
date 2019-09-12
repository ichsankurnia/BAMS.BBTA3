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


fig = plt.figure(dpi=80, num="BAMS Data Accelerometer 2") # num = 2, figsize = (2, 3)
ax1 = fig.add_subplot(111)

array = [] #array

def animate(i):
	node = ""
	acc1, acc2 = [], []
	timestamp = []
	data = []
	with open("csvfile/sb4.csv", "r") as csvfile: #with untuk streaming file, secara otomatis akan close bersihin file saat ga di pake lagi
	    csvreader = csv.DictReader(csvfile) #bentuk dictionary
	    array = list(csvreader)
	    print("total baris : ", csvreader.line_num, "\n")

	for x in array:
		node = x["node"]
		acc2.append(double(x["acc2"]))
		timestamp = x["timestamp"]

	if len(data) < 100:
		for i in range(100):
			# acc1.append(random.randint(0,10))
			data.append(i)
	else:
		data = []
		# acc2 = []
		for i in range(100):
			# acc2.append(random.randint(0,10))
			data.append(i)

	print(node)

	print(timestamp)
	print(acc2)
	print("Length Times",len(timestamp))
	print("Length Acc2", len(acc2))
	print("Jumlah data", len(data))
	time.sleep(1)

	ax1.clear()
	# ax1.bar(timestamp, acc2)
	ax1.plot(data, acc2)
	# ax1.scatter(timestamp, acc2)
	plt.ylabel('Accelerometer 2 (m/s^2)')
	plt.xlabel('Number Of Data')
	plt.title('Bridge Aeroelastic Monitoring System\nLive Data From Node : {}\n Timestamp: {}'.format(node, timestamp))

def show_data():
	ani=animation.FuncAnimation(fig, animate, interval=5000)
	plt.show()

if __name__ == '__main__':
	show_data()