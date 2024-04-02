from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans

#Creates Session
spark = SparkSession.builder \
    .appName("KMeansModel") \
    .getOrCreate()

dataset = spark.read.format("libsvm").load("kmeans_input.txt") 

#Model Training
#Kmeans model
kmeans = KMeans().setK(2).setSeed(1) #kmeans to 2 clusters,1 random initialization
model = kmeans.fit(dataset) #performs clustering

#model testing
#apply trained model to dataset
predictions = model.transform(dataset)

predictionssss = predictions.select("features","prediction").collect()

for i in predictionssss:
    print(i)

#Get cluster center (vector form)
centers = model.clusterCenters()

#Displays cluster centers
print("Cluster Centers: ")
for center in centers:
    print(center)