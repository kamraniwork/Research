<div dir="rtl" style="font-size:40px; color:yellow">
ساختمان داده ها در پایتون
</div>

<div dir="rtl" style="font-size:30px; color:orange">
دیکشنری
</div>

<div dir="rtl" style="font-size:18px">

این ساختمان داده بسیار قدرتمند است و شامل یک کلید و یک مقدار است که این کلید hash میشود و وقتی مقدار این کلید رو
میخواهیم مقدار hash این کلید جست وجو میشود که سریع تر است
</div>

```commandline
>>> phonebook = {
...     "bob": 7387,
...     "alice": 3719,
...     "jack": 7052,
... }

>>> squares = {x: x * x for x in range(6)}

>>> phonebook["alice"]
3719

>>> squares
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

<div dir="rtl" style="font-size:18px">
دیکشنری در سرتاسر زبان پایتون استفاده شده و باعث بهینه تر شدن این زبان شده است. مثلا متغیرهای کلاس و متغیر های پشته ها و ...

همانطور که گفتیم این ساختمان داده از تابع hash برای ذخیره کلید ها استفاده میکنه که همین باعث میشه عملیات های اصلی مثل
خواندن و نوشتن و حذف کردن و بروزرسانی ها در مدت زمان (1)o انجام شود

کتابخانه استاندارد پایتون شامل دیکشنری های دیگری علاوه بر دیکشنری اصلی خودش هست که دارای امکانات اضافه تری هست ولی بر
پایه همان دیکشنری اصلی کار میکند

1.OrderedDict():

این ساختمان داده ترتیب ورود کلید هارو حفظ میکنه. گفتیم که دیکشنری معمولی از hash استفاده میکنه و این hash ممکنه کلید ها
رو جابه جا در حافظه ذخیره کنه
</div>

```python
import collections

d = collections.OrderedDict(one=1, three=3, two=2, a=0)
for i in d:
    print(i)

```

<div dir="rtl" style="font-size:18px">
2.defaultdict()

این ساختمان داده اگر مقدار کلید اشتباه وارد بشه خطایی نمیده و یک مقدار خالی برمیگردونه
</div>

```python
from collections import defaultdict

dd = defaultdict(list)
dd['a'].append(1)

for i in dd:
    print(dd[i])
# output: [1]
print(dd['mehran'])
# output: []
```

<div dir="rtl" style="font-size:18px">
3.ChainMap

برای ادغام دو دیکشنری در یک دیکشنری استفاده میشود
</div>

```python
from collections import ChainMap

dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}

chain = ChainMap(dict1, dict2)

print(chain['one'])
# output: 1
chain['one'] = 11
print(chain['one'])
# output: 11
```

<div dir="rtl" style="font-size:18px">
4.MappingProxyType

این ساختمان داده فقط قابلیت خواندن از دیکشنری را فراهم میکند و نمیتوانیم تغییری در دیکشنری بدهیم
</div>

```python
from types import MappingProxyType

writable = {"one": 1, "two": 2}
read_only = MappingProxyType(writable)

print(read_only["one"])
# output: 1
read_only["one"] = 23
# output: error
```

