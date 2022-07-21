import json
from kafka import KafkaConsumer

Consumer = KafkaConsumer(
    'test',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

for i in Consumer:
    print(json.loads(i.value))
