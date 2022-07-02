class DBConnectorSingleton:
    class __DBConnector:
        def __init__(self):
            self.status = "Not Connected"

        def _disconnect(self):
            self.status = "Disconnected"

        def _connect(self):
            self.status = "Connected"

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = cls.__DBConnector()
        return cls.instance


client1 = DBConnectorSingleton()
print("Client 1 ", client1)
print(client1.status)

client2 = DBConnectorSingleton()
print("Client 2 ", client2)
client2._connect()
print(client1.status)
