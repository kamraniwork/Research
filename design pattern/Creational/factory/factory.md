<div dir="rtl" style="font-size:40px; color:yellow">
الگوی طراحی Factory
</div>


<div dir="rtl" style="font-size:18px">
یکی از زیرشاخه های الگوهای طراحی، Creational Design Patterns است.
این الگو راهی جهت ساخت و ایجاد اشیاء (object) از کلاس ها را ارائه میدهد.
ساخت یک شیء با استفاده از new کردن آن کلاس در اصطلاح hard code کردن راه حل خوبی نیست و بهتر است از الگوهای طراحی Creational استفاده کرد.

اگر بخواهیم به تعداد بی شماری شی از یک کلاس بسازیم و نمیدانیم چه تعداد شی قرار است ساخته شود
</div>


<div dir="rtl" style="font-size:30px; color:yellow">
یک مثال از دنیای واقعی:
</div>

<div dir="rtl" style="font-size:18px">
یک مدیر رو فرض کنید که وظیفه استخدام افراد رو به عهده داره. مطمئنن براش غیر ممکنه که مصاحبه با همه افراد در پوزیشن‌های مختلف شرکت رو خودش انجام بده! پس میاد با توجه به پوزیشن تصمیم میگیره که مسئولیت مصاحبه رو به عهده یکی از کارمند‌هاش بزاره.
</div>

<div dir="rtl" style="font-size:30px; color:yellow">
پیاده سازی: 
</div>

<div dir="rtl" style="font-size:18px">
پس اول یک اینترفیس برای مصاحبه کننده‌ها میسازیم و چند پیاده‌سازی هم برای اون ایجاد می‌کنیم:
</div>

```python
class Interviewer:
    def askQuestions(self):
        pass


class Developer(Interviewer):
    def askQuestions(self):
        print
        'Asking about design patterns'


class CommunityExecutive(Interviewer):
    def askQuestions(self):
        print('Asking about community building')
```

<div dir="rtl" style="font-size:18px">
خب حالا HiringManager رو میسازیم:
</div>

```python
class HiringManager:
    def makeInterviewer(self):
        pass

    def takeInterview(self):
        interviewer = self.makeInterviewer()
        interviewer.askQuestions()
```

<div dir="rtl" style="font-size:18px">
در نهایت هر فرزند میتونه ازش ارث بری کنه و متد makeInterviewer خودش رو داشته باشه:
</div>

```python
class DevelopmentManager(HiringManager):
    def makeInterviewer(self):
        return Developer()


class MarketingManager(HiringManager):
    def makeInterviewer(self):
        return CommunityExecutive()
```

<div dir="rtl" style="font-size:18px">
و برای استفاده ازش به این صورت عمل می کنیم:
</div>

```python
devManager = DevelopmentManager()
devManager.takeInterview()

marketingManager = MarketingManager()
marketingManager.takeInterview()
```

<div dir="rtl" style="font-size:20px;">
اساساً زمانی ازین الگو استفاده میشه که چندین کلاس با ریشه مشترک داریم (یعنی چندین کلاس یک کلاس parent رو پیاده‌سازی می‌کنند) و با توجه به شرایط تصمیم میگیریم از یکی از اون‌ها استفاده کنیم.
</div>


<div dir="rtl" style="font-size:20px;">
کلاس های DevelopmentManager و MarketingManager  میتوانستند وجود نداشته باشند و به جای این ها یک کلاس داشته باشیم و با if , else آبجکت هارو بسازیم.
</div>

```python
from typing import Literal

class ManagerFactory(HiringManager):
    def makeInterviewer(self, manager_type: Literal['dev', 'martek']):
        if manager_type == 'dev':
                
            return Developer()
        return CommunityExecutive()

```

<div dir="rtl" style="font-size:20px;">
به نظرم این کار بده چون اگه کلاس جدیدی بخوایم بسازیم باید کد رو تغییر بدیم که این درست نیست و تاجای ممکن باید سعی بشه کد رو تغییر ندیم.
</div>