# Сервис управления рассылками

Этот проект — это веб-приложение для управления рассылками, созданное с использованием Django. Сервис предоставляет возможность создавать, редактировать, удалять рассылки, управлять клиентами, отслеживать статус попыток рассылки, а также автоматически или вручную запускать рассылки.

## Основные возможности:

- **CRUD для рассылок**: Просмотр, создание, редактирование и удаление рассылок с параметрами, такими как дата и время первой отправки, периодичность и статус.
- **Система управления пользователями**: Регистрация пользователей, верификация почты, разделение прав доступа для разных типов пользователей (например, администраторы и менеджеры).
- **Менеджер рассылок**: Возможность блокировать пользователей, отключать рассылки и просматривать любые рассылки, но без редактирования их содержимого.
- **Клиенты и сообщения**: Управление клиентами (контактный email, Ф. И. О., комментарии) и настройка сообщений для рассылок.
- **Попытки рассылки**: Отслеживание попыток отправки рассылки, статус каждой попытки (успешно/не успешно) и ошибки почтового сервера.

# Сущности системы:

- **Клиенты**: Получатели рассылок с полями для контактных данных.
- **Рассылка**: Рассылка сообщений с параметрами (дата отправки, периодичность и статус).
- **Сообщение**: Тема и тело письма для рассылки.
- **Попытка рассылки**: Запись о статусе попытки отправки сообщения (успешно/не успешно).

# Доработка сервиса:

- **Блог**: Создание блога для продвижения сервиса с функциями управления статьями (заголовок, содержимое, изображение, количество просмотров).
- **Кеширование**: Настройка кеширования для главной страницы и блога для улучшения производительности.
- **Контроль доступа**: Разграничение прав доступа для разных типов пользователей, ограничение редактирования рассылок и клиентов.

# Технологии:

- **Django**: Веб-фреймворк, используемый для разработки бэкенда.
- **PostgreSQL**: Система управления базами данных, используемая для хранения данных приложения.
- **UIkit Bootstrap**: Фреймворк для интерфейса.
- **Crontab**: Используется для работы с периодическими задачами.
- **Redis**: Используется для кеширования с целью повышения производительности и ускорения извлечения данных.

# Запуск:

## Установка и настройка

### 1. Клонировать репозиторий

Сначала клонируйте репозиторий с GitHub:

```bash
git clone git@github.com:kkatka1/mailing_service.git
cd mailing_service

2. Создать и активировать виртуальное окружение

Создайте виртуальное окружение с помощью `venv` и активируйте его:

Для Linux/macOS:

```bash
python3 -m venv env
source env/bin/activate

Для Windows:
python -m venv env
.\env\Scripts\activate

3. Установить зависимости

Установите зависимости из файла requirements.txt:
pip install -r requirements.txt

4. Запустить миграции

После установки зависимостей выполните миграции для базы данных:

python3 manage.py migrate

5. Создать суперпользователя

Для создания суперпользователя выполните команду:
python3 manage.py createsuperuser

6. Загрузить фикстуры

Для загрузки тестовых данных в базу данных выполните команду:
python3 manage.py loaddata data.json

7. Создать группу

Для создания группы пользователей выполните команду:
python3 manage.py create_groupe

8. Создать менеджера и контент-менеджера

Для создания менеджера и контент-менеджера выполните команду:
python3 manage.py create_staff

9. Запустить сервер

Для запуска сервера выполните команду:
python3 manage.py runserver

Сервер будет доступен по адресу: http://127.0.0.1:8000
