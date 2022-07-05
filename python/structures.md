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

<div dir="rtl" style="font-size:30px; color:orange">
آرایه ها:
</div>

<div dir="rtl" style="font-size:18px">
از آنجایی که آرایه‌ها اطلاعات را در بلوک‌های مجاور حافظه ذخیره می‌کنند، به عنوان ساختارهای داده پیوسته در نظر گرفته می‌شوند

1.list:

درپایتون همه چیز از ابجکت تشکیل شده است. پس میتوان در هر لیست شی با انواع مختلف تشکیل داد و میتوان چندین نوع
را در لیست ها ذخیره کرد. همچنین اندازه اون ها به صورت داینامیک هست یعنی مشخص نیست به چه تعداد هست
</div>

```python
arr = ['one', 'two', 'three']
print(arr[0])
# output: one
arr[1] = 'hello'
print(arr)
# output: ['one','hello','three']
del arr[1]
arr.append(23)
print(arr)
# output: ['one','three',23]
```

<div dir="rtl" style="font-size:18px">
2.tuple

ویژگی تاپل ها مانند لیست ها هست ولی نمیتوان محتوای آن را ویرایش یا حذف کرد.
فقط میتوانیم با تاپل ها محتوا را بخوانیم
</div>

```python
arr = ('one', 'two', 'three')
print(arr[0])
# output: one
arr[1] = 'hello'
# output: error
del arr[1]
# output: error
```

<div dir="rtl" style="font-size:18px">
3.array.array

داده هارا مثل همان ارایه موجود در زبان c ذخیره میکنه و نسبت به type حساس هست.
یعنی باید یا همه رشته باشند یا همه عدد صحیح یا اعشار یا ...
</div>

```python
import array

arr = array.array("f", (1.0, 1.5, 2.0, 2.5))
print(arr[1])
# output: 1.5
arr[1] = 23.0
print(arr)
# output: array('f', [1.0, 23.0, 2.0, 2.5])
del arr[1]
print(arr)
# output: array('f', [1.0, 2.0, 2.5])
arr.append(42.0)
print(arr)
# output: array('f', [1.0, 2.0, 2.5, 42.0])
arr[1] = "hello"
# output: error
```

<div dir="rtl" style="font-size:18px">
4.str

در پایتون نسخه ۳ رشته هارو به صورت آرایه ای از unicode ها ذخیره میکند
</div>

```python
arr = "abcd"
print(arr[1])
# output: 'b'
arr[1] = "e"
# output: error
del arr[1]
# output: error
```

<div dir="rtl" style="font-size:18px">
5.bytes

فقط اعداد بین ۰ تا ۲۵۵ رو ذخیره میکنه
</div>

```commandline
>>> arr = bytes((0, 1, 2, 3))
>>> arr[1]
1

>>> # Bytes literals have their own syntax:
>>> arr
b'\x00\x01\x02\x03'
>>> arr = b"\x00\x01\x02\x03"

>>> # Only valid `bytes` are allowed:
>>> bytes((0, 300))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: bytes must be in range(0, 256)

>>> # Bytes are immutable:
>>> arr[1] = 23
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment

>>> del arr[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object doesn't support item deletion

```

<div dir="rtl" style="font-size:18px">
6.bytearray

در این ساختمان داده فقط میتوان عدد بین ۰ تا ۲۵۵ ذخیره کرد و همچنین میتوان اعداد ذخیره شده رو بروزرسانی و حذف کرد
</div>

```commandline
>>> arr = bytearray((0, 1, 2, 3))
>>> arr[1]
1

>>> # The bytearray repr:
>>> arr
bytearray(b'\x00\x01\x02\x03')

>>> # Bytearrays are mutable:
>>> arr[1] = 23
>>> arr
bytearray(b'\x00\x17\x02\x03')

>>> arr[1]
23

>>> # Bytearrays can grow and shrink in size:
>>> del arr[1]
>>> arr
bytearray(b'\x00\x02\x03')

>>> arr.append(42)
>>> arr
bytearray(b'\x00\x02\x03*')

>>> # Bytearrays can only hold `bytes`
>>> # (integers in the range 0 <= x <= 255)
>>> arr[1] = "hello"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer

>>> arr[1] = 300
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: byte must be in range(0, 256)
```

