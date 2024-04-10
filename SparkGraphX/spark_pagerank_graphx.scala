import org.apache.spark.graphx.{Graph, Edge}
import org.apache.spark.SparkContext

//spark context
val conf = new SparkConf()
  .setAppName("Pagerank")
  .setMaster("local[*]") 
val sc = new SparkContext(conf)

//loads file
val file = sc.textFile("02AdjacencyList.txt")

//creates array of string for each line
val linesArray = file.map(line => line.split(" "))

//gets array
val arrays = linesArray.collect()
//prints file
file.collect().foreach(println)