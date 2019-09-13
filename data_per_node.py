import random
from datetime import datetime
import csv

import os
import sys
import struct
import argparse
import datetime
import paho.mqtt.client as mqtt

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

    if node == "sb1":
        acc1 = sensor[:100]
        acc2 = sensor[100:]
        ane1 = sensor[-3]
        ane2 = sensor[-2]
        ane3 = sensor[-1]
        with open("csvfile/sb1.csv", "w") as csvfile:
            fields = ["node", "acc1", "acc2", "ane1", "ane2", "ane3", "timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            for i in range(len(acc1)):
                array = [{'node':node, 'acc1':acc1[i], 'acc2':acc2[i], 'ane1': ane1, 'ane2': ane2, 'ane3': ane3,'timestamp': timestamp}]
                print(array)
                writer.writerows(array)

    elif node == "sb2":
        acc1 = sensor[:100]
        acc2 = sensor[100:200]
        acc3 = sensor[200:]
        ane1 = sensor[-3]
        ane2 = sensor[-2]
        ane3 = sensor[-1]
        with open("csvfile/sb2.csv", "w") as csvfile:
            fields = ["node", "acc1", "acc2", "acc3", "ane1", "ane2", "ane3", "timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            for i in range(len(acc1)):
                array = [{'node':node, 'acc1':acc1[i], 'acc2':acc2[i], 'acc3': acc3[i], 'ane1': ane1, 'ane2': ane2, 'ane3': ane3,'timestamp': timestamp}]
                print(array)
                writer.writerows(array)

    elif node == "sb3":
        acc1 = sensor[:100]
        acc2 = sensor[100:200]
        with open("csvfile/sb3.csv", "w") as csvfile:
            fields = ["node", "acc1", "acc2", "timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            for i in range(len(acc1)):
                array = [{'node':node, 'acc1':acc1[i], 'acc2':acc2[i], 'timestamp': timestamp}]
                print(array)
                writer.writerows(array)

    elif node == "sb4":
        acc1 = sensor[:100]
        acc2 = sensor[100:200]
        with open("csvfile/sb4.csv", "w") as csvfile:
            fields = ["node", "acc1", "acc2", "timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            for i in range(len(acc1)):
                array = [{'node':node, 'acc1':acc1[i], 'acc2':acc2[i], 'timestamp': timestamp}]
                print(array)
                writer.writerows(array)

    elif node == "sb5":
        acc1 = sensor[:100]
        acc2 = sensor[100:200]
        with open("csvfile/sb5.csv", "w") as csvfile:
            fields = ["node", "acc1", "acc2", "timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            for i in range(len(acc1)):
                array = [{'node':node, 'acc1':acc1[i], 'acc2':acc2[i], 'timestamp': timestamp}]
                print(array)
                writer.writerows(array)

    elif node == "sb6":
        acc1 = sensor[:100]
        acc2 = sensor[100:200]
        with open("csvfile/sb6.csv", "w") as csvfile:
            fields = ["node", "acc1", "acc2", "timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            for i in range(len(acc1)):
                array = [{'node':node, 'acc1':acc1[i], 'acc2':acc2[i], 'timestamp': timestamp}]
                print(array)
                writer.writerows(array) 

    print('\n',node, timestamp, len(sensor), len(max_length), len(max_length)/8)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Melakukan koneksi ke Broker...")

client.connect("103.224.137.180", 9621)

client.username_pw_set('bams', 'bams.pwd')

client.loop_forever()

