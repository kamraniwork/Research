<div dir="rtl" style="font-size:18px">
یکی از زیرشاخه های الگوهای طراحی، Creational Design Patterns است.
این الگو راهی جهت ساخت و ایجاد اشیاء (object) از کلاس ها را ارائه میدهد.
ساخت یک شیء با استفاده از new کردن آن کلاس در اصطلاح hard code کردن راه حل خوبی نیست و بهتر است از الگوهای طراحی Creational استفاده کرد.


این شکل از الگوی factor اینطور هست که هر تابع کار مخصوص به خودش را انجام میدهد مثلا یک تابع مسول ساختن شی و تابع دیگر
مسیول اضافه کردن ویژگی در شی اضافه شده هست

به عنوان یک مثال:
فرض کنید افرادی هستند که این افراد یا Manager هستند یا Engineer. پس مدارکی که این افراد در اختیار دارند با هم متفاوت
هستند
ما سه نوع مدرک داریم (Be,MBA,Me).

وقتی شی از کلاس ManagerFactory یا EngineerFactory ساخته میشود باید در قسمت profile آن ها مدارک آن ها به صورت خودکار
ساخته شود. این کار با کمک تابعی که فقط مخصوص این کار است انجام میشود
</div>

```python
from abc import ABCMeta, abstractmethod


class AbstractDegree(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        pass


class Be(AbstractDegree):
    def info(self):
        print("Bachelor of engineering")

    def __str__(self):
        return "Bachelor of engineering"


class Me(AbstractDegree):
    def info(self):
        print("Master of engineering")

    def __str__(self):
        return "Master of engineering"


class Mba(AbstractDegree):
    def info(self):
        print("Master of business administration")

    def __str__(self):
        return "Master of business engineering"


```

<div dir="rtl" style="font-size:18px">
در کد بالا سه نوع مدرک ساخته شده که هرکدام از این مدارک باید وقتی کلاسی از Profile ساخته شود به شی مورد نظر اضافه شوند.
</div>

```python
from abc import ABCMeta, abstractmethod


class AbstractPersonFactory(object):
    def __init__(self):
        self._degrees = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def add_degree(self, degree):
        self._degrees.append(degree)

    def get_degree(self):
        return self._degrees


class ManagerFactory(AbstractPersonFactory):
    def create_profile(self):
        self.add_degree(Be())
        self.add_degree(Mba())


class EngineerFactory(AbstractPersonFactory):
    def create_profile(self):
        self.add_degree(Be())
        self.add_degree(Me())

```

<div dir="rtl" style="font-size:18px">
در این مثال همان طور که گفتم دو نوع تخصص داریم(Manager,Engineer) که هرکدام از آن ها باید یک تابعی مخصوص به خود برای اضافه کردن مدرک به پروفایل شی ساخته شده باشند
</div>

<div dir="rtl" style="font-size:18px">

چه زمانی از الگوی Factory Method استفاده کنیم؟

از این الگو زمانی استفاده می‌کنیم که آبجکت‌های متنوعی وجود داره و تا قبل از اجرای برنامه نمی‌دونیم چه نوع آبجکتی و به چه
صورتی قراره استفاده بشه. (Manager,Engineer ؟) همچنین می‌خوایم راهی وجود داشته باشه که بتونیم بی‌نهایت نوع آبجکت داشته
باشیم که هر کدوم نحوه ساخت متفاوتی دارن.

مثال دیگر:
</div>

```python
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create?[LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
```