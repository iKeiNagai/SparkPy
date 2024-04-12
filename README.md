Spark/python

#WordCount
- input file peterpan.txt
- Remove stopwords from file
- Count frequency of words 
- Sort words based on frequency in descending order

#WordCount2
- Similar to WordCount but for each step, it creates a file

#RDD 
- Input file people.txt
- compute average age using RDDs

#Dataframe&SparkSQL
- Input file people.json
- compute average age using dataframe&SQl 

#Kmeans&graphh (spark ML)
- Input files kmeans_input
- Compute two clusters from kmeans_input
- outputs data point with prediction
- outputs file features(data),clusternum(prediction), and centers
- graphh use output files to create scatter graph

#spark_pagerank (spark GraphX)
- spark-shell  -i  spark_pagerank_graphx.scala to run
- Input files 02AdjacencyList
- creates directed graph from 02AdjacencyList
- Calculates pagerank of each node in graph