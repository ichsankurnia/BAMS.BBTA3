import time
import random
import matplotlib.pyplot as plt

plt.rcParams['animation.html'] = 'jshtml'

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()


i = 0
x = []
y = []

while True:
    x.append(i)
    y.append(random.randint(0,360))
    
    ax.plot(x, y, color='b')
    
    fig.canvas.draw()
    
    ax.set_xlim(left=max(0, i-10), right=i+10)
    
    time.sleep(0.1)
    i += 1

plt.close()