import random
from datetime import datetime
import csv

import os
import sys
import struct
import argparse
import datetime
import paho.mqtt.client as mqtt


times = []
acc1 = []
acc2 = []
acc3 = []
ane1 = []
ane2 = []
ane3 = []
node = ""

# Buat fungsi umpan balik ketika koneksi ke mqtt berhasil dilakukan.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # subscribe ke channel/topik saat on_connect()
    client.subscribe("BAMS")


# Buat fungsi umpan balik ketika PUBLISH MESSAGE diterima dari mqtt server.


def on_message(client, userdata, msg):

    n = 8  # pisah setiap 8 karakter
    node = msg.payload[0:3].decode('ascii')
    timestamp = datetime.datetime.now() - datetime.timedelta(seconds=3)
    timestamp = timestamp.strftime("%H:%M:%S")

    max_length=msg.payload[11:]

    sensor = [struct.unpack('!f', bytes.fromhex(msg.payload[i:i+n].decode('ascii')))[0]
              for i in range(11, len(msg.payload[11:]) + n, n)]

    if node == "sb1":
        array = [{"node" : node, "acc1" : sensor[80], "acc2" : sensor[180], "acc3" : 0, "ane1" : sensor[-2], "ane2" : sensor[-3], "ane3" : sensor[-1], "timestamp" : timestamp},]
    elif node == "sb2":
        array = [{"node" : node, "acc1" : sensor[80], "acc2" : sensor[180], "acc3" : sensor[280], "ane1" : sensor[-2], "ane2" : sensor[-3], "ane3" : sensor[-1], "timestamp" : timestamp},]
    else:
        array = [{"node" : node, "acc1" : sensor[80], "acc2" : sensor[180], "acc3" : 0, "ane1" : 0, "ane2" : 0, "ane3" : 0, "timestamp" : timestamp},]
    
    if len(times) < 5:
        if node == "sb1":
            acc1.append(sensor[80])
            acc2.append(sensor[180])
            acc3.append(0)
            ane1.append(sensor[-3])
            ane2.append(sensor[-2])
            ane3.append(sensor[-1])
            times.append(timestamp)
        elif node == "sb2":
            acc1.append(sensor[80])
            acc2.append(sensor[180])
            acc3.append(sensor[280])
            ane1.append(sensor[-3])
            ane2.append(sensor[-2])
            ane3.append(sensor[-1])
            times.append(timestamp)
        else:
            acc1.append(sensor[80])
            acc2.append(sensor[180])
            acc3.append(0)
            ane1.append(0)
            ane2.append(0)
            ane3.append(0)
            times.append(timestamp)
    else:
        if node == "sb1":
            acc1[:-1] = acc1[1:]
            acc1[-1] = sensor[80]

            acc2[:-1] = acc2[1:]
            acc2[-1] = sensor[180]

            acc3[:-1] = acc3[1:]
            acc3[-1] = 0

            ane1[:-1] = ane1[1:]
            ane1[-1] = sensor[-3]

            ane2[:-1] = ane2[1:]
            ane2[-1] = sensor[-2]

            ane3[:-1] = ane3[1:]
            ane3[-1] = sensor[-1]

            times[:-1] = times[1:]
            times[-1] = timestamp

        elif node == "sb2":
            acc1[:-1] = acc1[1:]
            acc1[-1] = sensor[80]

            acc2[:-1] = acc2[1:]
            acc2[-1] = sensor[180]

            acc3[:-1] = acc3[1:]
            acc3[-1] = sensor[280]

            ane1[:-1] = ane1[1:]
            ane1[-1] = sensor[-3]

            ane2[:-1] = ane2[1:]
            ane2[-1] = sensor[-2]

            ane3[:-1] = ane3[1:]
            ane3[-1] = sensor[-1]

            times[:-1] = times[1:]
            times[-1] = timestamp
        else:
            acc1[:-1] = acc1[1:]
            acc1[-1] = sensor[80]

            acc2[:-1] = acc2[1:]
            acc2[-1] = sensor[180]

            acc3[:-1] = acc3[1:]
            acc3[-1] = 0

            ane1[:-1] = ane1[1:]
            ane1[-1] = 0

            ane2[:-1] = ane2[1:]
            ane2[-1] = 0

            ane3[:-1] = ane3[1:]
            ane3[-1] = 0

            times[:-1] = times[1:]
            times[-1] = timestamp

    # print(sensor)

    print('\n',node, timestamp, len(sensor), len(max_length), len(max_length)/8)
    # print(sensor)
    print(acc1)
    print(acc2)
    print(acc3)
    print(ane1)
    print(ane2)
    print(ane3)
    print(times)

    """Menulis File CSV pada python"""

    # array = [{"node" : node, "acc1" : sensor[80], "acc2" : sensor[180], "acc3" : sensor[280], "ane1" : sensor[-2], "ane2" : sensor[-3], "ane3" : sensor[-1], "timestamp" : timestamp},]

    with open("file.csv", "w") as csvfile:
            fields = ["node", "acc1", "acc2", "acc3", "ane1", "ane2", "ane3", "timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames = fields)

            writer.writeheader()
            writer.writerows(array)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Melakukan koneksi ke Broker...")

client.connect("103.224.137.180", 9621)

client.username_pw_set('bams', 'bams.pwd')

client.loop_forever()

