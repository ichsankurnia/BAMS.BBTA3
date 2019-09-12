import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as graph

from pymongo import *
import datetime
from pprint import *

df = pd.read_csv('DataAngin/anm3.2_BRIDGE_SISI PASURUAN.csv', sep=';')

df = df[(df.X > 1.5 ) & (df.X < 1.7)]

df.sort_values('X', inplace=True) # tim data yg lama jika ada data yg baru

data = df.iloc[0:5]

# print(data)

# data['X'] = df['X']
list_Time = data.Time.tolist()
list_X = data.X.tolist()
list_Y = data.Y.tolist()
list_Z = data.Z.tolist()

plt.plot([1, 2, 3, 4, 5], list_Y)
plt.ylabel('some numbers')
plt.xlabel('Y')
plt.show()

# fig = graph.Figure()
# fig.add_trace(graph.Histogram(x=[1,2,3,4,5], histnorm='probability density'))
# fig.add_trace(graph.Scattergl(x=[1,2,3,4,5], y=list_Y))
# fig.show()