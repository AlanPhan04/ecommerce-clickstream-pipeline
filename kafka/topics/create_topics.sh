#!/bin/bash
# Script tạo Kafka topic 'clickstream'
KAFKA_BIN=/usr/bin/kafka-topics.sh
$KAFKA_BIN --create --topic clickstream --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1