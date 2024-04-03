import numpy as np
import matplotlib.pyplot as plt

#Load data from file
array = np.loadtxt('features.txt')
list = np.loadtxt('clusternum.txt')
#Extract data from file
x = array[:, 0]
y = array[:, 1]

#Plot data as a scatter plot
plt.scatter(x, y, c=list)

#cluster 1 color red and cross mark
x_cluster1 = x[list == 0]
y_cluster1 = y[list == 0]
plt.scatter(x_cluster1, y_cluster1, color='red', marker='x', label='Cluster 1')

#cluster 2 color blue and circle mark
x_cluster1 = x[list == 1]
y_cluster1 = y[list == 1]
plt.scatter(x_cluster1, y_cluster1, color='blue', marker='o', label='Cluster 2')

#show graph
plt.show()
