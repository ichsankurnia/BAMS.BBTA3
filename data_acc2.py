import csv
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot

import random
from datetime import datetime

style.use('fivethirtyeight')
# plt.rcParams['animation.html'] = 'jshtml'

# Sent for figure
font = {'size'   : 9}
matplotlib.rc('font', **font)


fig = plt.figure(dpi=70, num="BAMS Data Accelerometer 2") # num = 2, figsize = (2, 3)
ax1 = fig.add_subplot(1,1,1)

array = []

node = ""
acc1, acc2, acc3, ane1, ane2, ane3 = [], [], [], [], [], []
timestamp = []
data_ke = []

def animate(i):
	with open("csvfile/file.csv", "r") as csvfile: #with untuk streaming file, secara otomatis akan close bersihin file saat ga di pake lagi
	    csvreader = csv.DictReader(csvfile)
	    array = list(csvreader)
	    # print("total baris : ", csvreader.line_num, "\n")

	for x in array:
	    node = x["node"]
	    timestamp = x["timestamp"]
	    if len(acc2) < 100:
	    	acc2.append(double(x["acc2"]))
	    	data_ke.append(i)	# nilai i dari function animate(i)
	    else:
	    	acc1[:-1] = acc1[1:]
	    	acc1[-1] = double(x["acc1"])

	    	data_ke[:-1] = data_ke[1:]
	    	data_ke[-1] = data_ke(i)

	
	print(node, timestamp)
	print(acc2)
	print(data_ke)

	ax1.clear()
	ax1.plot(data_ke, acc2)
	plt.ylabel('Accelerometer 2 (m/s^2)')
	plt.xlabel('Number Of Data')
	plt.title('Bridge Aeroelastic Monitoring System\nLive Data From Node : {}\n Timestamp: {}'.format(node, timestamp))

def show_data():
	ani=animation.FuncAnimation(fig, animate, interval=5000)
	plt.show()

if __name__ == '__main__':
	show_data()