# RUN ON PYSPARK
from decimal import Decimal
from pyspark.sql.types import *
from pyspark.sql import SQLContext
from datetime import datetime
import pyspark
from pyspark.sql import SparkSession
sc = pyspark.SparkContext(appName="load_parq")
sqlContext = SQLContext(sc)
spark = SparkSession(sc)
tbl_folder = "/clean_data/"

data = sc.textFile(tbl_folder+"/region.tbl")
fields = [
    StructField("R_REGIONKEY", IntegerType()),
    StructField("R_NAME", StringType()),
    StructField("R_COMMENT", StringType()),
]
schema = StructType(fields)
data_frame = data\
            .map(lambda x:x.split("|"))\
            .map(lambda x: {
                "R_REGIONKEY":int(x[0]),
                "R_NAME": x[1],
                "R_COMMENT": x[2]
            })\
            .toDF(schema)
data_frame.write.mode("overwrite").parquet("hdfs://namenode:8020/region.parquet")

data = sc.textFile(tbl_folder+"/nation.tbl")
fields = [
    StructField("N_NATIONKEY", IntegerType()),
    StructField("N_NAME", StringType()),
    StructField("N_REGIONKEY", StringType()),
    StructField("N_COMMENT", StringType()),
]
schema = StructType(fields)
data_frame = data\
            .map(lambda x:x.split("|"))\
            .map(lambda x: {
                "N_NATIONKEY":int(x[0]),
                "N_NAME": x[1],
                "N_REGIONKEY": int(x[2]),
                "R_COMMENT": x[3],
            })\
            .toDF(schema)
data_frame.write.mode("overwrite").parquet("hdfs://namenode:8020/nation.parquet")

data = sc.textFile(tbl_folder+"/supplier.tbl")
fields = [
    StructField("S_SUPPKEY", IntegerType()),
    StructField("S_NAME", StringType()),
    StructField("S_ADDRESS", StringType()),
    StructField("S_NATIONKEY", StringType()),
    StructField("S_PHONE", StringType()),
    StructField("S_ACCTBAL", DecimalType()),
    StructField("S_COMMENT", StringType()),
]
schema = StructType(fields)
data_frame = data\
            .map(lambda x:x.split("|"))\
            .map(lambda x: {
                "S_SUPPKEY":int(x[0]),
                "S_NAME": x[1],
                "S_ADDRESS": x[2],
                "S_NATIONKEY": int(x[3]),
                "S_PHONE": x[4],
                "S_ACCTBAL": Decimal(x[5]),
                "S_COMMENT": x[6],
            })\
            .toDF(schema)
data_frame.write.mode("overwrite").parquet("hdfs://namenode:8020/supplier.parquet")

data = sc.textFile(tbl_folder+"/part.tbl")
fields = [
    StructField("P_PARTKEY", IntegerType()),
    StructField("P_NAME", StringType()),
    StructField("P_MFGR", StringType()),
    StructField("P_BRAND", StringType()),
    StructField("P_TYPE", StringType()),
    StructField("P_SIZE", IntegerType()),
    StructField("P_CONTAINER", StringType()),
    StructField("P_RETAILPRICE", DecimalType()),
    StructField("P_COMMENT", StringType()),
]
schema = StructType(fields)
data_frame = data\
            .map(lambda x:x.split("|"))\
            .map(lambda x: {
                "P_PARTKEY":int(x[0]),
                "P_NAME": x[1],
                "P_MFGR": x[2],
                "P_BRAND": x[3],
                "P_TYPE": x[4],
                "P_SIZE": int(x[5]),
                "P_CONTAINER": x[6],
                "P_RETAILPRICE": Decimal(x[7]),
                "P_COMMENT": x[8],
            })\
            .toDF(schema)
data_frame.write.mode("overwrite").parquet("hdfs://namenode:8020/part.parquet")

data = sc.textFile(tbl_folder+"/customer.tbl")
fields = [
    StructField("C_CUSTKEY", IntegerType()),
    StructField("C_NAME", StringType()),
    StructField("C_ADDRESS", StringType()),
    StructField("C_NATIONKEY", IntegerType()),
    StructField("C_PHONE", StringType()),
    StructField("C_ACCTBAL", DecimalType()),
    StructField("C_MKTSEGMENT", StringType()),
    StructField("C_COMMENT", StringType()),
]
schema = StructType(fields)
data_frame = data\
            .map(lambda x:x.split("|"))\
            .map(lambda x: {
                "C_CUSTKEY":int(x[0]),
                "C_NAME": x[1],
                "C_ADDRESS": x[2],
                "C_NATIONKEY": int(x[3]),
                "C_PHONE": x[4],
                "C_ACCTBAL": Decimal(x[5]),
                "C_MKTSEGMENT": x[6],
                "C_COMMENT": x[7],
            })\
            .toDF(schema)
