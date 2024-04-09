from pyspark import SparkContext, SparkConf

# Prepare the Spark context
conf = SparkConf().setAppName("Word Frequency Count").setMaster("local")
sc = SparkContext(conf=conf)

# Read input file
input_file_name = "peterpan"
lines = sc.textFile(input_file_name)

#List of stopwords
stopwords = set([
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no",
    "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this",
    "to", "was", "will", "with"
])

#Remove stopwords and save to disk
remove_stopwords = lines.flatMap(lambda line: line.split(" ")) \
                                .filter(lambda word: word.lower() not in stopwords) \
                                .map(lambda word: word.lower())
remove_stopwords.saveAsTextFile("task1output")

#Count word frequencies and save to disk
word_counts = remove_stopwords.map(lambda word: (word, 1)) \
                        .reduceByKey(lambda x, y: x + y)
word_counts.saveAsTextFile("task2output")

#Sort word frequencies and save to disk
sorted_word_counts = word_counts.sortBy(lambda x: x[1], ascending=False)
sorted_word_counts.saveAsTextFile("task3output")

# Stop the Spark context
sc.stop()
