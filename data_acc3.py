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


fig = plt.figure(dpi=70, num="BAMS Data Accelerometer 3") # num = 2, figsize = (2, 3)
ax1 = fig.add_subplot(1,1,1)

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
	    if len(acc3) < 10:
	    	acc3.append(double(x["acc3"]))
	    	timestamp.append(x["timestamp"])
	    else:
	    	acc3[:-1] = acc3[1:]
	    	acc3[-1] = double(x["acc3"])

	    	timestamp[:-1] = timestamp[1:]
	    	timestamp[-1] = x["timestamp"]

	    print(node)

	print(timestamp)
	print(acc3)
	# time.sleep(1)

	ax1.clear()
	ax1.plot(timestamp, acc3)
	plt.ylabel('Accelerometer 3 (m/s^2)')
	plt.xlabel('Timestamp (H:M:S)')
	plt.title('Bridge Aeroelastic Monitoring System\nLive Data Accelerometer 3 From Node : {}'.format(node))

def show_data():
	ani=animation.FuncAnimation(fig, animate, interval=5000)
	plt.show()

if __name__ == '__main__':
	show_data()

