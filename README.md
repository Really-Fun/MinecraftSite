<h1 align="center">Прототип сайта по майнкрафту ⛏🧱</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11.8-blue" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Django-5.0.6-orange" alt="Django"/>
  <img src="https://img.shields.io/badge/NoSQL-Redis-red" alt="Redis"/>
  <img src="https://img.shields.io/badge/SQL-Postgres-yellow" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/mctools-1.3.0-green" alt="mctools"/>
</p>

<p align="center">
  <a href="https://github.com/Really-Fun/MinecraftSite" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/GitHub-Repo-black" alt="GitHub Repo"/>
  </a>
  <img src="https://img.shields.io/badge/license-Apache-green" alt="License"/>
</p>

## 🛠 Используемые технологии

- **Python 3.11.8**: Основной язык программирования.
- **Django 5.0.6**: Веб-фреймворк для создания сайта.
- **PostgreSQL**: Реляционная база данных для хранения информации о пользователях и других данных.
- **Redis**: NoSQL база данных, использующаяся для кэширования и управления сессиями.
- **mctools 1.3.0**: Библиотека для взаимодействия с Minecraft сервером.

## 📖 Описание

**Minecraft Server Portal** — это веб-приложение, созданное с использованием Django, которое служит порталом для управления и мониторинга Minecraft сервера. Проект позволяет пользователям регистрироваться, просматривать статистику сервера, оставлять заявки на участие в серверных событиях, а также выполнять другие действия, связанные с сервером, например, покупка доната.

## 🚀 Функционал

- **Регистрация и вход**: Пользователи могут создавать аккаунты, входить в систему и управлять своими профилями.
- **Мониторинг сервера**: Отображение текущего статуса сервера, количества активных игроков и другой важной информации.
- **Новости и события**: Администраторы могут публиковать новости и анонсировать события, связанные с сервером.
- **Донаты**: Поддержка системы донатов для получения дополнительных привилегий на сервере.

## 📂 Установка

Следуйте этим шагам, чтобы развернуть проект локально:

### 1. Клонирование репозитория

```bash
git clone https://github.com/Really-Fun/MinecraftSite.git
cd MinecraftSite
python -m venv .venv
source .venv/Scripts/activate  # Для Windows
# source .venv/bin/activate     # Для Linux/MacOS
pip install -r requirements.txt
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
```

## 🌟 Дополнительные возможности
1. Карта мира
В будущем можно добавить интеграцию с динамической картой мира, чтобы пользователи могли в реальном времени наблюдать за активностью на сервере.

2. Система достижений
Разработать систему достижений, которая будет поощрять активных игроков и давать им бонусы.

3. Чат в реальном времени
Реализовать чат в реальном времени для общения между пользователями сайта и игроками на сервере.

Если у вас есть вопросы или предложения по улучшению проекта, вы можете создать issue или pull request в репозитории.

## 📄 Лицензия
Этот проект лицензируется под лицензией Apache2.0. Более подробную информацию см. в файле LICENSE.
