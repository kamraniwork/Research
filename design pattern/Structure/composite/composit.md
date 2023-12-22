<div dir="rtl" style="font-size:40px; color:yellow">
الگوی طراحی Decorator
</div>


<div dir="rtl" style="font-size:18px">
برای ایجاد ساختارهای درختی از اشیا یا کلاس ها به کار میرود که این الگو امکان میدهد تا اشیا به صورت سلسله مراتبی ترکیب کنیم.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
یک مثال از دنیای واقعی:
</div>

<div dir="rtl" style="font-size:18px">
    فرض کنید شما یک کلاس ارسال مرسوله طراحی میکنید. هر کلاس یک جعبه هست که میتونه شامل چند جعبه دیگه یا شامل چند شیء باشه. > > برای ثبت یا محاسبه قیمت چطور عمل میکنید؟ > > در هر جعبه رو باز میکنید و اشیای توش رو بررسی میکنید؟ > > این قضیه توی دنیای واقعی شاید قابل انجام باشه ولی توی دنیای برنامه نویسی یا نشدنیه یا خیلی طاقت‌فرسا
</div>


<div dir="rtl" style="font-size:30px; color:yellow">
به زبون ساده:
</div>

<div dir="rtl" style="font-size:18px">
    در واقع این دیزاین پترن این امکان رو بهتون میده که ساختار‌های درختی بسازید و سپس با این ساختار‌ها طوری کار کنید که انگار با یک ابجکت منفرد کار کردید.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
پیاده سازی: 
</div>

<div dir="rtl" style="font-size:18px">
بطور کلی توی دیزاین پترن composite ما دو مدل دیتا داریم:

یک: اینکه Composite که میتونه برای خودش زیرمجموعه داشته باشه. (هرچند خودش هم وظایفی داشته باشه)

دو: Leaf که در واقع زیر مجموعه نداره و فقط یک سری وظیفه داره.

خب اول بیایم یک اینترفیس پایه برای کامپوننت‌هامون بسازیم و در ادامه هم اینترفیس‌های Composite و Leaf رو بسازیم:
</div>

```python
class Component():
    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def operation(self) -> str:
        pass


class Leaf(Component):
    def operation(self) -> str:
        return &quotLeaf&quot


class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f&quotBranch({'+'.join(results)})&quot
```

<div dir="rtl" style="font-size:18px">
استفاده ازش هم خیلی راحته:
</div>

```python
tree = Composite()

branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())

branch2 = Composite()
branch2.add(Leaf())

tree.add(branch1)
tree.add(branch2)

print(f&quotRESULT: {tree.operation()}&quot, end=&quot&quot)
# RESULT: Branch(Branch(Leaf+Leaf)+Branch(Leaf))
```

<div dir="rtl" style="font-size:30px; color:yellow">
دلیل استفاده از این الگو:
</div>

<div dir="rtl" style="font-size:18px">
وقتی که شما با سلسله مراتب از اشیا کار دارید و میخواهید اشیا را به صورت سلسله مراتب ترکیب کنید.
</div>

<div dir="rtl" style="font-size:18px">
وقتی که با ساختارهای درختی متشکل از عناصری که میتوانند زیر مجموعه دیگری داشته باشند، سروکار داریم
</div>