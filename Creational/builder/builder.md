<div dir="rtl" style="font-size:18px">
یکی از زیرشاخه های الگوهای طراحی، Creational Design Patterns است.
این الگو راهی جهت ساخت و ایجاد اشیاء (object) از کلاس ها را ارائه میدهد.
ساخت یک شیء با استفاده از new کردن آن کلاس در اصطلاح hard code کردن راه حل خوبی نیست و بهتر است از الگوهای طراحی Creational استفاده کرد.


این الگو به ما این امکان رو میده تا به صورت مرحله به مرحله، یک آبجکت پیچیده رو بسازیم. الگوی Builder مرحله‌های ساختن
آبجکت رو برای ما تعریف می‌کنه و با اونها می‌تونیم آبجکت‌های متنوعی بسازیم.

استفاده از دیزاین پترن Builder موجب کاهش پیچیدگی ها در ساخت اشیاء میشود.

برای مثال:
</div>

```python
class Pizza:
    name = ''
    spicy = False
    sauce = False
    cheese = False

```

<div dir="rtl" style="font-size:18px">
یک کلاس شامل متغیر های اولیه که نام پیتزا و سس و فلفل و پنیر  هست که به صورت boolean تعریف شده اند و اگر کاربر نیازی به آن نداشته باشد مقدارد False و اگر بخواهد مقدار True خواهد بود
</div>

```python
class PizzaBuilder(Pizza):

    def name(self, name):
        self.name = name
        return self

    def add_sauce(self):
        self.sauce = True
        return self

    def add_pepperoni(self):
        self.spicy = True
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def __str__(self):
        result = self.name + "\n"
        result += "Has Spicy\n" if self.spicy else ""
        result += "Has Sauce\n" if self.sauce else ""
        result += "Has Cheese\n" if self.cheese else ""
        return result

```

<div dir="rtl" style="font-size:18px">
در کلاس اصلی هر متغیری که تغییر داده شده مثلا در تابع add_cheese که متغیر cheese تغییر داده شده است باید مقدار خود کلاس بازگردد تا بتوانیم دوباره از اون شی استفاده کنیم
</div>

```python
if __name__ == "__main__":
    pizza = PizzaBuilder().name("Peperoney").add_cheese().add_sauce()
    print(pizza)

```

```text
output:
Peperoney
Has Sauce
Has Cheese
```

<div dir="rtl" style="font-size:18px">
حالا اگر این روش استفاده نمیکردم باید یک تابع موجود بود و در اون تابع کلی پارامتر داشت و برای ایجاد هر شی باید اون تابع با پارامتر های زیاد رو صدا میزدم
</div>

```python
make_pizza(name="Peperoney", cheese=True, sauce=True, spicy=False)
```
<div dir="rtl" style="font-size:18px">

چه زمانی از الگوی Builder استفاده کنیم؟

استفاده از این الگو، بهترین راه برای ساختن آبجکت‌هایی هست که برای ساخته شدن نیاز به کانفیگ و ورودی‌های متعدد دارن. بدون استفاده از این الگو باید دست به دامن توابعی با تعداد پارامترهای زیاد بشیم:
</div>