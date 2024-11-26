# bar_project
🌍 Веб-приложение для бара, написанное на Python, с использованием фраймворка Django, а так же HTML, CSS и PostgreSQL

## Содержание
- [Технологии](#технологии)
- [Зависимости](#зависимости)
- [Запуск](#запуск)
- [Автор проекта](#автор-проекта)

## Технологии
- Python3
- Django Framework
- PostgreSQL
- HTML5
- CSS 
- JavaScript

## Зависимости
Создайте виртуальное окружение.
```sh
python3 -m venv venv
```
Установите зависимости проекта, командой ниже.
```sh
$ pip3 install -r requirements.txt
```

## Запуск

Создайте базу данных и настройте суперпользователя и выполните эти команды.
```sh
cd backend
python3 manage.py makemigrations
python3 manage.py migrate
```
Затем запустите ваш сервер.
```sh
python3 manage.py runserver
```
Сервер стартует по адресу ``` http://127.0.0.1:8000/```
## Автор проекта
...