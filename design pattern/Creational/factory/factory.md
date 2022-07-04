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
پیاده سازی: 
</div>

```python
from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    @abstractmethod
    def create(self, name):
        pass


class HR(Person):
    def create(self, name):
        print(f"HR {name} is created")


class Engineer(Person):
    def create(self, name):
        print(f"Engineer {name} is created")


class PersonFactory(object):
    @classmethod
    def create_person(cls, designation, name):
        eval(designation)().create(name)


if __name__ == "__main__":
    designation = input("Please enter the designation - ")
    name = input("Please enter the person name - ")
    PersonFactory.create_person(designation, name)


```

<div dir="rtl" style="font-size:20px;">
در کد بالا دو کلاس مختلف از Person را داریم که میخواهیم از هرکدام از آن ها در حین اجرای برنامه هر موقع که خواستیم یک شی بسازیم. و نمیخواهیم از if-else استفاده کنیم که باعث پیچیدگی بیشتر برنامه میشود و وظیفه ایجاد شی به عهده کلاس PersonFactoryاست
</div>