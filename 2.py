import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10.01,0.01)
plt.plot(x,x*x-6-x)
plt.show()
D = (-1) ** 2 - 4 * (-6) * 1
print((1 - D ** 0.5)/2,(1 + D ** 0.5)/2)
