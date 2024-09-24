from pyspark.sql import SparkSession
from google.cloud import storage

# Change for github actions secrets
DELTA_LAKE  = "abinbev-database-delta-lake"
BQ_TABLE    = "abinbev-case-eric:brewery_data.breweries"
TEMP_BUCKET = "abinbev-temp"


if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("ExportDeltaToBq") \
        .config("spark.jars.packages", "io.delta:delta-core_2.12:1.2.1,com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.26.0") \
        .getOrCreate()

    client = storage.Client()
    bucket = client.get_bucket(DELTA_LAKE)

    delta_path = set()
    for blob in bucket.list_blobs():
        path_name = "/".join(blob.name.split("/")[:2])
        delta_path.add(f"gs://{DELTA_LAKE}/{path_name}")

    delta_dfs = [spark.read.format("delta").load(path) for path in delta_path]

    combined_df = delta_dfs[0]

    for df in delta_dfs[1:]:
        combined_df = combined_df.unionByName(df)

    combined_df.write \
        .format("bigquery") \
        .option("table", BQ_TABLE) \
        .option("temporaryGcsBucket", TEMP_BUCKET) \
        .mode("overwrite") \
        .save()