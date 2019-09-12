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


def on_message(client, userdata, msg):

    n = 8  # pisah setiap 8 karakter
    node = msg.payload[0:3].decode('ascii')
    # timestamp = int(msg.payload[3:11], 16)  # dalam satuan ms
    # timestamp = datetime.datetime.fromtimestamp(timestamp).isoformat()
    timestamp = datetime.datetime.now() - datetime.timedelta(seconds=1)
    timestamp = timestamp.strftime("%H:%M:%S")

    max_length=msg.payload[11:]

    sensor = [struct.unpack('!f', bytes.fromhex(msg.payload[i:i+n].decode('ascii')))[0]
              for i in range(11, len(msg.payload[11:]) + n, n)]

    array = []
    if node == "sb4":
        sb4_acc1 = sensor[:100]
        sb4_acc2 = sensor[100:]
        with open("sb4.csv", "w") as csvfile:
            fields = ["node", "acc1", "acc2", "timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            for i in range(len(sb4_acc2)):
                array = [{'node':node, 'acc1':sb4_acc1[i], 'acc2':sb4_acc2[i], 'timestamp': timestamp}]
                print(array)
                writer.writerows(array)

        if len(times) < 5:
            acc1.append(sensor[99])
            acc2.append(sensor[180])
            times.append(timestamp)
        else:
            acc1[:-1] = acc1[1:]
            acc1[-1] = sensor[99]

            acc2[:-1] = acc2[1:]
            acc2[-1] = sensor[180]

            times[:-1] = times[1:]
            times[-1] = timestamp

       

    print('\n',node, timestamp, len(sensor), len(max_length), len(max_length)/8)
    # print(sensor)
    print(acc1)
    print(acc2)
    print(times)
    print(sensor[:100])


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Melakukan koneksi ke Broker...")

client.connect("103.224.137.180", 9621)

client.username_pw_set('bams', 'bams.pwd')

client.loop_forever()

