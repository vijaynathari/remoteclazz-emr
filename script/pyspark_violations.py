import sys
from operator import add
from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Create Spark session
    spark = SparkSession.builder.appName("Calculate Red Health Violations").getOrCreate()

    # Load the restaurant violation CSV data
    restaurants_df = spark.read.option("header", "true").csv(sys.argv[1])

    # Create an in-memory DataFrame to query
    restaurants_df.createOrReplaceTempView("restaurant_violations")

    # Create a DataFrame of the top 10 restaurants with the most Red violations
    top_red_violation_restaurants = spark.sql("SELECT name, count(*) AS total_red_violations " +
        "FROM restaurant_violations " +
        "WHERE violation_type = 'RED' " +
        "GROUP BY name " +
        "ORDER BY total_red_violations DESC LIMIT 10 ")

    # Write the results to the specified output URI
    top_red_violation_restaurants.write.option("header", "true").mode("overwrite").csv(sys.argv[2])

    spark.stop()