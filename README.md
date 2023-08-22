#  Telegram Contacts Export
Export Telegram Contacts to CSV and JSON formats

---
## Farsi
برای گرفتن خروجی از **لیست کانتکت های تلگرام** باید api id و api hash از [اینجا](https://my.telegram.org/apps) 
در سایت تلگرام بگیرید. بعد از کلون کردن این مخزن، فایل `example.env` در یک ادیتور مناسب باز کنید و مقادیری که از سایت تلگرام برداشتین در جای مناسب کانفیگ کنید و در نهایت این فایل تغییر نام بدین به `.env` یعنی فقط پسوند فایل نگهدارید و اسم رو پاک کنید.
حواس تون باشه که برای ران کردن این برنامه به `python` نیاز دارید. اگر پایتون نصب ندارید از سایت رسمی ش برای سیستم عامل خودتون دانلود و نصب کنید.

## راهنمای استفاده
پس از اطمینان از نصب بودن پایتون، ترمینال را باز کنید و پیش نیازهای برنامه را نصب کنید :
```commandline
pip install requirements.txt
```
این برنامه برای برقراری امن با تلگرام از کتابخانه **telethon** استفاده می کند. سپس :
```commandline
python app.py
```
اجرا کنید. پس از اجرای برنامه **telethon** سعی در ایجاد یک ارتباط امن با تلگرام می کند. 
ابتدا از شما می خواهد شماره موبایل خود را وارد کنید. در مرحله بعد تلگرام یک کد برای شما ارسال می کند (شبیه به زمانی که می خواهید از یک دستگاه جدید به تلگرام وارد شوید)
که بعد از وارد کردن این کد، در صورت فعال بودن احراز هویت دو مرحله ای تلگرام، از شما کلمه عبورتان را می خواهد. 
پس از وارد کردن موارد گفته شده، لیستی از کانتکت های شما در خروجی ترمینال چاپ می شود و بعد از آن شما یک فایل به نام 
`contacts.csv` در مسیر جاری برنامه خواهید یافت که شامل تمام موارد چاپ شده روی ترمینال خواهد بود.

## خطای TakeoutInitDelayError
در صورت مشاهده این خطا بعد از اجرای برنامه، سعی کنید یک بار دیگر برنامه را اجرا کنید. اگر باز هم این خطا را 
ردیافت کردید، بهتر است بعد از چند دقیقه دوباره سعی کنید.


## English
First clone this repo. Make sure you have `python` installed on your system. 
Navigate to the repository directory and run :
```commandline
pip install requirements.txt
```
This application uses `telethon` to securely connect to Telegram via OAuth2. 
Tne run :
```commandline
python app.py
```
After that, you must see all your Telegram's contacts on your terminal. 
Also, all of your contacts will be saved on a csv file in the current directory named :
 `contacts.csv`.
If you get error message `TakeoutInitDelayError` please re run the app or wait 
a few minutes then retry.

### Contact
Email : **imun22** on gmail.com
