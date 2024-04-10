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

//gets first items of array, map vertices to 1
val firstItems = linesArray.map(arr => arr(0)).map(vertice => (vertice,1))

//get value
val value = firstItems.collect()
//prints file
file.collect().foreach(println)