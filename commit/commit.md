<div dir="rtl" style="font-size:60px; color:yellow">
نحوه‌ی commit زدن
</div>

<br/>
<div dir="rtl" style="font-size:28px">
موقع کامیت زدن اگه از pycharm استفاده میکنم این اکستنشن رو نصب کنم:
</div>

```
 conventional commits 
```

<div dir="rtl" style="font-size:28px">
این کار باعث میشه که تو قسمت commit در پایچارم برامون ابزارهای بهتری بیاد برای مدیریت commit هامون
</div>

<br/>
<br/>

<div dir="rtl" style="font-size:28px">
 قراردادی برای بهتر نوشتن  پیام کامیت ها
</div>

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

<br/>
<br/>


<div dir="rtl" style="font-size:28px">
به عنوان مثال:
</div>

<br/>
<br/>

```conventionalcommit
fix(middleware): ensure Range headers adhere more closely to RFC 2616

Add one new dependency, use `range-parser` (Express dependency) to compute
range. It is more well-tested in the wild.

Fixes #2310
```

<br/>
<br/>

<div dir="rtl" style="font-size:48px; color:yellow">
مقادیر مجاز  type
</div>

<br/>
<br/>


<div dir="rtl" style="font-size:28px">
feat: افزودن یک ویژگی جدید به پروژه 
</div>

<div dir="rtl" style="font-size:28px">
fix: حل یک مشکل 
</div>


<div dir="rtl" style="font-size:28px">
docs: مستندات پروژه 
</div>

<div dir="rtl" style="font-size:28px">
test: آزمون واحد و یکپارچه سازی
</div>


<div dir="rtl" style="font-size:28px">
chore: کارهایی از قبیل اضافه کردن تسک های gulp و npm و... که تغییری در فایل های آزمون و src ایجاد نمی کنیم
</div>

<div dir="rtl" style="font-size:28px">
refactor: برای تغییر و بهتر کردن کد
</div>


<br/>
<br/>

<div dir="rtl" style="font-size:48px; color:yellow">
متن subject باید چگونه باشه:
</div>

<br/>
<div dir="rtl" style="font-size:28px">
یک توضیح بسیار کوتاه در مورد تغییر انجام شده.
از یک فعل امری و زمان حال استفاده کنید: برای مثال "change" و نه "changed" یا "changes"
اولین حرف را بزرگ نمی نویسیم.    
اخر جمله . نمی گذاریم.

</div>









