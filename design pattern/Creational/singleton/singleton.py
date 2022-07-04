class SingleTonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """
    __instance = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls.__instance:
            cls.__instance[cls] = super().__call__(*args, **kwargs)
        return cls.__instance[cls]


class DBConnector(metaclass=SingleTonMeta):
    def __init__(self):
        self.status = "Not Connected"

    def disconnect(self):
        self.status = "Disconnected"

    def connect(self):
        self.status = "Connected"


client1 = DBConnector()
print("Client 1 ", client1)
print(client1.status)

client2 = DBConnector()
print("Client 2 ", client2)
client2.connect()
print(client1.status)
