<div dir="rtl" style="font-size:40px; color:yellow">
الگوی طراحی Builder
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
یکی از زیرشاخه های الگوهای طراحی، Creational Design Patterns است.
این الگو راهی جهت ساخت و ایجاد اشیاء (object) از کلاس ها را ارائه میدهد.
ساخت یک شیء با استفاده از new کردن آن کلاس در اصطلاح hard code کردن راه حل خوبی نیست و بهتر است از الگوهای طراحی Creational استفاده کرد.


این الگو به ما این امکان رو میده تا به صورت مرحله به مرحله، یک آبجکت پیچیده رو بسازیم. الگوی Builder مرحله‌های ساختن
آبجکت رو برای ما تعریف می‌کنه و با اونها می‌تونیم آبجکت‌های متنوعی بسازیم.

استفاده از دیزاین پترن Builder موجب کاهش پیچیدگی ها در ساخت اشیاء میشود.

</div>

<div dir="rtl" style="font-size:30px; color:yellow">
به زبون ساده:
</div>

<div dir="rtl" style="font-size:18px">
    در واقع کار Builder اینه که توی ساخت ابجکت‌های پیچیده یا ابجکت‌هایی که نیاز به شخصی سازی زیادی دارن، بهمون کمک بکنه.در واقع روش کارش به این صورت هست که بجای اینکه تعداد زیادی پارامتر رو از ورودی تابع سازنده دریافت کنیم (__init__) ، اون دیتارو بصورت مرحله به مرحله دریافت کنیم.
</div>

<br/>

<div dir="rtl" style="font-size:18px">
برای همه ما پیش اومد که یک تابع سازنده به این شکل ببینیم:
</div>

```python
def __init__(self, size, cheese=True, pepperoni=True, tomato=False, lettuce=True)
```

<div dir="rtl" style="font-size:18px">
در این شرایط معمولا Builder میتونه به دادمون برسه.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
مثال برنامه نویسی
</div>

<div dir="rtl" style="font-size:18px">
اولین مرحله اینه که یک کلاس برگر معمولی داشته باشیم:
</div>

```python
class Burger:
    _size = None

    _cheese = False
    _pepperoni = False
    _lettuce = False
    _tomato = False

    def __init__(self, builder):
        self._size = builder.size
        self._cheese = builder.cheese
        self._pepperoni = builder.pepperoni
        self._lettuce = builder.lettuce
        self._tomato = builder.tomato
```

<div dir="rtl" style="font-size:18px">
در ادامه کلاس Builder رو براش ایجاد میکنیم:
</div>

```python
class BurgerBuilder:
    size = None

    cheese = False
    pepperoni = False
    lettuce = False
    tomato = False

    def __init__(self, size):
        self.size = size

    def addPepperoni(self):
        self.pepperoni = True
        return self

    def addLettuce(self):
        self.lettuce = True
        return self

    def addCheese(self):
        self.cheese = True
        return self

    def addTomato(self):
        self.tomato = True
        return self

    def build(self):
        return Burger(self)

```

<div dir="rtl" style="font-size:18px">
روش استفاده از کلاس Builder هم به این صورت هست:
</div>

```python
burger = BurgerBuilder(10).addPepperoni().addLettuce().addTomato().build()

print(vars(burger))
```


<div dir="rtl" style="font-size:30px; color:yellow">
چه زمانی از الگوی Builder استفاده کنیم؟
</div>

<div dir="rtl" style="font-size:18px">
همونطور که قبل تر اشاره کردم این دیزاین پترن رو معمولا برای ساخت ابجکت‌های پیچیده یا ابجکت‌هایی که نیاز به شخصی سازی زیادی دارن استفاده میکنیم.
</div>