<div dir="rtl" style="font-size:40px; color:yellow">
الگوی طراحی singleton
</div>


<div dir="rtl" style="font-size:18px">
یکی از زیرشاخه های الگوهای طراحی، Creational Design Patterns است.
این الگو راهی جهت ساخت و ایجاد اشیاء (object) از کلاس ها را ارائه میدهد.
ساخت یک شیء با استفاده از new کردن آن کلاس در اصطلاح hard code کردن راه حل خوبی نیست و بهتر است از الگوهای طراحی Creational استفاده کرد.
هدف این الگوی طراحی این است تا مطمئن شویم از یک کلاس، فقط و فقط یک شیء در کل برنامه وجود دارد.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
انواع پیاده سازی: 
</div>

<div dir="rtl" style="font-size:20px;">
روش اول:
</div>

```python
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

```

<div dir="rtl" style="font-size:20px;">
روش دوم:
</div>

```python
class SingleTonDecorator(object):
    """
       The Singleton class can be implemented in different ways in Python. Some
       possible methods include: base class, decorator, metaclass. We will use the
       decorator
    """

    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


@SingleTonDecorator
class Logger(object):
    def __init__(self):
        self.start = None

    def write(self, message):
        if self.start:
            print(self.start, message)
        else:
            print(message)

```

<div dir="rtl" style="font-size:20px;">
روش سوم:(بهینه)
</div>

```python
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

```

```text

output:
Client 1  <__main__.DBConnector object at 0x7f3613f396c0>
Not Connected
Client 2  <__main__.DBConnector object at 0x7f3613f396c0>
Connected

```

<div dir="rtl" style="font-size:20px;">
مشاهده میشود که وقتی یک شی از کلاس DBConnector ساخته میشود و در متغیر clinet1 ریخته میشود که خروجی status برابر است با "Not Connected".
یک شی دیگر از این کلاس میسازیم و آن را در متغیر client2 ذخیره میکنیم حال اگر متد connect را فراخوانی کنیم در این صورت status برابر میشود با "Connected" حال اگر دوباره client1 را چاپ کنیم مقدار "Connected" چاپ میکند 

این یعنی فقط یک شی ساخته شده و هر اتفاقی که به آن شی بیفتد برای سایر جاهایی که ساخته شده همان یکی است
</div>