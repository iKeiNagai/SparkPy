import numpy as np
import matplotlib.pyplot as plt

#Load data from file
array = np.loadtxt('features.txt')
clusternum = np.loadtxt('clusternum.txt')
centers = np.loadtxt('centers.txt')

#Extract data from file
x = array[: ,0]
y = array[: ,1]

#Plot data as a scatter plot
plt.scatter(x, y)

#cluster 1 color red and cross mark
x_cluster1 = x[clusternum == 0]
y_cluster1 = y[clusternum == 0]
plt.scatter(x_cluster1, y_cluster1, color='red', marker='x', label='Cluster 1')

#cluster 2 color blue and circle mark
x_cluster2 = x[clusternum == 1]
y_cluster2 = y[clusternum == 1]
plt.scatter(x_cluster2, y_cluster2, color='blue', marker='o', label='Cluster 2')

#extrated centers from file
centroid_1 = centers[0]
centroid_2 = centers[1]

#Plot centers as red and triangle in graph
plt.scatter(centroid_1,centroid_2 ,c='yellow', marker='^')
#show graph
plt.show()
