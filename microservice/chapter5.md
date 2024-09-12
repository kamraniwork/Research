<div dir="rtl" style="font-size:60px; color:yellow">
فصل پنجم
</div>

<br/>
<div dir="rtl" style="font-size:48px;  color:yellow">
⚫ Data Management
</div>

<br/>

<div dir="rtl" style="font-size:28px; text-align: justify">
در پایگاه داده مونولیتیک، به راحتی می‌توان به هر ترکیب دلخواه داده پرداخت چرا که یک پایگاه داده مونولیتیک واحد را به اشتراک می‌گذاریم. اما در محیط میکروسرویسی، هر قطعه داده توسط یک سرویس تکمیل شده و از یک سیستم ثبت شده استفاده می‌کند. برای دسترسی به داده متعلق به یک میکروسرویس دیگر، تنها راه از طریق رابط سرویس یا API است.
</div>

<br/>
<div dir="rtl" style="font-size:48px;  color:yellow">
⚫ ⚫ Eliminating Shared Tables
</div>

<br/>

<div dir="rtl" style="font-size:28px; text-align: justify">
وقتی یک جدول بین دو یا چند میکروسرویس به اشتراک گذاشته می‌شود، هر تغییر در طرح این جدول ممکن است تأثیرگذار باشد. راه‌حل برای این مشکل این است که داده مربوط به هر میکروسرویس در جداول جداگانه قرار گیرد و خدمات مسئولیت نگهداری هماهنگی داده‌ها را از طریق API منتشر شده دارند.
</div>

<br/>
<div dir="rtl" style="font-size:48px;  color:yellow">
⚫ ⚫ Shared Data
</div>

<br/>

<div dir="rtl" style="font-size:28px; text-align: justify">
در حالت مونولوتیک اینطوریه:
</div>

![img_13.png](img_13.png)

<br/>

<div dir="rtl" style="font-size:48px;  color:yellow">
⚫ ⚫ ⚫ Synchronous Lookups
</div>

<br/>

<div dir="rtl" style="font-size:28px; text-align: justify">
هر میکروسرویس برای دسترسی به داده دیگر، می‌تواند API منتشر شده آن میکروسرویس را استفاده کند. این رویکرد در دسترسی همگام به داده ساده است ولی از کنسیستانسی معمولی ناهمگام فاقد است.
</div>

![img_14.png](img_14.png)


<div dir="rtl" style="font-size:48px;  color:yellow">
⚫ ⚫ ⚫ Using Asynchronous Events
</div>

<br/>

<div dir="rtl" style="font-size:28px; text-align: justify">
از الگوی ارتباط با رویدادها (الگوی منتشرکننده-گوش‌دهنده) می‌توان برای به اشتراک گذاری داده بین سرویس‌ها استفاده کرد. این رویکرد، با توجه به مزایا و چالش‌ها، به دسترسی به داده‌های ناهمگام کمک می‌کند.
</div>

![img_15.png](img_15.png)

<br/>
<div dir="rtl" style="font-size:48px;  color:yellow">
⚫ ⚫ Data Composition
</div>

<br/>

<div dir="rtl" style="font-size:28px; text-align: justify">
اگر جداولمون یکپارچه بود در اون صورت میتونیستیم داده هامون رو باهم ترکیب کنیم ولی چون هر میکروسرویس دیتابیس خودش رو ترکیب داده سخته. 

روش های مختلفی وجود داره برای ترکیب داده:
</div>

<br/>
<div dir="rtl" style="font-size:48px;  color:yellow">
Zuul
</div>

<br/>

<div dir="rtl" style="font-size:28px; text-align: justify">
 ترافیک HTTP را به سرویس های زیرین توزیع می کند.
 دسترسی به سرویس های زیرین را کنترل می کند.
 آمار و گزارش های مربوط به ترافیک را جمع آوری می کند.
</div>

![img_12.png](img_12.png)