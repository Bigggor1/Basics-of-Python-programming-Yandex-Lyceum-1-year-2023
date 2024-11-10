import matplotlib.pyplot as plt
import numpy as np

# create 1000 equally spaced points between -10 and 10
x = np.linspace(-25, 25, 1000)

# calculate the y value for each element of the x vector
y = (x**4) + (5*(x**3)) - (10*x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.grid()
plt.show()