<div dir="rtl" style="font-size:48px; text-align: justify">
typing
</div>


<div dir="rtl" style="font-size:28px; text-align: justify">
Annotated
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Annotated یک نوع از تایپینگ در پایتون است که برای افزودن توضیحات به تایپ‌ها استفاده می‌شود.

</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
علاوه بر توضیحات چیزهای اضافه و توابع annotated_types به آن اضافه کرد
</div>

```python
from typing import Annotated

def process_string(text: Annotated[str, "A string containing user input"]) -> None:
    pass
```

```python

# pip install annotated_types

from typing import Annotated
from annotated_types import Gt


def process_int(number: Annotated[int, Gt(1)]) -> None:
    print(number)

```

<div dir="rtl" style="font-size:18px; text-align: justify">
در پایتون به صورت خام فقط برای توضیحات هست ولی در پکیج های دیگه از این توضیحات استفاده میکنه برای validation متغیر
</div>

<div dir="rtl" style="font-size:28px; text-align: justify">
overload
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
این مفهوم به منظور افزایش انعطاف‌پذیری توصیف نوع ورودی و خروجی توابع مورد استفاده قرار می‌گیرد. با استفاده از overload، می‌توانید یک تابع را به گونه‌ای تعریف کنید که با ورودی‌های مختلف، نتایج مختلفی تولید کند.

</div>

```python
from typing import overload

@overload
def process_data(data: int) -> str:
    ...

@overload
def process_data(data: float) -> int:
    ...

def process_data(data):
    if isinstance(data, int):
        return str(data)
    elif isinstance(data, float):
        return int(data)
```


<div dir="rtl" style="font-size:18px; text-align: justify">
سوال :
</div>

```python
from typing import Literal

def get_data(self, output: Literal["json", "dict"] | None = None) -> str | dict:
        if output == "json" and isinstance(self._data, BaseModel):
            return self._data.json(indent=4)
        elif output == "dict" and isinstance(self._data, BaseModel):
            return self._data.dict()
        elif output is None and not isinstance(self._data, BaseModel):
            return str(self._data)
        else:
            raise AttributeError(f"The data object of type {type(self._data)} does not support the '{output}' operation.")
```

<div dir="rtl" style="font-size:18px; text-align: justify">
تبدیل میشه به:
</div>

```python
from typing import overload, Literal 

@overload
def get_data(self, output: Literal["json"]) -> str:
   ... 

@overload
def get_data(self, output: Literal["dict"]) -> dict:
   ... 

def get_data(self, output: Literal["json", "dict"] | None) -> str | dict:
    # Code
```

<div dir="rtl" style="font-size:28px; text-align: justify">
ANY
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
در تایپینگ پایتون، Any یک نوع خاص است که به معنای "هر نوعی" است. به عبارت دیگر، می‌توانید از Any برای تعریف متغیر یا پارامتری استفاده کنید که نوع دقیق آن را نمی‌دانید یا ممکن است انواع مختلفی از داده‌ها در آن استفاده شود.
</div>

```python
from typing import Any

def process_data(data: Any) -> None:
    pass
```


<div dir="rtl" style="font-size:18px; text-align: justify">
سعی کنم به جای استفاده زیاد از ANY که نوع آن هارو نمیدونم از object استفاده کنم چون هرچیزی در پایتون از object ایجاد شده
</div>

```python
from example import Widget

class BlueWidget(Widget):
    def __init__(self, *args: object, blueness: int = 50, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        self.blueness = blueness
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Callable
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Callable یک نوع تایپینگ در پایتون است که برای نمایاندن توابع و متغیرهایی استفاده می‌شود که فراخوانی پذیر هستند. به عبارت دیگر، اگر می‌خواهید یک متغیری را تعریف کنید که به عنوان یک تابع مورد استفاده قرار می‌گیرد، می‌توانید از Callable استفاده کنید.
</div>

```python
from typing import Callable

def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(x: int, y: int) -> int:
    return x + y

result = apply_function(add, 3, 5)
print(result)

