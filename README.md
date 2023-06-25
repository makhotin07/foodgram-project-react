# 🥗 Foodgram: «Продуктовый помощник» 🥗

<div align="center">
    <img src="https://image.flaticon.com/icons/png/512/2921/2921822.png" width="150" height="150"/>
</div>

<p align="center"><i>Ваш личный кулинарный ассистент в мире рецептов!</i></p>

---

🍳 **Foodgram** - это волшебное место, где вы можете **публиковать свои рецепты**, **подписываться на публикации** других пользователей, **добавлять понравившиеся рецепты в список «Избранное»**, а перед походом в магазин **скачивать сводный список продуктов**, необходимых для приготовления одного или нескольких выбранных блюд.

<div align="center">
    <img src="https://media3.giphy.com/media/l3vRlInF7QViJNOow/giphy.gif" width="250"/>
</div>

---

## 🛠 Технологии:
- **Python 3.8.9**
- **Django 4.0.3**
- **Gunicorn**
- **PostgreSQL**

![workflow badge](https://github.com/makhotin07/foodgram-project-react/actions/workflows/main.yml/badge.svg)

🌍 **Попробуйте наш сайт**: [Foodgram](http://158.160.100.123/)

👑 **Вход для администратора**:
```
Почта: a@adm.ru
Пароль: admin5
```

---

## 🚀 Запуск на localhost:

#### 1. Клонируйте репозиторий и перейдите в его директорию:
```sh
git clone https://github.com/makhotin07/foodgram-project-react.git
cd foodgram-project-react
```

#### 2. Создайте и активируйте виртуальное окружение:
```sh
python3 -m venv venv
source venv/bin/activate
```

#### 3. Создайте файл `.env` с настройками (или используйте значения по умолчанию из файла `settings.py`):
```sh
DB_ENGINE=
DB_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=
```

#### 4. Соберите и запустите проект в контейнерах:
```sh
cd infra
docker-compose -f docker-compose.dev.yml up -d --build
```
> Команды миграции данных выполняются при сборке.

#### 5. Создайте суперпользователя:
```sh
docker-compose exec backend python manage.py createsuperuser
```

#### 6. Откройте в браузере:
- Главная страница: [http://localhost/](http://localhost/)
- Панель администратора: [http://localhost/admin](http://localhost/admin)
- Документация API: [http://localhost/api/docs/](http://localhost/api/docs/)

---



<div align="center">
    <b>🍽 Приятного аппетита с Foodgram! 🍽</b>
    <p><img src="https://media1.giphy.com/media/l49JThpgIOD24fGxi/giphy.gif" width="250"/></p>
</div>
