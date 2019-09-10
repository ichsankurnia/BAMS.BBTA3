import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import time
import random

from datetime import datetime

style.use('fivethirtyeight')

fig = plt.figure()
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

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.ylabel('Random Data')
plt.xlabel('Real-Time')
plt.show()