```

<div dir="rtl" style="font-size:28px; text-align: justify">
ClassVar
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
ClassVar یک نوع تایپینگ در پایتون است که برای تعریف متغیرهای کلاسی با استفاده از توابع پایتون به منظور توابع مشخص‌تر کردن و تایپ‌ها استفاده می‌شود. این نوع متغیرها به کلاس‌ها اختصاص دارند و نه به نمونه‌هایی از آن کلاس.
</div>

```python
from typing import ClassVar

class MyClass:
    count: ClassVar[int] = 0
    description: ClassVar[str] = "This is a class variable."

    def __init__(self, value: int):
        self.value = value
        MyClass.count += 1
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Final
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Final یک نوع تایپینگ در پایتون است که برای نشان دادن توالی‌های نهایی (final sequences) در تایپ‌ها استفاده می‌شود. توالی‌های نهایی توالی‌هایی هستند که پس از ایجاد، نمی‌توانند تغییر کنند. این نوع تایپینگ به شما اجازه می‌دهد تا محدودیت‌های تغییر ناپذیری را در تایپ‌های خود اعمال کنید.
</div>

```python
from typing import Final, List
from abc import ABC, abstractmethod

CONSTANT_NUMBERS: Final[List[int]] = [1, 2, 3, 4, 5]

PI: Final[float] = 3.14159

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self) -> str:
        pass

class ChildClass(AbstractClass):
    def abstract_method(self) -> Final[str]:
        return "Implementation in the child class."
```

<div dir="rtl" style="font-size:28px; text-align: justify">
ForwardRef
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
ForwardRef یک کلاس در ماژول typing در پایتون است که برای ایجاد یک مرجع به یک توالی یا نوع از پیش تعریف شده در زمان اجرا (runtime) استفاده می‌شود. این ابزار به شما اجازه می‌دهد که به توابع یا کلاس‌ها که تا زمان اجرا تعریف می‌شوند، ارجاع دهید.</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
مثلا وقتی که import کردن کلاس یا فایل باعث خطا بشه استفاده از این میتونه مشکل رو حل کنه
</div>

```python
from typing import ForwardRef

def create_recursive_function() -> ForwardRef('RecursiveFunction'):
    def recursive_function(value: int) -> int:
        if value <= 0:
            return 0
        return value + recursive_function(value - 1)
    
    return recursive_function
```

<div dir="rtl" style="font-size:18px; text-align: justify">
مثال دیگه
</div>

```python

from typing import ForwardRef, List

def recursive_function(data: List[ForwardRef("Node")]) -> None:
    pass

class Node:
    pass
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Generic
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Generic یک قابلیت در تایپینگ پایتون است که برای ایجاد کلاس‌ها یا توابع ژنریک (generic classes/functions) با قابلیت عمومی (generic) و اعمال چندین نوع مختلف در زمان اجرا (runtime) استفاده می‌شود. این ابزار به شما اجازه می‌دهد تا توابع و کلاس‌ها را به گونه‌ای بنویسید که با انواع مختلف داده‌ها سازگار باشند.

</div>

```python
from typing import Generic, TypeVar, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return not bool(self.items)


if __name__ == '__main__':
    stack1 = Stack[int]()
    stack1.push(1)
```

<div dir="rtl" style="font-size:18px; text-align: justify">
تو پایتون نسخه ۳.۱۲ سینتکس بهتر شده:
</div>

```python
from typing import List

# in python 3.12

class NewStack[T]:
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return not bool(self.items)


if __name__ == '__main__':
    stack1 = NewStack[int]()
    stack1.push(1)
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Literal
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Literal یک کلاس در ماژول typing در پایتون است که برای تعریف توالی‌های ثابت (literal sequences) از مقادیر استفاده می‌شود. این ابزار به شما اجازه می‌دهد تا توالی‌های ثابت از مقادیر مختلف را به عنوان نوع‌های ممکن برای یک متغیر یا ورودی تابع مشخص کنید.
</div>

```python
from typing import Literal

gender: Literal["Male", "Female", "Other"] = "Male"
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Optional
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Optional یک کلاس در ماژول typing در پایتون است که برای نمایاندن اینکه یک متغیر می‌تواند مقدار داشته باشد یا نداشته باشد، به کار می‌رود. این ابزار به شما اجازه می‌دهد تا تعیین کنید آیا یک متغیر باید دارای مقدار (مقداردهی شده) باشد یا می‌تواند مقدار نداشته باشد (مقداردهی نشده).

</div>

```python
from typing import Optional

