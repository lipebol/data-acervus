from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("SQL").getOrCreate()

spark.read.parquet('./files/sales').createOrReplaceTempView('sales')

spark.sql('SELECT * FROM sales LIMIT 7').show()