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

# Setup figure and subplots
# f0 = figure(num = 0, figsize = (12, 8))#, dpi = 100)
# f0.suptitle("Oscillation decay", fontsize=12)
# ax01 = subplot2grid((2, 2), (0, 0))
# ax02 = subplot2grid((2, 2), (0, 1))
# ax03 = subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)

fig = plt.figure(num = 2, figsize = (2, 3))
ax1 = fig.add_subplot(1,1,1)

data = []
timestamp = []

def animate(i):
    # graph_data = open('data.txt', 'r').read()
    # lines = graph_data.split('\n')
    # xs = []
    # ys = []

    # for line in lines:
    #     if len(line) > 1:
    #         x, y = line.split(',')
    #         xs.append(x)
    #         ys.append(float(y))

# while 1:
    # date = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    date = datetime.now().strftime("%M:%S")

    random_data = random.randint(0,1024)

    if len(data) < 20:
        data.append(float(random_data))
        timestamp.append(date)
    else:
        timestamp[:-1] = timestamp[1:]
        timestamp[-1] = date
        
        data[:-1] = data[1:]
        data[-1] = random_data

    print(data)
    print(timestamp)
    # time.sleep(1)

    ax1.clear()
    ax1.plot(timestamp, data)
    plt.ylabel('Random Data')
    plt.xlabel('Real-Time')
    plt.title('Live graph with matplotlib')

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

