<div dir="rtl" style="font-size:40px; color:yellow">
الگوی طراحی Prototype
</div>

<div dir="rtl" style="font-size:18px">
یکی از زیرشاخه های الگوهای طراحی، Creational Design Patterns است.
این الگو راهی جهت ساخت و ایجاد اشیاء (object) از کلاس ها را ارائه میدهد.
ساخت یک شیء با استفاده از new کردن آن کلاس در اصطلاح hard code کردن راه حل خوبی نیست و بهتر است از الگوهای طراحی Creational استفاده کرد.

الگوی Prototype به ما این امکان رو میده تا با Clone (کپی) کردن از نمونه‌های موجود، نمونه‌های جدیدی بسازیم.


چه زمانی از الگوی Prototype استفاده کنیم؟

از این الگو زمانی استفاده می‌کنیم که می‌خوایم یک Clone (کپی) از یک نمونه داشته باشیم. اما ساختن نمونه با کلمه کلیدی new هزینه‌های زیادی داره

</div>

<div dir="rtl" style="font-size:30px; color:yellow">
به زبون ساده:
</div>

<div dir="rtl" style="font-size:18px">
مشکل از اینجا شروع میشه که یک ابجکت دارید و نیاز دارید از اون یک کپی ایجاد کنین. چطوری این کار رو میکنین؟ اول باید یک ابجکت جدید از همون کلاس ایجاد کنین بعد باید مقادیر ابجکت اصلی رو در ابجکت جدید کپی کنید. حالا از همین پروسه طاقت فرسا که بگذریم، این مشکل وجود داره این هست که به متغیر‌های خصوصی دسترسی ندارید.دیزاین پترن Prototype میگه یک Interface مشترک داشته باشید که وظیفه‌ش ساخت یک ابجکت کپی از روی ابجکت فعلی باشه.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
مثال برنامه نویسی
</div>

<div dir="rtl" style="font-size:18px">
فرض کنید کلاس SomeComponent به این صورت تعریف شده:
</div>

```python
class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref
```

<div dir="rtl" style="font-size:18px">
پایتون magic method‌هایی برای این مساله در نظر گرفته که ماهم از همون دو تابع معروف copy و deep copy استفاده میکنیم:
</div>

```python
import copy

class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref
    
    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo={}):
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
    
        return new
```

<div dir="rtl" style="font-size:30px; color:yellow">
تفاوت Shadow Copy و Deep Copy ؟
</div>

<div dir="rtl" style="font-size:18px">
توی Shadow Copy، یک متغیر ساخته می‌شود و به مکانی توی حافظه، که مقدار متغیر قبلی توش قرار گرفته، اشاره می‌کنه. پس اگر شما مقدار متغیر اول رو تغییر بدین، متغیر دوم هم تغییر می‌کنه. و همین‌طور اگر مقدار متغیر دوم رو تغییر بدین، مقدار متغیر اول هم تغییر می‌کنه.

ولی توی deep copy، یک متغیر ساخته می‌شه و مقدار متغیر قبلی توی اون کپی می‌شه. در نتیجه تغییر ابجکت اول یا ابجکت کپی تغییری توی اون یکی به وجود نمیاره.
</div>
