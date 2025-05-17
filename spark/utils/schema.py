from pyspark.sql.types import StructType, StructField, StringType, LongType

clickstream_schema = StructType([
    StructField('type', StringType()),
    StructField('element', StringType()),
    StructField('timestamp', LongType()),
    StructField('x', LongType()),
    StructField('y', LongType())
])