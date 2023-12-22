<div dir="rtl" style="font-size:40px; color:yellow">
الگوی طراحی Fecade
</div>


<div dir="rtl" style="font-size:18px">
رابط ساده و یک پارچه را برای دسترسی به یک سیستم یا گروه از کلاس ارایه میدهد و پیچیدگی داخلی سیستم را مخفی میکند
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
یک مثال از دنیای واقعی:
</div>

<div dir="rtl" style="font-size:18px">
    اگه ازتون بپرسم چطور یک لپ تاپ رو روشن میکنید؟ جواب شما این هست که "دکمه پاور رو میزنم"خب این چیزیه که شما بهش باور دارین، ولی در واقع دارین از یک رابط کاربری ساده میخواید تا یک عمل پیچیده با مراحل زیاد رو انجام بده.
</div>


<div dir="rtl" style="font-size:30px; color:yellow">
به زبون ساده:
</div>

<div dir="rtl" style="font-size:18px">
    این دیزاین پترن یک رابط ساده برای یک سیستم پیچیده دراختیار ما میزاره.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
پیاده سازی: 
</div>

<div dir="rtl" style="font-size:18px">
بیاین همون مثال مربوط به کامپیوتر رو پیاده‌سازی کنیم!

اول باید کلاس کامپیوتر رو بسازیم:
</div>

```python
class Computer:
    def getElectricShock(self):
        print(&quotOuch!&quot)

    def makeSound(self):
        print(&quotBeep Beep!&quot)

    def showLoadingScreen(self):
        print(&quotLoading...&quot)

    def bam(self):
        print(&quotReady to be used...&quot)

    def closeEverything(self):
        print(&quotBup bup bup buzzz!&quot)

    def sooth(self):
        print(&quotZzzzz&quot)

    def pullCurrent(self):
        print(&quotHaaah!&quot)
```

<div dir="rtl" style="font-size:18px">
کلاس Facade به این صورت پیاده‌سازی میشه که یک ابجکت رو به عنوان ورودی دریافت میکنه و با هر تابع خودش یک سری عملیات رو روی اون ابجکت اعمال میکنه.

به نحوه پیاده‌سازی Facade برای کلاس کامپیوتر دقت کنین:
</div>

```python
class ComputerFacade:
    _computer = None

    def __init__(self, computer):
        self.computer = computer

    def turnOn(self):
        self.computer.getElectricShock()
        self.computer.makeSound()
        self.computer.showLoadingScreen()
        self.computer.bam()

    def turnOff(self):
        self.computer.closeEverything()
        self.computer.pullCurrent()
        self.computer.sooth()
```

<div dir="rtl" style="font-size:18px">
نحوه استفاده از یک کلاس فساد هم به این صورته:
</div>

```python
computer = ComputerFacade(Computer())
computer.turnOn()
computer.turnOff()
```

<div dir="rtl" style="font-size:30px; color:yellow">
دلیل استفاده از این الگو:
</div>

<div dir="rtl" style="font-size:18px">
ساده سازی دسترسی به یک سیستم پیچیده
</div>

