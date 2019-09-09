import time
import random

from datetime import datetime

data = []
timestamp = []

while 1:
    date = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")

    random_data = random.randint(0,1024)

    if len(data) < 6:
        data.append(random_data)
        timestamp.append(date)
    else:
        timestamp[:-1] = timestamp[1:]
        timestamp[-1] = date
        
        data[:-1] = data[1:]
        data[-1] = random_data

    print(data)
    print(timestamp)
    time.sleep(1)