from pyspark.sql.functions import col,when, concat_ws, lit
from pyspark.sql import SparkSession
import sys

if __name__ == "__main__":

    spark = SparkSession.builder.appName("Test_Merge_Proj").getOrCreate()
    
    years =  list(range(2000, 2023))
    merged_df = None

    for year in years:
        #file_path = f"test_data_{year}.csv"
        file_path = f"{year}_Data.csv"

        df = spark.read.csv(file_path, header=True, inferSchema=True)
        
        df = df.filter(
            (col("Country Name") != "") & 
            (col("Country Code") != "") & 
            (col("Series Name") != "") & 
            (col("Series Code") != "")
        )

        if merged_df is None:
            merged_df = df
        else:
            merged_df = merged_df.join(df, ["Country Name", "Country Code", "Series Name", "Series Code"], "inner")

    merged_df = merged_df.drop("Country Code", "Series Code")
    
#     for col_name in merged_df.columns:
#         merged_df = merged_df.withColumn(
#             col_name, 
#             concat_ws(",", lit('"'), col(col_name), lit('"'))
#         )

    
    merged_df.write.csv("final_merge_data.csv", header=True, quoteAll=True)

    spark.stop()
    
    