data_frame.write.mode("overwrite").parquet("hdfs://namenode:8020/customer.parquet")


data = sc.textFile(tbl_folder+"/partsupp.tbl")
fields = [
    StructField("PS_PARTKEY", IntegerType()),
    StructField("PS_SUPKEY", IntegerType()),
    StructField("PS_AVAILQTY", IntegerType()),
    StructField("PS_SUPPLYCOST", DecimalType()),
    StructField("PS_COMMENT", StringType()),
]
schema = StructType(fields)
data_frame = data\
            .map(lambda x:x.split("|"))\
            .map(lambda x: {
                "PS_PARTKEY":int(x[0]),
                "PS_SUPKEY": int(x[1]),
                "PS_AVAILQTY": int(x[2]),
                "PS_SUPPLYCOST": Decimal(x[3]),
                "PS_COMMENT": x[4],
            })\
            .toDF(schema)
data_frame.write.mode("overwrite").parquet("hdfs://namenode:8020/partsupp.parquet")

data = sc.textFile(tbl_folder+"/orders.tbl")
fields = [
    StructField("O_ORDERKEY", IntegerType()),
    StructField("O_CUSTKEY", IntegerType()),
    StructField("O_ORDERSTATUS", StringType()),
    StructField("O_TOTALPRICE", DecimalType()),
    StructField("O_ORDERDATE", DateType()),
    StructField("O_ORDERPRIORITY", StringType()),
    StructField("O_CLERK", StringType()),
    StructField("O_SHIPPRIORITY", IntegerType()),
    StructField("O_COMMENT", StringType()),
]
schema = StructType(fields)
data_frame = data\
            .map(lambda x:x.split("|"))\
            .map(lambda x: {
                "O_ORDERKEY":int(x[0]),
                "O_CUSTKEY": int(x[1]),
                "O_ORDERSTATUS": x[2],
                "O_TOTALPRICE": Decimal(x[3]),
                "O_ORDERDATE": datetime.strptime(x[4],"%Y-%m-%d"),
                "O_ORDERPRIORITY": x[5],
                "O_CLERK": x[6],
                "O_SHIPPRIORITY": int(x[7]),
                "O_COMMENT": x[8],
            })\
            .toDF(schema)
data_frame.write.mode("overwrite").parquet("hdfs://namenode:8020/orders.parquet")


data = sc.textFile(tbl_folder+"/lineitem.tbl")
fields = [
    StructField("L_ORDERKEY", IntegerType()),
    StructField("L_PARTKEY", IntegerType()),
    StructField("L_SUPKEY", IntegerType()),
    StructField("L_LINENUMBER", IntegerType()),
    StructField("L_QUANTITY", DecimalType()),
    StructField("L_EXTENDEDPRICE", DecimalType()),
    StructField("L_DISCOUNT", DecimalType()),
    StructField("L_TAX", DecimalType()),
    StructField("L_RETURNFLAG", StringType()),
    StructField("L_LINESTATUS", StringType()),
    StructField("L_SHIPDATE", DateType()),
    StructField("L_COMMITDATE", DateType()),
    StructField("L_RECEIPTDATE", DateType()),
    StructField("L_SHIPINSTRUCT", StringType()),
    StructField("L_SHIPMODE", StringType()),
    StructField("L_COMMENT", StringType()),
]
schema = StructType(fields)
data_frame = data\
            .map(lambda x:x.split("|"))\
            .map(lambda x: {
                "L_ORDERKEY":int(x[0]),
                "L_PARTKEY": int(x[1]),
                "L_SUPKEY": int(x[2]),
                "L_LINENUMBER": int(x[3]),
                "L_QUANTITY": Decimal(x[4]),
                "L_EXTENDEDPRICE": Decimal(x[5]),
                "L_DISCOUNT": Decimal(x[6]),
                "L_TAX": Decimal(x[7]),
                "L_RETURNFLAG": x[8],
                "L_LINESTATUS": x[9],
                "L_SHIPDATE": datetime.strptime(x[10],"%Y-%m-%d"),
                "L_COMMITDATE": datetime.strptime(x[11],"%Y-%m-%d"),
                "L_RECEIPTDATE": datetime.strptime(x[12],"%Y-%m-%d"),
                "L_SHIPINSTRUCT": x[13],
                "L_SHIPMODE": x[14],
                "L_COMMENT": x[15],
            })\
            .toDF(schema)
data_frame.write.mode("overwrite").parquet("hdfs://namenode:8020/lineitem.parquet")
