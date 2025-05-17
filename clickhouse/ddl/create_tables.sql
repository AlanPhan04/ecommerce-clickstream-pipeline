CREATE TABLE IF NOT EXISTS clickstream_events (
    event_date Date DEFAULT toDate(event_time),
    event_time DateTime,
    event_type String,
    element String,
    x Int32,
    y Int32
) ENGINE = MergeTree()
PARTITION BY event_date
ORDER BY (event_time);