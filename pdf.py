from math import gamma, exp
import pandas as pd
import plotly.graph_objects as graph

if __name__ == '__main__':
	df = pd.read_csv('DataAngin/anm3.2_BRIDGE_SISI PASURUAN.csv', sep=';')
	# print(df.head())
	# print(df.X.min())	# print(df.Y.min()) 
	# print(df.X.max())	# print(df.Y.min())

	df = df[(df.X > 0 ) & (df.X < 20)]
	# print(df.X.max())

	df.sort_values('X', inplace=True) # tim data yg lama jika ada data yg baru
	# print(df.head(20)) # ambil 20 data

	# a = []
	# a.append(df.X)
	# print(a)

	print(df)

	rata2_kec = df.X.mean() 		# kecepatan rata2
	std_deviasi_kec = df.X.std() 	# standart deviasi
	# print(rata2_kec)

	# Hitung parameter bentuk k
	k = pow(std_deviasi_kec / rata2_kec, -1.086)

	# Hitung parameter skala c
	c = rata2_kec / gamma(1 + 1 / k)

	# Tambah kolom baru kedalam dataFrame untuk PDF
	df['pdf'] = df.X.apply(lambda v: (k / c) * pow(v / c, k - 1) * exp(-1 * pow(v / c, k)))
	df = df[['X', 'pdf']]		# Tampilkan hanya data x dan pdf
	# print(df.head())

	print(df)


	fig = graph.Figure()
	fig.add_trace(graph.Histogram(x=df.X, histnorm='probability density'))
	fig.add_trace(graph.Scattergl(x=df.X, y=df.pdf))
	fig.show()