def greet(name: Optional[str]) -> str:
    if name is not None:
        return f"Hello, {name}!"
    else:
        return "Hello, Guest!"
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Protocol
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Protocol یک کلاس در ماژول typing در پایتون است که برای تعریف و تایپینگ یک پروتکل (protocol) استفاده می‌شود. پروتکل‌ها به شما اجازه می‌دهند تا مشخص کنید که یک کلاس یا یک شیء باید از ویژگی‌ها و متدهای خاصی پیروی کند.
</div>

```python
from typing import Protocol

class Printable(Protocol):
    def __str__(self) -> str:
        ...

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} ({self.age} years old)"

def print_person(p: Printable) -> None:
    print(str(p))

person = Person("Alice", 30)
print_person(person)  # output: "Alice (30 years old)"

```

<div dir="rtl" style="font-size:28px; text-align: justify">
Tuple
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Tuple در تایپینگ پایتون یک کلاس است که برای تعریف توالی‌ها (sequences) از انواع داده مختلف به کار می‌رود. توالی‌ها می‌توانند مقادیر مختلف را در یک ترتیب خاص نگه دارند.
</div>

```python
from typing import Tuple

numbers: Tuple[int, int, int] = (1, 2, 3)

mixed_data: Tuple[int, str, float] = (42, "Hello", 3.14)

all_str_tuple: Tuple[str, ...] = ("mehran", "kamrani", "Adtrace")
```


<div dir="rtl" style="font-size:28px; text-align: justify">
Type
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Type یک کلاس در ماژول typing در پایتون است که برای نشان دادن نوع (type) یک کلاس یا نوع داده مورد استفاده قرار می‌گیرد. این کلاس به شما اجازه می‌دهد تا نوعی که یک متغیر، یک شیء یک کلاس دارد را مشخص کنید.
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
این تایپنگ برای شی نیست و فقط برای پاس دادن کلاس استفاده میشه
</div>

```python
from typing import Type

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

person_type: Type[Person] = Person
```

<div dir="rtl" style="font-size:28px; text-align: justify">
TypeVar
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
TypeVar یک کلاس در ماژول typing در پایتون است که برای تعریف متغیرهای نوعی (type variables) در تایپینگ استفاده می‌شود. متغیرهای نوعی به شما اجازه می‌دهند تا نوع‌های مختلفی را به عنوان ورودی‌ها یا خروجی‌ها در توابع و کلاس‌ها مشخص کنید.
</div>

```python
from typing import TypeVar, List

T = TypeVar('T') 

def find_element(lst: List[T], target: T) -> int:
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Union
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Union یک کلاس در ماژول typing در پایتون است که برای نشان دادن اینکه یک متغیر یا مقدار می‌تواند یکی از چند نوع مختلف داشته باشد به کار می‌رود. این کلاس به شما اجازه می‌دهد تا نوع‌های متغیرها را به صورت جداگانه تعیین کنید.
</div>

```python
from typing import Union

value: Union[int, str, float] = 42

value1: Union[int, str, float] = 42
value2: Union[int, str, float] = "Hello"
value3: Union[int, str, float] = 3.14
```

<div dir="rtl" style="font-size:18px; text-align: justify">
که تو ورژن 3.11 پایتون به این شکل استفاده میشه:
</div>

```python
value: int| str| float = 42
```

<div dir="rtl" style="font-size:28px; text-align: justify">
AbstractSet
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
کلاس‌های مجموعه در پایتون باید تعدادی متد و ویژگی خاص را پیاده‌سازی کنند تا عملیات‌های مجموعه‌ای مانند افزودن عناصر، حذف عناصر، اجتماع، اشتراک و ... را انجام دهند. AbstractSet این ویژگی‌ها و متدها را به عنوان واسط (interface) تعریف می‌کند تا کلاس‌های مجموعه بتوانند از آن ارث بری کنند و آن‌ها را پیاده‌سازی کنند.
برای استفاده از فقط متدهای __contains__ , __iter__ , __len__ را باید پیاده سازی کنیم.
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
تایپ Set هم از این ارثبری کرده و همین ویژگی هارو داره ولی اگه مجموعه ای میخوایم که custom خود ما باشه باید از AbstractSet استفاده کنیم
</div>

```python
from typing import AbstractSet

