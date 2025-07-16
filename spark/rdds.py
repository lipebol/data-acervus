from pyspark.sql import SparkSession


# .master:  Run Spark locally with a single thread
# .appName: Name the application "GettingStarted"
# .getOrCreate: Create or retrieve a SparkSession with the specified configurations

spark = SparkSession.builder.master("local[*]").appName("RDDs").getOrCreate()

# rdd_from_list = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

# print(rdd_from_list.count())

# rdd_from_file_numbers = spark.sparkContext.textFile('./files/one_file.txt')

# print(rdd_from_file.map(lambda x: int(x)+1).collect())

# print(rdd_from_list.filter(lambda x: x % 2 == 0).collect())


spark.sparkContext.textFile(
    './files/sales.txt'
).filter(
    lambda sale: float(sale.split(',')[1]) > 100
).map(
    lambda sale: sale.split(',')[0]
).repartition(3).saveAsTextFile('./files/high_value_sales')

print(spark.sparkContext.textFile('./files/high_value_sales').collect())
print(spark.sparkContext.textFile('./files/high_value_sales/part-00000').collect())
print(spark.sparkContext.textFile('./files/high_value_sales/part-00001').collect())


spark.stop()