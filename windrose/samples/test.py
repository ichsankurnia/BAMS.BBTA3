import pandas as pd

from windrose import plot_windrose
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np

df = pd.read_csv("data_anemo(new).csv", sep=",")
# df = df.set_index("Kecepatan angin (ws)")

print(df["Kecepatan angin (ws)"]) # tampilin data kecepatan angin