class MySet(AbstractSet):
    def __init__(self, data):
        self.data = set(data)
    
    def __contains__(self, item):
        return item in self.data
    
    def __iter__(self):
        return iter(self.data)
    
    def __len__(self):
        return len(self.data)
```

<div dir="rtl" style="font-size:28px; text-align: justify">
ByteString
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
ByteString یک نوع داده در تایپینگ پایتون است که برای نمایش داده‌های بایت (byte) به کار می‌رود. این نوع داده معمولاً برای کار با داده‌های دودویی و داده‌هایی که به صورت بایت‌ها ذخیره می‌شوند مورد استفاده قرار می‌گیرد.
</div>

```python
from typing import ByteString

def write_binary_data(data: ByteString) -> None:
    with open('binary_data.bin', 'wb') as file:
        file.write(data)

binary_data = b'\x48\x65\x6C\x6C\x6F'
write_binary_data(binary_data)
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Container
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Container یک کلاس در ماژول typing در پایتون است که برای نمایش اینکه یک متغیر یا مقدار می‌تواند شامل چند عنصر یا عناصری از یک نوع مختلف باشد به کار می‌رود. این کلاس به شما اجازه می‌دهد تا نوع متغیرها را به عنوان یک مجموعه از انواع مختلف مشخص کنید.
</div>

```python
from typing import Container

class MyContainer(Container):
    def __init__(self, elements):
        self.elements = elements

    def __contains__(self, item):
        return item in self.elements

my_container: Container = MyContainer([1, 2, 3, 4, 5])

element_to_check = 3
if element_to_check in my_container:
    print(f"The element {element_to_check} is in the container.")
else:
    print(f"The element {element_to_check} is not in the container.")
```

<div dir="rtl" style="font-size:28px; text-align: justify">
ContextManager
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
در typing پایتون، ContextManager یک نوع داده است که برای تعریف منابع مدیریت شده (managed resources) در تایپینگ به کار می‌رود. این نوع داده به عنوان ورودی و خروجی توابع وسوسه‌گرهای (context managers) استفاده می‌شود که به شما اجازه می‌دهد منابع را مدیریت کنید.

معمولاً از وسوسه‌گرهای contextlib برای تعریف منابع مدیریت شده در تایپینگ استفاده می‌شود. این نوع از تایپینگ به برنامه‌نویسان کمک می‌کند تا تضمین کنند که منابع به درستی مدیریت می‌شوند و همچنین از مزایای استفاده از منابع مدیریت شده در کد خود

بهره‌برند.</div>

```python
from typing import ContextManager
from contextlib import contextmanager

@contextmanager
def my_file_manager(filename: str, mode: str) -> ContextManager:
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with my_file_manager("example.txt", "w") as file:
    file.write("Hello, Context Managers!")
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Hashable
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Hashable یک نوع داده در typing پایتون است که برای نمایش اینکه یک متغیر قابل هش کردن (hashable) است یا نه به کار می‌رود. اشیاء قابل هش کردن به عنوان کلید‌های دیکشنری‌ها (dictionaries) در پایتون مورد استفاده قرار می‌گیرند.
</div>

```python
from typing import Hashable

def calculate_hash(key: Hashable) -> int:
    return hash(key)

my_key = "example"
hash_value = calculate_hash(my_key)
print(f"Hash value of the key: {hash_value}")
```

<div dir="rtl" style="font-size:28px; text-align: justify">
ItemsView
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
ItemsView یک نوع داده در typing پایتون نیست. به جای آن، این معمولاً به عنوان یک نوع مربوط به دیکشنری‌ها در پایتون شناخته می‌شود. در واقعیت، ItemsView یک نوع ویو (view) در پایتون است که به شما امکان می‌دهد به عنوان یک نمای کلی دسترسی به مقادیر و کلیدهای یک دیکشنری داشته باشید.
</div>

```python
from typing import ItemsView

