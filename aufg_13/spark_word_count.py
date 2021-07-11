from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("word count").setMaster("local[3]")
    sc = SparkContext(conf=conf)

    lines = sc.textFile("/home/guido/gitprojects/datascience/aufg_13/t8.shakespeare.txt")

    words = lines.flatMap(lambda line: line.split(" "))

    wordCounts = words.countByValue()
    wordCounts_sorted = dict(sorted(wordCounts.items(), key=lambda item: item[1]))

    for word, count in wordCounts_sorted.items():
        print("{} : {}".format(word, count))

    #print(dir(wordCounts))

