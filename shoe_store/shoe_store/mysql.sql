-- Active: 1727627173131@@127.0.0.1@3306@ecommerce
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shoestore_db',  # ตัวอย่างชื่อฐานข้อมูล
        'USER': 'root',  # ผู้ใช้ MySQL (ตัวอย่างเป็น root)
        'PASSWORD': 'your_password',  # รหัสผ่านสำหรับผู้ใช้ root
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