my_dict = {'apple': 3, 'banana': 5, 'cherry': 8}
items_view: ItemsView = my_dict.items()
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Iterable
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Iterable یک نوع داده در typing پایتون است که به عنوان یک ویژگی برای اشیاء استفاده می‌شود تا نشان دهد که می‌توانند در یک حلقه for در پایتون تکرار شوند. اشیاء Iterable از ویژگی‌هایی مانند __iter__ و __next__ پشتیبانی می‌کنند.

اگر متغیر ما ممکن باشد از نوع List و Tuple و Dict باشد به جای Union میتونیم از این استفاده کنیم.
</div>

```python
from typing import Iterable

def iterate_over_items(items: Iterable[int]):
    for item in items:
        print(item)

my_list = [1, 2, 3, 4, 5]
iterate_over_items(my_list)

```

<div dir="rtl" style="font-size:28px; text-align: justify">
Iterator
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Iterator یک نوع داده در typing پایتون است که برای نمایاندن اشیاءی استفاده می‌شود که می‌توانند در یک حلقه تکرار شوند و از ویژگی‌هایی مانند __iter__ و __next__ پشتیبانی می‌کنند.

اگر خروجی یا متغیر ما یک Iterator باشه مثل yield از این برای شناسایی مقداری که این iterator برمیگردونه استفاده میشود.
</div>

```python
from typing import Iterator

class MyIterator:
    def __init__(self, max_limit):
        self.max_limit = max_limit
        self.current = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self):
        if self.current < self.max_limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

my_iterator: Iterator[int] = MyIterator(5)

for item in my_iterator:
    print(item)

def generate_number(n:int) -> Iterator[int]:
    for i in range(n):
        yield i
```

<div dir="rtl" style="font-size:28px; text-align: justify">
KeysView
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
KeysView یک نوع داده در typing پایتون است که برای نمایاندن نمایه (view) از کلیدهای یک دیکشنری (dictionary) استفاده می‌شود. این نمایه نسبت به دیکشنری اصلی، قابلیت تکرار و دسترسی به کلیدها را فراهم می‌کند. KeysView معمولاً در تایپینگ به عنوان تایپ اطلاعاتی برای ویژگی‌هایی که کلیدها را از یک دیکشنری باز می‌گردانند، استفاده می‌شود.
</div>

```python
from typing import KeysView

my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}

def print_keys(keys_view: KeysView[str]):
    for key in keys_view:
        print(key)

keys = my_dict.keys()
print_keys(keys)
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Mapping
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
مثل Dict میمونه با این تفاوت که هر نوع ساختاری رو میپذیره مثل Orderdict, defaultdict, chainMap,...
</div>



<div dir="rtl" style="font-size:28px; text-align: justify">
MappingView
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
در واقعیت، MappingView یک ویژگی از دیکشنری‌ها (Dictionaries) در پایتون است که به صورت خودکار توسط متدهایی مانند items() بر روی دیکشنری‌ها ایجاد می‌شود. این ویژگی به شما امکان مشاهده مقادیر در دیکشنری‌ها به صورت جفت کلید و مقدار را می‌دهد. از آن به عنوان یک ویژگی عملی در پایتون برای دسترسی به عناصر دیکشنری‌ها استفاده می‌شود،
</div>

```python
from typing import MappingView, Mapping

my_dict: Mapping[str, int] = {'apple': 3, 'banana': 5, 'cherry': 2}

mapping_view: MappingView[str,int] = my_dict.items()
```

<div dir="rtl" style="font-size:28px; text-align: justify">
MutableMapping
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
MutableMapping یک تایپ مخصوص به typing در پایتون است که برای نمایاندن ساختار‌های داده‌ای قابل تغییر مانند دیکشنری‌ها (Dictionaries) و مپ‌ها (Mappings) با امکان افزودن، حذف، و تغییر عناصر به کار می‌رود. این تایپ نشان می‌دهد که می‌توانید دستکاری و تغییرات در دیکشنری‌ها و مپ‌ها انجام دهید.
</div>

```python
from typing import MutableMapping

