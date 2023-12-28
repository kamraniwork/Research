<div dir="rtl" style="font-size:40px; color:yellow">
الگوی طراحی Abstract Factory
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
یک مثال از دنیای واقعی:
</div>

<div dir="rtl" style="font-size:18px">
 فرض کنید در حال ساخت خونه هستین و نیاز به چند درب مختلف دارید ولی اینبار نیاز به درب چوبی، درب ضد سرقت، درب شیشه و ... دارین. به طبع برای خرید باید به مغازه‌های مختلفی مراجعه کنید ، از طرفی برای استفاده ازشون هم ممکنه نیاز به متخصص مربوطه داشته باشین. برای مثال ما برای درب چوبی به چوب فروشی میریم و برای نصبش هم از یک نجار کمک میگیریم یا برای درب شیشه ای به مغازه و متخصص مربوط به خودش مراجعه میکنیم.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
به زبون ساده:
</div>

<div dir="rtl" style="font-size:18px">
    این دیزاین پترن تا حد زیادی مشابه simple factory هست با این تفاوت که مجموعه ای از اشیا مرتبط بهم رو ایجاد میکنه.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
مثال برنامه نویسی
</div>

<div dir="rtl" style="font-size:18px">
اول باید اینترفیس درب رو بسازیم و چند پیاده‌سازی ازش ایجاد کنیم :
</div>

```python
class Door:
    def getDescription(self):
        pass


class WoodenDoor(Door):
    def getDescription(self):
        print('I am a wooden door')


class IronDoor(Door):
    def getDescription(self):
        print('I am an iron door')
```
<div dir="rtl" style="font-size:18px">
در مرحله بعد برای هر درب متخصص مربوطه رو ایجاد می‌کنیم:
</div>

```python
class DoorFittingExpert:
    def getDescription(self):
        pass


class Welder(DoorFittingExpert):
    def getDescription(self):
        print('I can only fit iron doors')


class Carpenter(DoorFittingExpert):
    def getDescription(self):
        print('I can only fit wooden doors')
```

<div dir="rtl" style="font-size:18px">
حالا اینجاست که ما سراغ پیاده‌سازی دیزاین پترن‌مون میریم.

برای مثال کلاس WoodenDoorFactory زمانی استفاده میشه که نیاز به درب چوبی داریم و کارش اینه که برای ایجاد ابجکت درب (که اینجا درب چوبی هست) از کلاس WoodenDoor و برای ایجاد ابجکت متخصص (که اینجا نجار هست) از Carpenter استفاده کنه.

این موضوع برای درب آهنی و ... هم بطور مشابه پیاده‌سازی میشه.
</div>

```python
class DoorFactory:
    def makeDoor(self):
        pass

    def makeFittingExpert(self):
        pass


class WoodenDoorFactory(DoorFactory):
    def makeDoor(self):
        return WoodenDoor()

    def makeFittingExpert(self):
        return Carpenter()


class IronDoorFactory(DoorFactory):
    def makeDoor(self):
        return IronDoor()

    def makeFittingExpert(self):
        return Welder()
```

<div dir="rtl" style="font-size:18px">
روش استفاده ازش هم به این صورت هست:
</div>

```python
woodenFactory = WoodenDoorFactory()

door = woodenFactory.makeDoor()
expert = woodenFactory.makeFittingExpert()

door.getDescription()
expert.getDescription()

# -----------------------------------------------

ironFactory = IronDoorFactory()

door = ironFactory.makeDoor()
expert = ironFactory.makeFittingExpert()

door.getDescription()
expert.getDescription()
```

<div dir="rtl" style="font-size:30px; color:yellow">
چه موقع باید ازش استفاده کنیم؟
</div>

<div dir="rtl" style="font-size:18px">
زمانی که وابستگی‌های منطقی نه چندان ساده برای ایجاد وجود داره، میتونیم ازین دیزاین پترن استفاده کنیم.
</div>


<div dir="rtl" style="font-size:18px">
این الگو اگر شی های متفاوتی یک کارخانه تولید کند مثلا در این مثال هم کلاس در (چوب، فلز) بود و هم متخصص طراح در ( نجار، جوشکار).
</div>

<div dir="rtl" style="font-size:18px">
پس ما علاوه بر اینکه برای هر کدوم از این انواع باید کلاس factory بسازیم باید برای خود این factory ها هم یک factory بسازیم. یعنی factory of foatories.
</div>

<div dir="rtl" style="font-size:18px">
یعنی ما یک کلاس factory برای ساخت ابجکت در داریم که میتونه از نوع چوب یا فلز باشه. و یک factory برای ساخت متخصص داریم که میتونه نجار یا جوشکار باشه. و یک کلاس factory دیگه هم داریم که مشخص میکنه کدوم نوع فکتوری باید ایجاد بشه.
</div>

<div dir="rtl" style="font-size:18px">
که این مدل آخر یعنی کدوم نوع فکتوری باید ایجاد بشه در این مثال حذف شده و بهتر آن جایگزین شده چون باید if و else مینوشتیم که اگه فلان بود این فکتوری ایجاد بشه و در غیر این صورت یک فکتوری دیگه صدا زده بشه.
</div>