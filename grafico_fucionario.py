import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv")

df_lucro = df[df['lucro'] > 0]
xpoints = df_lucro['nome']
ypoints = df_lucro['lucro']

plt.barh(xpoints, ypoints)

bars = plt.barh(xpoints, ypoints)

plt.bar_label(bars, fmt='%.2f', padding=3)

plt.title('grafico')
plt.xlabel('plano x')
plt.ylabel('plano y')

plt.show()