def add_to_dict(data: MutableMapping[str, int], key: str, value: int) -> None:
    data[key] = value

my_dict = {'apple': 3, 'banana': 5}
add_to_dict(my_dict, 'cherry', 2)
```

<div dir="rtl" style="font-size:28px; text-align: justify">
MutableSequence
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
MutableSequence یک تایپ مخصوص به typing در پایتون است که برای نمایاندن ساختار‌های داده‌ای قابل تغییر مانند لیست‌ها (Lists) و تاپل‌های قابل تغییر (Mutable Tuples) با امکان افزودن، حذف، و تغییر عناصر به کار می‌رود. این تایپ نشان می‌دهد که می‌توانید دستکاری و تغییرات در داده‌ها اعمال کنید.
</div>

```python
from typing import MutableSequence

def remove_item(data: MutableSequence[int], item: int) -> None:
    if item in data:
        data.remove(item)

my_list = [3, 5, 2, 7, 3]
remove_item(my_list, 5)
```

<div dir="rtl" style="font-size:28px; text-align: justify">
MutableSet
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
MutableSet یک تایپ مخصوص به typing در پایتون است که برای نمایاندن ساختار‌های داده‌ای قابل تغییر مانند مجموعه‌ها (Sets) با امکان افزودن، حذف، و تغییر عناصر به کار می‌رود. این تایپ نشان می‌دهد که می‌توانید دستکاری و تغییرات در داده‌ها اعمال کنید.
</div>

```python
from typing import MutableSet

def remove_item(data: MutableSet[int], item: int) -> None:
    if item in data:
        data.remove(item)

my_set = {3, 5, 2, 7, 3}
remove_item(my_set, 5)
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Sequence
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
در typing پایتون، Sequence یک تایپ مخصوص است که برای نمایاندن ساختار‌های داده‌ای مشابه ترتیبی مانند لیست‌ها (Lists)، رشته‌ها (Strings) و تاپل‌ها (Tuples) با استفاده از شاخص‌ها برای دسترسی به عناصر به کار می‌رود. Sequence نشان می‌دهد که عناصر مجموعه به ترتیب خاصی ذخیره شده‌اند و می‌توان با استفاده از اندیس‌ها به آن‌ها دسترسی داشت.
</div>

```python
from typing import Sequence

def get_first_element(data: Sequence[int]) -> int:
    return data[0]

my_list = [3, 5, 2, 7]
first_element = get_first_element(my_list)
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Sized
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Sized یک تایپ مخصوص به typing در پایتون است که برای نمایاندن ساختار‌های داده‌ای که اندازه‌گیری پذیر هستند مانند لیست‌ها (Lists)، رشته‌ها (Strings) و دیگر مشابه ترتیبی با استفاده از تابع داخلی len() به کار می‌رود. این تایپ نشان می‌دهد که می‌توانید اندازه (تعداد عناصر) این ساختار‌های داده‌ای را بدست آورید.
</div>

```python
from typing import Sized

def get_length(data: Sized) -> int:
    return len(data)

my_list = [3, 5, 2, 7]
length = get_length(my_list)
```


<div dir="rtl" style="font-size:28px; text-align: justify">
ValuesView
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
    ValuesView در واقع یک نوع داده در پایتون نیست و نیاز به تعریف آن به عنوان تایپ در typing وجود ندارد. اشتباهاً در پیش‌نمایش‌های گذشته اطلاعات اشتباهی ارائه دادم و معذرت می‌خواهم.
</div>

```python
from typing import ValuesView, Mapping

my_dict: Mapping[str, int] = {'apple': 3, 'banana': 5, 'cherry': 2}
values_view: ValuesView[int] = my_dict.values()
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Awaitable
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
Awaitable یک تایپ در typing پایتون است که به نمایاندن اشیاء قابل انتظار (awaitable objects) برای استفاده در کد همروند (concurrent) و انتظار (awaiting) توابع async/await در پایتون می‌پردازد. این تایپ به شما این امکان را می‌دهد که بگویید یک شیء می‌تواند به عنوان مقدار منتظر شدنی (awaitable value) در یک تابع async استفاده شود.

