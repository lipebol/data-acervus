from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.master("local[*]").appName("DataFrames").getOrCreate()

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

df_from_list_dict.show(5)
print(df_from_list_dict.count())
df_from_rdd.printSchema()
print(df_from_rdd.count())

df_from_csv = spark.read.csv(
    './files/sales.csv', header=True, inferSchema=True, sep=';'
).fillna({"price": 0}).dropna(subset=['name'])

df_from_csv.show(60)

df_from_json = spark.read.json('./files/sales.json', multiLine=True)

df_from_csv.select('name').join(
    df_from_json, 'name', 'right'
).write.parquet('./files/sales')

df_from_parquet = spark.read.parquet('./files/sales')

def filter(data):
    return data.filter(
        df_from_parquet.price > 900
    )

filter(df_from_parquet).select('name').show()

df_from_parquet = df_from_parquet.withColumn('cost_value', col('price') - 200)

filter(df_from_parquet).withColumn(
    'sale_value', col('price') + 200
).select('name', 'cost_value', 'sale_value').show()