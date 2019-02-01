# spark-submit load_avro.py --master spark://master:7077
import pyspark
from pyspark.sql import SparkSession
from decimal import Decimal
from pyspark.sql.types import *
from datetime import datetime
from time import time
pyspark.SparkContext.setSystemProperty('spark.sql.orc.impl', 'native')
sc = pyspark.SparkContext(appName="load_avro")
spark = SparkSession(sc)
name_list = [
    "region",
    "nation",
    "supplier",
    "part",
    "customer",
    "partsupp",
    "orders",
    "lineitem",
]
start_time = time()
for name in name_list:
    print("START LOAD: "+name)
    spark.read.format('parquet').load("hdfs://namenode:8020/"+name+".parquet")\
        .write.format("com.databricks.spark.avro").mode('overwrite')\
        .save("hdfs://namenode:8020/"+name+".avro")
    print("END LOAD: "+name)
