from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0,5,50)

plt.figure(figsize = (10,10))
plt.plot(x, np.cos(x))
plt.show()


