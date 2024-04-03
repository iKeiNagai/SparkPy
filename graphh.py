import numpy as np
import matplotlib.pyplot as plt

#Load data from file
array = np.loadtxt('features.txt')

#Extract data from file
x = array[:, 0]
y = array[:, 1]

# Plot the data as a scatter plot
plt.scatter(x, y)
plt.show()
