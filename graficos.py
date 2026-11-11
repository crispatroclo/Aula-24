import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)

plt.title('grafico')
plt.xlabel('plano x')
plt.ylabel('plano y')

plt.show()