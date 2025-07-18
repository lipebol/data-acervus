from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("RDDs").getOrCreate()

file = spark.sparkContext.textFile('./files/sales.txt')

def sparkDataFrame(data, cols=None):
    return spark.createDataFrame(data, cols)

df_from_list_dict = sparkDataFrame(
    file.map(
        lambda row: dict(
            (key,value) for key, value in zip(['name', 'price'], row.split(','))
        )
    ).collect()
)

df_from_rdd = sparkDataFrame(
    file.map(
        lambda row: list(info for info in row.split(','))
    ), ['name', 'price']
)

df_from_list_dict.show()
df_from_rdd.show()