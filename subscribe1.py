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

times = []
acc1 = []
acc2 = []
acc3 = []
ane1 = []
ane2 = []
ane3 = []


# Buat fungsi umpan balik ketika koneksi ke mqtt berhasil dilakukan.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # subscribe ke channel/topik saat on_connect()
    client.subscribe("BAMS")


# Buat fungsi umpan balik ketika PUBLISH MESSAGE diterima dari mqtt server.
def on_message(client, userdata, msg):
    n = 8  # pisah setiap 8 karakter
    node = msg.payload[0:3].decode('ascii')
    # timestamp = int(msg.payload[3:11], 16) * 1000  # dalam satuan ms
    # timestamp = int(msg.payload[3:11], 16)  # dalam satuan ms
    # timestamp = datetime.datetime.fromtimestamp(timestamp).isoformat()
    timestamp = datetime.datetime.now() - datetime.timedelta(seconds=3)
    timestamp = timestamp.strftime("%H:%M:%S")

    max_length=msg.payload[11:]

    if args.s is None or args.s == 0:
        sensor = [struct.unpack('!f', bytes.fromhex(msg.payload[i:i+n].decode('ascii')))[0]
                  for i in range(11, len(msg.payload[11:]) + n, n)]

        if node == "sb1":
            print(sensor[80])
            print(sensor[180])

            if len(acc1) < 5:
                acc1.append(sensor[80])
                acc2.append(sensor[180])
            else:
                acc1[:-1] = acc1[1:]
                acc1[-1] = sensor[80]

                acc2[:-1] = acc2[1:]
                acc2[-1] = sensor[180]

            if len(ane1) < 5:
                ane1.append(sensor[-3])
                ane2.append(sensor[-2])
                ane3.append(sensor[-1])
            else:
                ane1[:-1] = ane1[1:]
                ane1[-1] = sensor[-3]

                ane2[:-1] = ane2[1:]
                ane2[-1] = sensor[-2]

                ane3[:-1] = ane3[1:]
                ane3[-1] = sensor[-1]

            if len(times) < 5:
                times.append(timestamp)
            else:
                times[:-1] = times[1:]
                times[-1] = timestamp


        elif node == "sb2":
            print(sensor[80])
            print(sensor[180])
            print(sensor[280])

            if len(acc1) < 5:
                acc1.append(sensor[80])
                acc2.append(sensor[180])
            else:
                acc1[:-1] = acc1[1:]
                acc1[-1] = sensor[80]

                acc2[:-1] = acc2[1:]
                acc2[-1] = sensor[180]

            if len(acc3) < 5:
                acc3.append(sensor[280])
            else:
                acc3[:-1] = acc3[1:]
                acc3[-1] = sensor[280]

            if len(ane1) < 5:
                ane1.append(sensor[-3])
                ane2.append(sensor[-2])
                ane3.append(sensor[-1])
            else:
                ane1[:-1] = ane1[1:]
                ane1[-1] = sensor[-3]

                ane2[:-1] = ane2[1:]
                ane2[-1] = sensor[-2]

                ane3[:-1] = ane3[1:]
                ane3[-1] = sensor[-1]

            if len(times) < 5:
                times.append(timestamp)
            else:
                times[:-1] = times[1:]
                times[-1] = timestamp


        else:
            print(sensor[80])
            print(sensor[180])

            if len(acc1) < 5:
                acc1.append(sensor[80])
                acc2.append(sensor[180])
            else:
                acc1[:-1] = acc1[1:]
                acc1[-1] = sensor[80]

                acc2[:-1] = acc2[1:]
                acc2[-1] = sensor[180]

            if len(times) < 5:
                times.append(timestamp)
            else:
                times[:-1] = times[1:]
                times[-1] = timestamp


        print('\n',node, timestamp, len(sensor), len(max_length), len(max_length)/8)
    # print(sensor)
    print(acc1)
    print(acc2)
    print(acc3)
    print(ane1)
    print(ane2)
    print(ane3)
    print(times)


if __name__ == "__main__":
    # Buat koneksi mqtt sebagai client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print("Melakukan koneksi ke Broker...")

    client.connect("103.224.137.180", 9621)
    
    client.username_pw_set('bams', 'bams.pwd')

    client.loop_forever()
