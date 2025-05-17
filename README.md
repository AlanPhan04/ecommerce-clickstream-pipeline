# Clickstream Analytics Project

## Mục đích
Thu thập và phân tích dữ liệu clickstream realtime từ client, xử lý bằng Kafka, Spark Structured Streaming, lưu trữ và truy vấn hiệu năng cao trên ClickHouse.

## Cấu trúc
- kafka/: Kafka producer, topic scripts
- spark/: Spark Structured Streaming job
- clickhouse/: DDL tạo bảng
- docker/: Docker Compose cho Kafka, ClickHouse
- notebooks/: Jupyter notebooks phân tích dữ liệu
- dashboards/: Dashboard Metabase/Superset config
- data/: Dữ liệu mẫu
- docs/: Tài liệu, báo cáo

## Hướng dẫn chạy
Xem file `run_pipeline.sh` để chạy toàn bộ pipeline.