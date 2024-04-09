from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

#Using Dataframe to compute average age in each gender

spark = SparkSession.builder \
    .appName("Average") \
    .getOrCreate()

#input file
people1 = spark.read.json("people.json")

#groupby gender and avg age
gender_average = people1.groupby("gender").avg("age")

#show output 
gender_average.show()