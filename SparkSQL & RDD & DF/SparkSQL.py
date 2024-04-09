from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

#Using SparkSQL to compute average age in each gender

spark = SparkSession.builder \
    .appName("Average") \
    .getOrCreate()

#input file
people2 = spark.read.json("people.json")

#creates temporary table of dataframe
people2.createOrReplaceTempView("people")

#Sql statement to get data from temporary table
gender_avg = spark.sql("SELECT gender, avg(age) FROM people GROUP BY gender")

#show output
gender_avg.show()