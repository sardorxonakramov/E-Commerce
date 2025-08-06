
# 📦 E-Commerce Django Loyihasi


---

## 📁 Loyihani yuklab olish va ishga tushirish

### 1. Klonlash

```bash
git clone https://github.com/sardorxonakramov/E-Commerce.git
cd E-Commerce
```

### 2. Virtual muhit yaratish

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows uchun: .venv\Scripts\activate
```

### 3. Kerakli kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

### 4. Bazani sozlash

#### `.env` fayl yarating:

```env
DJANGO_SECRET_KEY = "django-insecure-rvz-v2f4evqrwg=lv+do8aay@-7++nm7t2)h3+z9+^ieg=*f@m"


DB_NAME = "ECommerce"
DB_USER = 'postgres'
DB_PASSWORD='your_password'
DB_PORT=5432
DB_HOST ='localhost'
```

Yoki `settings.py` orqali to‘g‘ridan-to‘g‘ri `DATABASES` ni sozlang.

### 5. Migratsiyalarni bajarish

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Superuser yaratish

```bash
python manage.py createsuperuser
```

### 7. Serverni ishga tushurish

```bash
python manage.py runserver
```

---

## 📑 API Hujjatlari

### Swagger orqali avtomatik API hujjat:
`drf-spectacular` yordamida yaratilgan:

- Swagger: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- Redoc: [http://localhost:8000/api/redoc/](http://localhost:8000/api/schema/redoc/)
- Schema: [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

---


## ⚙️ Admin Panel

Admin panelga kirish:  
[http://localhost:8000/admin](http://localhost:8000/admin)

Superuser orqali tizimga kiring va mahsulotlar, foydalanuvchilar, buyurtmalarni boshqaring.
## 👀
- Admin paneli siz ham barcha ishalrni rollar ga bo'lingan holda ham bajarsa bo'ladi va bu ancha ossonroq bo'ladi chunki asosiy etiborni men admin panelga emsa loyihani o'ziga qaratdim


---



## 📌 Muallif

**Sardorxon Akramov**  
Django Backend Developer