<div dir="rtl" style="font-size:30px; color:orange">
data classes
</div>

<div dir="rtl" style="font-size:18px">
با نوشتن یک کلاس داده به جای یک کلاس ساده پایتون، نمونه های شی شما چند ویژگی مفید را از جعبه دریافت می کنند که تایپ و کارهای پیاده سازی دستی را برای شما ذخیره می کند.
ویژگی های پیاده سازی یک دیتاکلس:

۱- دیگر لازم نیست کلاس __init__ بسازیم

۲- به طور خودکار کلاس __repr__ پیاده سازی شده است

۳- متغیر های موجود در کلاس اطلاعات بیشتری را باید داشته باشند که همین باعث میشود کد ما تا حدی خواناتر شود
</div>

```commandline
>>> from dataclasses import dataclass
>>> @dataclass
... class Car:
...     color: str
...     mileage: float
...     automatic: bool
...
>>> car1 = Car("red", 3812.4, True)

>>> # Instances have a nice repr:
>>> car1
Car(color='red', mileage=3812.4, automatic=True)

>>> # Accessing fields:
>>> car1.mileage
3812.4

>>> # Fields are mutable:
>>> car1.mileage = 12
>>> car1.windshield = "broken"

>>> # Type annotations are not enforced without
>>> # a separate type checking tool like mypy:
>>> Car("red", "NOT_A_FLOAT", 99)
Car(color='red', mileage='NOT_A_FLOAT', automatic=99)

```

<div dir="rtl" style="font-size:18px">
4.typing.NamedTuple

مثل مورد ۳ هست ولی دیگر نمیتوان مقدار کلاس رو عوض کرد
</div>

```commandline
>>> from typing import NamedTuple

>>> class Car(NamedTuple):
...     color: str
...     mileage: float
...     automatic: bool

>>> car1 = Car("red", 3812.4, True)

>>> # Instances have a nice repr:
>>> car1
Car(color='red', mileage=3812.4, automatic=True)

>>> # Accessing fields:
>>> car1.mileage
3812.4

>>> # Fields are immutable:
>>> car1.mileage = 12
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute

>>> car1.windshield = "broken"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Car' object has no attribute 'windshield'

>>> # Type annotations are not enforced without
>>> # a separate type checking tool like mypy:
>>> Car("red", "NOT_A_FLOAT", 99)
Car(color='red', mileage='NOT_A_FLOAT', automatic=99)

```

<div dir="rtl" style="font-size:18px">
5.types.SimpleNamespac

روش دیگری برای تعریف کلاس که شامل فقط متغیر هست
</div>

```commandline
>>> from types import SimpleNamespace
>>> car1 = SimpleNamespace(color="red", mileage=3812.4, automatic=True)

>>> # The default repr:
>>> car1
namespace(automatic=True, color='red', mileage=3812.4)

>>> # Instances support attribute access and are mutable:
>>> car1.mileage = 12
>>> car1.windshield = "broken"
>>> del car1.automatic
>>> car1
namespace(color='red', mileage=12, windshield='broken')

```

<div dir="rtl" style="font-size:30px; color:orange">
set and multiset
</div>

<div dir="rtl" style="font-size:18px">
از ساختمان داده های داخلی پایتون هست. قابل تغییر است و میشود آن را تغییر داد
</div>

```commandline
>>> vowels = {"a", "e", "i", "o", "u"}
>>> "e" in vowels
True

>>> letters = set("alice")
>>> letters.intersection(vowels)
{'a', 'e', 'i'}

>>> vowels.add("x")
>>> vowels
{'i', 'a', 'u', 'o', 'x', 'e'}

>>> len(vowels)
6

```

<div dir="rtl" style="font-size:18px">
نوع دیگری از set ها وجود دارد که قابلیت تغییر ندارند
</div>

```commandline
>>> vowels = frozenset({"a", "e", "i", "o", "u"})
>>> vowels.add("p")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'

>>> # Frozensets are hashable and can
>>> # be used as dictionary keys:
>>> d = { frozenset({1, 2, 3}): "hello" }
>>> d[frozenset({1, 2, 3})]
'hello'

```