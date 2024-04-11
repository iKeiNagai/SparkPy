import org.apache.spark.graphx.{Graph, Edge}
import org.apache.spark.SparkContext

//spark context
val conf = new SparkConf()
  .setAppName("Pagerank")
  .setMaster("local[*]") 
val sc = new SparkContext(conf)

//loads file
val file = sc.textFile("02AdjacencyList.txt")

//creates array of string for each line, converts to long
val linesArray = file.map(line => line.split(" ").map(.toLong))

//gets first items of array, map vertices to 1
val firstItemstoVertice = linesArray.map(arr => arr(0)).map(vertice => (vertice,1))

//map the edges 
val edges = linesArray.flatMap { arr =>
  val src = arr.head
  arr.tail.map(dest => Edge(src, dest, 1))
}

//creates graph with vertices and edges 
val graph = Graph(firstItemstoVertice, edges)

//displays graph vertices and edges
val getvertices = graph.vertices.collect()
val getedges = graph.edges.collect()

//prints file
file.collect().foreach(println)