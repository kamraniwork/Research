<div dir="rtl" style="font-size:40px; color:yellow">
مقایسه ها در پایتون
</div>

<div dir="rtl" style="font-size:18px">
گفتیم که هر چیزی در پایتون از ابجکت ایجاد شده پس وقتی ایجاد میشه در مکانی از حافظه قرار میگیره.

حالا اگر دو مقدار یکسان بودن آیا پایتون تشخیص میده و دو متغیر رو به یک جای حافظه اشاره میکنه یا هر کدوم به قسمت های
مختلف حافظه اشاره میکنن؟
</div>

```commandline
>>> from sys import intern
>>> a = 'hello world'
>>> b = 'hello world'
>>> a is b
False
>>> id(a)
1603648396784
>>> id(b)
1603648426160

>>> a = intern(a)
>>> b = intern(b)
>>> a is b
True
>>> id(a)
1603648396784
>>> id(b)
1603648396784

```

<div dir="rtl" style="font-size:18px">
در مثال بالا دیدیم که متغیر های a , b به هر کدام به قسمت های مختلف حافظه اشاره دارند و به نوعی ربطی به هم ندارند.
ولی اگر از کتابخانه intern استفاده کنیم به پایتون میفهمونیم که این دو تا متغیر یکی هستن و هردو رو به یک مکان از حافظه اشاره کن

همان طور که گفتیم اگر بازه ی اعداد از ۵- تا ۲۵۶ باشه مفسر پایتون این اعداد رو در جای مخصوصی از حافظه اشاره میکنه پس اگر
بین این اعداد باشه میفهمه که متغیر ها برابرند:

</div>

```commandline
>>> a = 256
>>> b = 256
>>> a is b
True
>>> id(a)
1638894624
>>> id(b)
1638894624

>>> a = 257
>>> b = 257
>>> a is b
False

>>> id(a)
2570926051952
>>> id(b)
2570926051984
```

<div dir="rtl" style="font-size:18px">
 اگر از عملگر (=) برای مساوی قرار دادن دو متغیر استفاده کنیم یعنی داریم میگیم که این دو تا آبجکت یکی هستند و در یک خونه از حافظه به این دو متغیر اشاره کن. بنابراین دارای id های یکسانی میشوند و تغییر در هر کدام از آنها
باعث تغییر در دیگری میشود چون به یک خانه از حافظه اشاره دارند
</div>

```commandline
>>> a = [1, 2, 3]
>>> b = a
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]

>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3, 4]

>>> id(a)
2570926056520
>>> id(b)
2570926056520

```

<div dir="rtl" style="font-size:18px">
 در حالت معمولی این چنین نیست یعنی اگر ما مساوی قرار ندیم (a=b) نمیفهمه که اینا یکی هستن
</div>

```commandline
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
>>> id(a)
2356388925576
>>> id(b)
2356388952648
```

<div dir="rtl" style="font-size:18px">
با استفاده از تابع copy میتوانیم مقدار فقظ مقدار متغیر را در متغیر دیگر قرار دهیم ولی هردو متغیر به جاهای مختلف حافظه اشاره کنند
و تغییر در هر کدام از متغیر ها باعث تغییر در متغیر های دیگر نشه
</div>

```commandline
>>> a = [1, 2, 3]
>>> b = a.copy()
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]

>>> a == b
True
>>> a is b
False

>>> id(a)
2570926058312
>>> id(b)
2570926057736
```

<div dir="rtl" style="font-size:18px">
میتونیم از magic method ها در کلاس استفاده کنیم و خروجی مد نظر خودمون وقتی از == استفاده شد رو اعمال کنیم مثلا:
</div>

```python
class SillyString(str):
    # This method gets called when using == on the object
    def __eq__(self, other):
        print(f'comparing {self} to {other}')
        # Return True if self and other have the same length
        return len(self) == len(other)    
```

```commandline
>>> # Compare two strings
>>> 'hello world' == 'world hello'
False

>>> # Compare a string with a SillyString
>>> 'hello world' == SillyString('world hello')
comparing world hello to hello world
True

>>> # Compare a SillyString with a list
>>> SillyString('hello world') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
comparing hello world to [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
True

```