#!/bin/bash
echo "Start Kafka, ClickHouse with Docker..."
docker-compose -f docker/docker-compose.yml up -d

echo "Create Kafka topics..."
bash kafka/topics/create_topics.sh

echo "Run Spark job..."
spark-submit spark/jobs/clickstream_etl.py

echo "Pipeline started."