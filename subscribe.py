import os
import sys
import struct
import argparse
import datetime
import paho.mqtt.client as mqtt


# Buat turunan dari class argument parser
parser = argparse.ArgumentParser(
    description='CLI untuk baca live data atau tambah data di database.')

# Tambah argument
parser.add_argument('-s',
                    metavar='status',
                    type=int,
                    help='''
                        Status atau kondisi; 0 -> live, 1 -> tambah, pilihan: 0. 
                        PERINGATAN: status 1 (tambah data) hanya dilakukan oleh SATU service agar data tidak konflik.
                    ''')

# Jalankan cli argument
args = parser.parse_args()


# Buat fungsi umpan balik ketika koneksi ke mqtt berhasil dilakukan.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # subscribe ke channel/topik saat on_connect()
    client.subscribe("BAMS")


# Buat fungsi umpan balik ketika PUBLISH MESSAGE diterima dari mqtt server.
def on_message(client, userdata, msg):
    # print("Connected with " + msg)
    n = 8  # pisah setiap 8 karakter
    node = msg.payload[0:3].decode('ascii')
    # timestamp = int(msg.payload[3:11], 16) * 1000  # dalam satuan ms
    timestamp = int(msg.payload[3:11], 16)  # dalam satuan ms
    timestamp = datetime.datetime.fromtimestamp(timestamp).isoformat()

    max_length=msg.payload[11:]

    acc1 = []
    acc2 = []
    acc3 = []
    ane1 = 0
    ane2 = 0
    ane3 = 0

    if args.s is None or args.s == 0:
        sensor = [struct.unpack('!f', bytes.fromhex(msg.payload[i:i+n].decode('ascii')))[0]
                  for i in range(11, len(msg.payload[11:]) + n, n)]

        if node == "sb1":
            acc = sensor[:-3]  # dalam bentuk List
            acc1 = sensor[:101]
            acc2 = sensor[101:201]
            ane1 = sensor[-3]  # dalam bentuk Scalar
            ane2 = sensor[-2]  # dalam bentuk Scalar
            ane3 = sensor[-1]  # dalam bentuk Scalar

        elif node == "sb2":
            acc = sensor[:-3]  # dalam bentuk List
            acc1 = sensor[:101]
            acc2 = sensor[101:201]
            acc3 = sensor[201:303]
            ane1 = sensor[-3]  # dalam bentuk Scalar
            ane2 = sensor[-2]  # dalam bentuk Scalar
            ane3 = sensor[-1]  # dalam bentuk Scalar

        else:
            acc = sensor  # dalam bentuk List
            acc1 = sensor[:101]
            acc2 = sensor[101:]
            # acc2 = sensor[101:201]
            # ane1 = 0  # dalam bentuk Scalar
            # ane2 = 0  # dalam bentuk Scalar
            # ane3 = 0  # dalam bentuk Scalar

        # print(acc)
        print(acc1)
        print(acc2)
        print(acc3)
        print(ane1)
        print(ane2)
        print(ane3)
        print(node, timestamp, len(sensor), len(max_length), len(max_length)/8, '\n')


if __name__ == "__main__":
    # Buat koneksi mqtt sebagai client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print("Melakukan koneksi ke Broker...")

    client.connect("103.224.137.180", 9621)

    try:
        # client.username_pw_set(os.getenv('bams'), os.getenv('bams.pwd'))
        client.username_pw_set('bams', 'bams.pwd')
    except KeyError:
        print('Silahkan tambah env. untuk MQ_USER dan/atau MQ_PWD')
        sys.exit()

    client.loop_forever()
