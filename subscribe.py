import os
import sys
import struct
import argparse
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
    n = 8  # pisah setiap 8 karakter
    node = msg.payload[0:3].decode('ascii')
    timestamp = int(msg.payload[3:11], 16) * 1000  # dalam satuan ms

    if args.s is None or args.s == 0:
        sensor = [struct.unpack('!f', bytes.fromhex(msg.payload[i:i+n].decode('ascii')))[0]
                  for i in range(11, len(msg.payload[11:]) + n, n)]

        if node == "sb1" or node == "sb2":
            acc = sensor[:-3]  # dalam bentuk List
            ane1 = sensor[-1]  # dalam bentuk Scalar
            ane2 = sensor[-2]  # dalam bentuk Scalar
            ane3 = sensor[-3]  # dalam bentuk Scalar

        else:
            acc = sensor  # dalam bentuk List
            ane1 = 0  # dalam bentuk Scalar
            ane2 = 0  # dalam bentuk Scalar
            ane3 = 0  # dalam bentuk Scalar

        print(acc)
        print(node, timestamp, len(sensor), '\n')


if __name__ == "__main__":
    # Buat koneksi mqtt sebagai client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print("Melakukan koneksi ke Broker...")

    client.connect("bbta3.bppt.go.id", 9621)

    try:
        client.username_pw_set(os.getenv('MQ_USER'), os.getenv('MQ_PWD'))
    except KeyError:
        print('Silahkan tambah env. untuk MQ_USER dan/atau MQ_PWD')
        sys.exit()

    client.loop_forever()
