import json
from kafka import KafkaProducer

Producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))

Producer.send('test', {'kamrani': "mehran"})
