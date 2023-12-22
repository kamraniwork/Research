<div dir="rtl" style="font-size:40px; color:yellow">
الگوی طراحی Bridge
</div>


<div dir="rtl" style="font-size:18px">
برای جداکردن یک کلاس به دو بخش مستقل از هم ولی وابسته به کلاس های دیگر استفاده میشود.
این الگو در کلاس پل در متد __init__ یک شی میگیرد که از این شی در توابع خود استفاده کرده و متد لازم را صدا میزند
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
یک مثال از دنیای واقعی:
</div>

<div dir="rtl" style="font-size:18px">
    فرض کنید یک وبسایت دارید و می‌خواید با توجه به تنظیمات کاربر از قالب‌های مختلف پشتیبانی کنید.برای انجام این کار چطور عمل می‌کنین؟به ازای هر قالب یک کپی از وبسایت ایجاد میکنید و قالب مخصوص براش اضافه میکنید؟یا قالب‌های مختلفی ایجاد میکنید با توجه به تنظیمات کاربر اون‌ها رو بارگذاری میکنید؟الگوی طراحی Bridge به شما کمک میکنه راه حل دوم رو پیاده‌سازی کنید.
</div>


<div dir="rtl" style="font-size:30px; color:yellow">
به زبون ساده:
</div>

<div dir="rtl" style="font-size:18px">
    این الگوی طراحی درمورد ترجیح دادن ترکیب نسبت به ارث‌بری صحبت میکنه.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
پیاده سازی: 
</div>

<div dir="rtl" style="font-size:18px">
در مرحله اول کلاس WebPage و پیاده‌سازی‌هایی از اون رو داریم:
</div>

```python
class WebPage:
    _theme = None

    def __init__(self, theme):
        self.theme = theme

    def getContent(self):
        pass


class About(WebPage):
    def getContent(self):
        return "quotAbout page in quot" + self.theme.getColor()


class Careers(WebPage):
    def getContent(self):
        return "quotCareers page in quot" + self.theme.getColor()
```

<div dir="rtl" style="font-size:18px">
برای قالب هم، باید کلاس و پیاده سازی‌های مختلفی بنویسیم:
</div>

```python
class Theme:
    def getColor(self):
        pass


class DarkTheme(Theme):
    def getColor(self):
        return 'Dark Black'


class LightTheme(Theme):
    def getColor(self):
        return 'Off White'


class AquaTheme(Theme):
    def getColor(self):
        return 'Light Blue'
```

<div dir="rtl" style="font-size:18px">
حالا میتونید نحوه ترکیب کردن این دو تاروو باهم ببینید:
</div>

```python
darkTheme = DarkTheme()

about = About(darkTheme)
careers = Careers(darkTheme)

print(about.getContent())
print(careers.getContent())
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
