import findspark
findspark.init()   # makes pyspark importable as a regular library
#Get a Spark session
from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("shaheen_dp") \
    .config("spark.master","local[*]") \
    .getOrCreate()

import platform, sys, os
print('Platform = ',platform.platform())
print('Version of Spark = ',spark.version)
print('Python version = ',sys.version)


# schema_name = 'cmm_db'
# table_name = 'cs_cuboid_vsb_retail_tbl'
#
# datasource = spark.read.format("jdbc") \
#     .option("url", "jdbc:mysql://localhost:3306/cmm_db") \
#     .option("dbtable", "cs_cuboid_vsb_retail_tbl") \
#     .option("user", "root") \
#     .option("password", "") \
#     .option("useSSL", "false") \
#     .load()
#
# print(datasource.columns)
df = spark.read \
      .format("com.databricks.spark.csv") \
      .option("header", "true") \
      .option("sep",",") \
      .option("inferSchema", "true") \
      .load("/home/prasad/E/pythonNotes/datascienceNotes/input/titanic_train.csv")


# df = spark.read.csv("/home/prasad/Downloads/Meteorite_Landings.csv").cache()

# df.describe().show()

# import spark_df_profiling
# # spark_df_profiling.ProfileReport(datasource)
#
# profile = spark_df_profiling.ProfileReport(df)
# profile.to_file(outputfile="myoutputfile.html")

import spark_df_profiling_optimus

profile = spark_df_profiling_optimus.ProfileReport(df)
profile.to_file(outputfile="titanic.html")

