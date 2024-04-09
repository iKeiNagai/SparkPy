from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
# Prepare the Spark context
conf = SparkConf().setAppName("Average").setMaster("local")
sc = SparkContext(conf=conf)

#input files
text_file_input = "people.txt"
people = sc.textFile(text_file_input)


#Using RDDs to compute average age in each gender
males = people.map(lambda line: line.split(" ")) \
                  .filter(lambda x: x[2] == "Male") \
                  .map(lambda x: (int(x[1]),0)) 

males_age = males.aggregate((0,0),      #initialization
        (lambda acc, value: (acc[0] + value[0], acc[1] + 1)), #each partition
        (lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])) #Adds partitions together
        )

males_average_age = males_age[0]/males_age[1]   #calculates average 


females = people.map(lambda line: line.split(" ")) \
                  .filter(lambda x: x[2] == "Female") \
                  .map(lambda x: (int(x[1]),0)) 

females_age = females.aggregate((0,0),    #initialization
        (lambda acc, value: (acc[0] + value[0], acc[1] + 1)), #each partition
        (lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])) #Adds partitions together
        )

females_average_age = females_age[0]/females_age[1]


print(str(females_average_age) + " Females avg age")
print(str(males_average_age) + " Males avg age")


