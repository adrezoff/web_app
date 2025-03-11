# bar_project
🌍 Веб-приложение для бара, написанное на Python, с использованием фреймворка Django, HTML, CSS, JavaScript и PostgreSQL

## Демонстрация
![preview.gif](preview.gif)

## Содержание
- [Технологии](#технологии)
- [Зависимости](#зависимости)
- [Запуск](#запуск)

## Технологии
- Python3
- Django Framework
- PostgreSQL
- HTML
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
python3 manage.py makemigrations
python3 manage.py migrate
```
Затем запустите ваш сервер (не забудьте создать файл .env и заполнить ключи для файла ```bar_project/settings.py```).
```sh
python3 manage.py runserver
```
Сервер стартует по адресу ``` http://127.0.0.1:8000/```
