<div dir="rtl" style="font-size:40px; color:yellow">
الگوی طراحی Decorator
</div>


<div dir="rtl" style="font-size:18px">
امکان افزودن عملکردهای اضافی به یک شی بدون تغییر کد مربوط به آن شی را میدهد
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
یک مثال از دنیای واقعی:
</div>

<div dir="rtl" style="font-size:18px">
    فرض کنید یک مغازه خدمات خودرویی دارید که خدمات متنوع ای ارائه می دهید. فاکتور نهایی رو چطور محاسبه می کنید؟ شما یک سرویس رو انتخاب می کنید و به صورت پویا قیمت خدمات ارائه شده رو به اون اضافه می کنید تا به هزینه نهایی برسید. در اینجا هر نوع خدمات یک دکوریتور است.
</div>


<div dir="rtl" style="font-size:30px; color:yellow">
به زبون ساده:
</div>

<div dir="rtl" style="font-size:18px">
    دکوریتور به ما کمک میکنه به یک ابجکت یک Behavior اضافه کنیم بدون اینکه اون ابجکت رو تغییر بدیم.مفهوم Behavior = رفتاری که یک شیء می‌تواند از خود بروز دهد.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
پیاده سازی: 
</div>

<div dir="rtl" style="font-size:18px">
برای مثال قهوه را در نظر بگیرید. اول از همه ما یک قهوه ساده داریم که رابط قهوه را پیاده سازی می کند.
</div>

```python
class Coffee:
    def getCost(self):
        pass

    def getDescription(self):
        pass


class SimpleCoffee(Coffee):
    def getCost(self):
        return 10

    def getDescription(self):
        return 'Simple Coffee'
```

<div dir="rtl" style="font-size:18px">
ما می‌خوایم کد رو توسعه‌پذیر کنیم تا در صورت نیاز، گزینه‌ها بتونند اون رو تغییر بدند.

پس بیاید چند دکوریتور براش بسازیم:
</div>

```python
class MilkCoffee(Coffee):
    _coffee = None

    def __init__(self, coffee):
        self._coffee = coffee

    def getCost(self):
        return self._coffee.getCost() + 2

    def getDescription(self):
        return self._coffee.getDescription() + ', milk'


class WhipCoffee(Coffee):
    _coffee = None

    def __init__(self, coffee):
        self._coffee = coffee

    def getCost(self):
        return self._coffee.getCost() + 5

    def getDescription(self):
        return self._coffee.getDescription() + ', whip'


class VanillaCoffee(Coffee):
    _coffee = None

    def __init__(self, coffee):
        self._coffee = coffee

    def getCost(self):
        return self._coffee.getCost() + 3

    def getDescription(self):
        return self._coffee.getDescription() + ', vanilla'
```

<div dir="rtl" style="font-size:18px">
و حالا نحوه ساخت قهوه سفارشی:
</div>

```python
someCoffee = SimpleCoffee()
print(someCoffee.getCost())
print(someCoffee.getDescription())

someCoffee = MilkCoffee(someCoffee)
print(someCoffee.getCost())
print(someCoffee.getDescription())

someCoffee = VanillaCoffee(someCoffee)
print(someCoffee.getCost())
print(someCoffee.getDescription())

someCoffee = WhipCoffee(someCoffee)
print(someCoffee.getCost())
print(someCoffee.getDescription())
```

<div dir="rtl" style="font-size:30px; color:yellow">
دلیل استفاده از این الگو:
</div>

<div dir="rtl" style="font-size:18px">
وقتی میخواهیم یک سیستم را توسعه پذیر کنیم و امکان افزودن عملکردها و ویژگی جدید را بدون تغییر در کد موجود فراهم کنید
</div>

<div dir="rtl" style="font-size:18px">
کار با API یا کتابخانه ها که قابلیت تغییر را ارایه نمیدهند که این الگو ویژگی و عملکردهای اضافی را به کد اضافه میکند
</div>
