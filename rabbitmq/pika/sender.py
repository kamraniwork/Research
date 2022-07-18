try:
    import pika
except Exception as e:
    print(e)


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitMqConfigure(metaclass=Singleton):
    def __init__(self, queue='hello', host='localhost', routing_key='hello', exchange='', username='admin',
                 password='admin'):
        self.queue = queue
        self.host = host
        self.routing_key = routing_key
        self.exchange = exchange
        self.username = username
        self.password = password


class RabbitMq(object):
    def __init__(self, server):
        self.server = server

        self._credentials = pika.PlainCredentials(self.server.username, self.server.password)
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.server.host, credentials=self._credentials)
        )
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def publish(self, payload={}):
        self._channel.basic_publish(exchange=self.server.exchange, routing_key=self.server.routing_key,
                                    body=str(payload))
        print("Published Message: {}".format(payload))
        self._connection.close()


if __name__ == "__main__":
    server = RabbitMqConfigure(queue='hello', host='localhost', routing_key='hello', exchange='')
    rabbitmq = RabbitMq(server=server)
    rabbitmq.publish(payload={"data": 22})
