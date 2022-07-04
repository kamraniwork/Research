<div dir="rtl" style="font-size:18px">
یکی از زیرشاخه های الگوهای طراحی، Creational Design Patterns است.
این الگو راهی جهت ساخت و ایجاد اشیاء (object) از کلاس ها را ارائه میدهد.
ساخت یک شیء با استفاده از new کردن آن کلاس در اصطلاح hard code کردن راه حل خوبی نیست و بهتر است از الگوهای طراحی Creational استفاده کرد.

الگوی Prototype به ما این امکان رو میده تا با Clone (کپی) کردن از نمونه‌های موجود، نمونه‌های جدیدی بسازیم.


چه زمانی از الگوی Prototype استفاده کنیم؟

از این الگو زمانی استفاده می‌کنیم که می‌خوایم یک Clone (کپی) از یک نمونه داشته باشیم. اما ساختن نمونه با کلمه کلیدی new هزینه‌های زیادی داره

به عنوان مثال:
</div>

```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.contant = self.fetch_content_from_db()
    
    def fetch_content_from_db(self):
        # contant = Book.objects.get(title=self.title).contant
        contant = "The book contatnt"
        return contant
```

<div dir="rtl" style="font-size:18px">
همانطور که در کد بالا مشاهده میکنید متغیر contant شامل متن کتاب و عکس ها است و یک کتاب حداقل ۴۰۰ صفحه دارد 

پس هر بار که ما شی از ** همون کتاب **ایجاد میکنیم تمام این مراحل انجام میشه و بار زیادی به دیتابیس وارد میکنه
راه حلی وجود داره که وقتی شی جدید ایجاد میشه ما از کد زیر استفاده کنیم:

</div>

```python
class Book:
    def __init__(self, title, price, contant=None):
        self.title = title
        self.price = price
        self.contant = contant if contant != None else self.fetch_content_from_db()

    def fetch_content_from_db(self):
        # contant = Book.objects.get(title=self.title).contant
        contant = "The book contatnt"
        return contant

    def clone(self):
        clone_obj = self.contant + '(cached)'
        return Book(title=self.title, price=self.price, contant=clone_obj)

    def __str__(self):
        return f"title={self.title}, price={self.price}, contant={self.contant}"

```

<div dir="rtl" style="font-size:18px">
در کد بالا تغییراتی که دادم اینطور است که یک تابع clone نوشتم که در اون مقدار قبلی متغیر contant ذخیره شده بود و نیازی نبود که دوباره به دیتابیس درخواستی فرستاده شود و تونستم بدون اینکه درخواست سنگین به دیتابیس بدم یک شی از همون کتاب بسازم 

معایب الگوی Prototype

۱. کپی گرفتن از یک آبجکت پیچیده با پراپرتی‌های زیاد و تو در تو کار دشوار و ظریفی خواهد بود
</div>

