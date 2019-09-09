import time
import random

from datetime import datetime

data = []
timestamp = []

while 1:
    tanggal = datetime.now().strftime("%Y-%m-%d")
    jam = datetime.now().strftime("%H:%M:%S")
    waktu = tanggal + "/" + jam

    random_data = random.randint(0,1024)
    if len(data) < 6:
        data.append(random_data)
        timestamp.append(waktu)
    else:
        timestamp[:-1] = timestamp[1:]
        timestamp[-1] = waktu
        data[:-1] = data[1:]
        data[-1] = random_data

    print(data)
    print(timestamp)
    time.sleep(1)