Awaitable معمولاً برای نمایاندن اشیاءی مانند تسک‌ها (Tasks) و فریموورک‌های مبتنی بر async در پایتون استفاده می‌شود. این اشیاء به کار می‌روند تا اجرای همروند کد در برنامه‌های پایتون را مدیریت کنند.
</div>

```python
from typing import Awaitable
import asyncio

async def my_async_function() -> Awaitable[int]:
    await asyncio.sleep(1)
    return 42
```

<div dir="rtl" style="font-size:28px; text-align: justify">
AsyncIterator
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
AsyncIterator یک تایپ در ماژول typing پایتون است که برای نمایاندن اشیاء قابل ایتره شدن (iterable objects) در کدهای همروند (concurrent) با استفاده از توابع async/await به کار می‌رود. این تایپ به شما امکان می‌دهد تعیین کنید که یک شیء می‌تواند در یک کد همروند به عنوان یک ایتریتور مورد استفاده قرار گیرد.

AsyncIterator معمولاً برای نمایاندن اشیاءی که می‌توانند در توابع async ایتره شوند، مورد استفاده قرار می‌گیرد. این اشیاء معمولاً توسط توابع __aiter__() و __anext__() ایجاد می‌شوند و به شما امکان می‌دهند از آن‌ها در توابع async با استفاده از await و async for استفاده کنید.

به طور کلی مثل Iterator هست
</div>

```python
import asyncio
from typing import AsyncIterator

class MyAsyncIterable:
    async def __aiter__(self) -> AsyncIterator[int]:
        for i in range(5):
            yield i
            await asyncio.sleep(1)
```

<div dir="rtl" style="font-size:28px; text-align: justify">
AsyncIterable
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
مثل Iterable هست 
</div>

<div dir="rtl" style="font-size:28px; text-align: justify">
SupportsFloat
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
اگر داده ما شرایط این رو داشته باشد که به float تبدیل شوند در این صورت میتوانیم از این استفاده کنیم
</div>

```python
from typing import SupportsFloat, List

def calculate_average(numbers: List[SupportsFloat]):
    total = sum(float(n) for n in numbers)
    return total / len(numbers)

calculate_average(numbers=["30.5", 10])
```

<div dir="rtl" style="font-size:28px; text-align: justify">
SupportsInt
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
اگر داده ما شرایط این رو داشته باشد که به int تبدیل شوند در این صورت میتوانیم از این استفاده کنیم
</div>

```python
from typing import SupportsInt, List

def calculate_average(numbers: List[SupportsInt]):
    total = sum(int(n) for n in numbers)
    return total / len(numbers)

calculate_average(numbers=["30", 10])
```

<div dir="rtl" style="font-size:28px; text-align: justify">
SupportsRound
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
اگر داده ما شرایط این رو داشته باشد که بتواند به عدد round تبدیل شوند در این صورت میتوانیم از این استفاده کنیم
</div>

<div dir="rtl" style="font-size:28px; text-align: justify">
SupportsIndex
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
دنباله هایی که دارای index هستند مثل List, tupple,...
</div>


<div dir="rtl" style="font-size:28px; text-align: justify">
Reversible
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
ابجکت هایی که قابلیت معکوس کردن داده ها را دارند.
</div>

<div dir="rtl" style="font-size:28px; text-align: justify">
TypedDict
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
TypedDicts می‌تواند برای بهبود خوانایی و قابلیت نگهداری کد استفاده شود. استفاده از TypedDicts به خوانندگان کد می‌گوید که انتظار می‌رود یک مقدار از چه نوع داده ای باشد. همچنین، TypedDicts می‌تواند برای اطمینان از ایمنی نوع استفاده شود. استفاده از TypedDicts می‌تواند به جلوگیری از خطاهای ناشی از استفاده از مقادیر غیرمنتظره جلوگیری کند.

در اینجا چند مزیت استفاده از TypedDicts آورده شده است:

