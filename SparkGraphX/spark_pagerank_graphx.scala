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
val create_edges = linesArray.flatMap { arr =>
  val src = arr.head
  arr.tail.map(dest => Edge(src, dest, 1))
}

//creates graph with vertices and edges 
val graph = Graph(firstItemstoVertice, create_edges)

//displays graph vertices and edges
val getvertices = graph.vertices.collect()
val getedges = graph.edges.collect()

//calculate pagerank
val PageRankGraph1 = graph.staticPageRank(30, 0.15)

//stores pagrerank with vertices.
val PageRankVertices1 = PageRankGraph1.vertices

//total pagerank sum 
val dSum1 = PageRankVertices1.map(values => values._2).sum()

//each pagerank is divided by pagerank sum
val PageRankVertices11 = PageRankVertices1.mapValues(prValue=> prValue / dSum1)

//displays pagerank
val PageRankValues1 = PageRankVertices11.collect()
println("PageRank:")
println(PageRankValues1.mkString("\n"))

//prints file
file.collect().foreach(println)