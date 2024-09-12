<div dir="rtl" style="font-size:60px; color:yellow">
استراتژی‌های استفاده از cache
</div>


<br/>

<div dir="rtl" style="font-size:30px; color:orangered">
1- کش خودکار(Automatic Caching)
</div>

<br/>
<br/>
<div dir="rtl" style="font-size:18px">
در این روش، سیستم به صورت خودکار داده‌ها را در کش ذخیره می‌کند و همچنین به صورت خودکار آن‌ها را به‌روز می‌کند.

</div>

<br/>

<div dir="rtl" style="font-size:18px">
در استفاده از کش خودکار باید حواسمان به به‌روزرسانی داده ها در کش باشه وگرنه ممکنه ناسازگاری داده به وجود بیاد

</div>

<br/>

<div dir="rtl" style="font-size:18px">
پیاده سازی این نوع کش میتواند پیچیده باشد از این نظر که باید حواسمان باشه که داده ها وقتی به روزرسانی شدند در کش هم به‌روزرسانی شوند 
</div>

<br/>

<div dir="rtl" style="font-size:18px">
ابتدا برنامه به حافظه پنهان (Cache) درخواست داده رو ارسال میکنه. اگر داده مورد نظر در حافظه پنهان پیدا بشه، از اونجا بازیابی و به برنامه برگردونده میشه.
اگر داده در حافظه پنهان پیدا نشه، برنامه به منبع اصلی (مثلا پایگاه داده) مراجعه میکنه و داده رو از اونجا دریافت میکنه.
بعد از دریافت داده از منبع اصلی، برنامه اون رو در حافظه پنهان ذخیره میکنه تا دفعه بعد که بهش نیاز داشت، دیگه به منبع اصلی مراجعه نکنه و از حافظه پنهان استفاده کنه.
</div>

<br/>

```python

import time
import redis

r = redis.Redis()

def get_product_details(product_id):
    product_details: str = r.get(f"product:{product_id}")

    if product_details is not None:
        return product_details.decode('utf-8')

    print("بارگیری جزئیات محصول از پایگاه داده...")
    product_details = fetch_product_details_from_database(product_id)
    r.set(f"product:{product_id}", product_details, ex=60) 
    return product_details

def fetch_product_details_from_database(product_id):
    time.sleep(2)
    return f"Product details for {product_id}"

product_id = 123
product_details = get_product_details(product_id)
print(product_details)

```

<div dir="rtl" style="font-size:18px">
تو کد بالا اول از کش میخونه اگه داده تو کش بود همونو برمیگردونه اگر نبود از دیتابیس میخونه و دوباره داخل کش ذخیره میکنه تا رکوئست بعدی از کش بخونه.
</div>

<br/>
<br/>

<div dir="rtl" style="font-size:30px; color:orangered">
2- کش دستی (Manual Caching)
</div>

<br/>
<br/>

<div dir="rtl" style="font-size:18px">
در این روش، برخی اطلاعات به دستی در کش ذخیره می‌شود و به‌روزرسانی و حذف این اطلاعات نیز به صورت دستی انجام می‌شود.
</div>

<br/>


<div dir="rtl" style="font-size:30px; color:orangered">
3- همگام‌سازی دوره‌ای (Periodic Synchronization)
</div>

<br/>
<br/>

<div dir="rtl" style="font-size:18px">
در این روش، برخی اطلاعات به دستی در کش ذخیره می‌شود و به‌روزرسانی و حذف این اطلاعات نیز به صورت دستی انجام می‌شود.
</div>
