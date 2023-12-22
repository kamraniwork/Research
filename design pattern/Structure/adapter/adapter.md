<div dir="rtl" style="font-size:40px; color:yellow">
الگوی طراحی Adapter
</div>


<div dir="rtl" style="font-size:18px">
امکان میدهد یک یا چند رابط (interface) را به یک کلاس دیگر اضافه کنیم، بدون تغییر در ساختار اصلی آن. با این الگو میتوانیم کلاس های موجود را با تغییر حداقلی یا بدون تغییر در کد اصلی توسعه دهیم و رابط ها یا متدهای جدید به آن اضافه کنیم
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
یک مثال از دنیای واقعی:
</div>

<div dir="rtl" style="font-size:18px">
    واضح ترین مثال برای این الگوی طراحی خوده آداپتور‌ها هستن. (برای مثال، آداپتور‌های شارژر که سه شاخه رو به دو شاخه تبدیل میکنن)یامترجمی که کلمات یک نفر رو برای فرد دیگه ترجمه میکنه.
</div>


<div dir="rtl" style="font-size:30px; color:yellow">
به زبون ساده:
</div>

<div dir="rtl" style="font-size:18px">
    آداپتور بهتون کمک میکنه تا یک شی ناسازگار رو سازگار کنین تا بتونین توی کلاس‌های مختلف ازش استفاده کنین.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
پیاده سازی: 
</div>

<div dir="rtl" style="font-size:18px">
خب اول باید یک اینترفیس lion بسازیم که شیر‌های مختلف ازش استفاده کنن:
</div>

```python
class Lion:
    def roar(self):
        pass


class AfricanLion(Lion):
    def roar(self):
        pass


class AsianLion(Lion):
    def roar(self):
        pass
```

<div dir="rtl" style="font-size:18px">
خب حالا شکارچی وقتی شکار انجام بده اون شیر غرش انجام میده:
</div>

```python
class Hunter:
    def hunt(self, lion):
        lion.roar()
```

<div dir="rtl" style="font-size:18px">
حالا فرض کنید یک موجودیت جدید مثل سگ وحشی به برنامه اضافه شده.

خب سگ غرش انجام نمیده بجای اون bark انجام میده.

خب اینجا سگ وحشی با تابع hunt شکارچی ناسازگار میشه. (چون در زمان شکار تابع roar رو صدا میزنیم و سگ شکاری این تابع رو نداره!)

برای حلش به این صورت میتونیم براش آداپتور تعریف کنیم:</div>

```python
class WildDog:
    @staticmethod
    def bark():
        pass


class WildDogAdapter(Lion):
    _dog = None

    def __init__(self, dog):
        self._dog = dog

    def roar(self):
        self._dog.bark()
```

<div dir="rtl" style="font-size:18px">
در ادامه هم نحوه استفاده ازش رو میبینید:
</div>

```python
wildDog = WildDog()
wildDogAdapter = WildDogAdapter(wildDog)

hunter = Hunter()
hunter.hunt(wildDogAdapter)
```

<div dir="rtl" style="font-size:30px; color:yellow">
دلیل استفاده از این الگو:
</div>

<div dir="rtl" style="font-size:18px">
۱- توسعه کد موجود: وقتی که اضافه کردن متد یا کد به کد موجود ممکن یا معقول نباشد میتوانیم از این الگو استفاده کنیم.
</div>

<div dir="rtl" style="font-size:18px">
سازگاری با کتابخانه ها یا کلاس خارجی: اگر از یک کتابخانه خارجی استفاده میکنیم که رابط آن با نیازهای شما مطابقت ندارد
</div>
