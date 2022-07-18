import pika
import ast


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitMqConfigure(metaclass=Singleton):
    def __init__(self, queue='hello', host='localhost', username='admin', password='admin'):
        self.queue = queue
        self.host = host
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
        print(" [*] Waiting for messages. To exit press Ctrl+c")

    def callback(slef, ch, method, propertis, body):
        payload = body.decode("utf-8")
        payload = ast.literal_eval(payload)
        print(type(payload))
        print("Data Received : {}".format(payload))

    def start_server(self):
        self._channel.basic_consume(
            queue=self.server.queue, on_message_callback=self.callback, auto_ack=True
        )
        self._channel.start_consuming()


if __name__ == "__main__":
    server = RabbitMqConfigure(host='localhost', queue='hello')
    rabbitmq = RabbitMq(server=server)
    rabbitmq.start_server()
