from pyspark import SparkContext, SparkConf

# Prepare the Spark context
conf = SparkConf().setAppName("Word Frequency Count").setMaster("local")
sc = SparkContext(conf=conf)

# Input file
input_file_name = "hello"
lines = sc.textFile(input_file_name)

# List of stopwords
stopwords = set([
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no",
    "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this",
    "to", "was", "will", "with"
])

# Split each line into words, remove stopwords, and count the frequency of each word
stopwords = lines.flatMap(lambda line: line.split(" ")) \
                 .filter(lambda word: word.lower() not in stopwords) \
                 .map(lambda word: (word.lower()))
stopwords.saveAsTextFile("")

# Sort the words by frequency in descending order
sorted_word_counts = word_counts.sortBy(lambda x: x[1], ascending=False)

# Output the sorted word counts
for word, count in sorted_word_counts.collect():
    print(f"{word}: {count}")

# Stop the Spark context
sc.stop()
