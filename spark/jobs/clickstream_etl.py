from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp
from pyspark.sql.types import StructType, StructField, StringType, LongType

def main():
    spark = SparkSession.builder.appName('ClickstreamETL').getOrCreate()

    schema = StructType([
        StructField('type', StringType()),
        StructField('element', StringType()),
        StructField('timestamp', LongType()),
        StructField('x', LongType()),
        StructField('y', LongType())
    ])

    df = spark.readStream.format('kafka') \
        .option('kafka.bootstrap.servers', 'localhost:9092') \
        .option('subscribe', 'clickstream') \
        .load()

    json_df = df.select(from_json(col('value').cast('string'), schema).alias('data')).select('data.*')
    enriched_df = json_df.withColumn('event_time', to_timestamp((col('timestamp')/1000).cast('timestamp')))

    # TODO: clean, enrich, transform data

    query = enriched_df.writeStream \
        .format('console') \
        .outputMode('append') \
        .start()

    query.awaitTermination()

if __name__ == '__main__':
    main()