بهبود خوانایی کد: استفاده از TypedDicts به خوانندگان کد می‌گوید که انتظار می‌رود یک مقدار از چه نوع داده ای باشد. این می‌تواند کد را برای خوانندگان جدیدتر یا ناآشنا با کد شما آسان‌تر کند.
بهبود قابلیت نگهداری کد: استفاده از TypedDicts می‌تواند به شما کمک کند تا کد خود را پایدار نگه دارید. اگر نوع یک مقدار تغییر کند، TypedDict می‌تواند به شما هشدار دهد.
بهبود ایمنی نوع: استفاده از TypedDicts می‌تواند به جلوگیری از خطاهای ناشی از استفاده از مقادیر غیرمنتظره جلوگیری کند. این می‌تواند به شما کمک کند تا کد خود را ایمن‌تر نگه دارید.
</div>

```python
from typing import TypedDict

class SalesSummary(TypedDict):
    sales: int
    country: str
    product_codes: list[str]


def get_sales_summary() -> SalesSummary:
    """Return summary for yesterday’s sales."""
    return {
        "sales": 1_000,
        "country": "UK",
        "product_codes": ["SUYDT"],
    }
```

<div dir="rtl" style="font-size:28px; text-align: justify">
Type
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
گاهی اوقات میخواهیم یک کلاس مستقیم پاس بدیم نه یک ابجکت از اون کلاس:
</div>

```python
from typing import Type

...


def make_animal(animal_class: Type[Animal], name: str) -> Animal:
    return animal_class(name=name)
```

<div dir="rtl" style="font-size:28px; text-align: justify">
TypeGuard
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
مشخص میکند که ایا این متغیر دارای شرایطی که تعریف میکنیم هست یا نه. این typing در تابع یا لامبدا اجرا میشه:
</div>

```python
from __future__ import annotations

from typing_extensions import TypeGuard


def is_even(value: int) -> TypeGuard[int]:
    """Is the value even?"""
    return value % 2 == 0


x: int

reveal_type(x)
if is_even(x):
    reveal_type(x)
```

```python
from typing_extensions import TypeGuard

x: TypeGuard[lambda value: value == "hello"]

```

<div dir="rtl" style="font-size:28px; text-align: justify">
نکات
</div>

<div dir="rtl" style="font-size:23px; text-align: justify">
برای kwargs** , *args چند روش برای مشخص کردن typing داریم:
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
۱- اگر میدونی که از نوع ساده هستند مثلا int هستند:
</div>

```python
def variable(*args: int, **kwargs: int) -> None:
    ...

variable(1, 2, 3, a=4, b=5, c=6)

```

<div dir="rtl" style="font-size:18px; text-align: justify">
۲- اگر نوع داده پیچیده تر باشه:
</div>

```python
from typing import List, Dict

def my_function(**kwargs: Dict[str, int], *args: List[str]) -> None:
    pass

```

<div dir="rtl" style="font-size:18px; text-align: justify">
۲- اگر بخوایم کنترل بیشتری داشته باشیم از TypeDict استفاده کنیم:
</div>

```python
from typing import TypedDict

class PersonTypedDict(TypedDict):
    name: str
    age: int
    address: str

def my_function(**kwargs: PersonTypedDict, *args: List[str]) -> None:
    pass

```

<div dir="rtl" style="font-size:23px; text-align: justify">
برای وقتی که از یک api یک متغیری دریافت میکنیم که با پایتون همخوانی ندارد مثلا اسم متغیر اینه: date-time:
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
۲- اگر بخوایم کنترل بیشتری داشته باشیم از TypeDict استفاده کنیم:
</div>

```python
import datetime as dt
from typing import TypedDict

Event = TypedDict("Event", {"date-time": dt.datetime})
```

<div dir="rtl" style="font-size:23px; text-align: justify">
با استفاده از پکیج pyupgrade میتونیم نوع های توابعمون رو درست کنیم:
</div>

```python
def old_function(x):
    if isinstance(x, list):
        return len(x)
    elif isinstance(x, dict):
        return len(x.keys())

```

```console
pyupgrade --write old_function.py
```

```python
def new_function(x: List[Any]) -> int:
    return len(x)


def new_function(x: Dict[str, Any]) -> int:
    return len(x.keys())
```

