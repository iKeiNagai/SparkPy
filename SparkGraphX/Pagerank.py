from pyspark.sql import SparkSession
from graphframes import GraphFrame

#Creates Session
spark = SparkSession.builder \
    .appName("pagerank") \
    .getOrCreate()


spark.stop()