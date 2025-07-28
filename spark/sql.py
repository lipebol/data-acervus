from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.master("local[*]").appName("SQL").getOrCreate()

spark.read.parquet('./files/sales').createOrReplaceTempView('sales')

# spark.sql('SELECT * FROM sales LIMIT 7').explain()

def name_range(name: str, range: str):
    return f"{name} ({range})"

spark.udf.register("new_name", udf(name_range, StringType()))

spark.sql(
    """
    SELECT new_name(name, range) AS product, valuable FROM 
        (SELECT
            *,
            CASE
                WHEN price <= 500 THEN '0-500'
                WHEN price >= 501 AND price <= 1000 THEN '501-1000'
                ELSE '1000+'
            END AS range,
            CASE
                WHEN range IN ('0-500') THEN 'low'
                WHEN range IN ('501-1000') THEN 'medium'
                ELSE 'high'
            END AS valuable
        FROM
            sales
        ORDER BY price DESC)
    """
).show()