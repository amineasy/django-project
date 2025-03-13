# انتخاب ایمیج پایه پایتون
FROM python:3.10

# تنظیم متغیر محیطی برای اینکه خروجی‌های پایتون به‌طور خودکار در کنسول نشان داده شود
ENV PYTHONUNBUFFERED=1

# ایجاد دایرکتوری برای پروژه در کانتینر
WORKDIR /app

# کپی کردن فایل requirements.txt به کانتینر
COPY requirements.txt /app/

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کل پروژه به داخل کانتینر
COPY . /app/

# اجرای دستور برای شروع سرور جنگو
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
