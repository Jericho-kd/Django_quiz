# Инструкции

## 1.Установка

  Клонирование репозитория:

    git clone https://github.com/Jericho-kd/Django_quiz.git
    
## 2.Установка зависимостей:

    pip install -r requirements.txt

## 3.Миграции
Запуск миграций:

    python manage.py makemigrations
    python manage.py migrate

## 4.Создание суперпользователя

Для создания суперпользователя запустите:

    python manage.py createsuperuser

После запуска этой команды Вы должны ввести имя пользователя и пароль. После этого Вы можете получить доступ к
панели администратора по адресу localhost:8000/admin/

## 5.Локальный запуск

Приложение запускается на localhost, порт 8000 установлен по-умолчанию.

    python manage.py runserver


