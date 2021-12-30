# Django Framework. Инструменты оптимизации

Репозиторий для сдачи домашнего задания.

Коробанов Георгий.

##Урок 6
* 0:14 pip install django-debug-toolbar | pip install django-debug-toolbar-template-profiler
* 0:17 settings 'debug_toolbar', 'template_profiler_panel' | if DEBUG: ...
* 0:19 urls
* 0:24 STATIC_ROOT | collectstatic
* 0:27 restart gunicorn
* 0:30 vk
* 0:31 debug toolbar
* 0:43 card.html
* 0:47 select_related
* 1:10 pip install django-extensions | python manage.py show_urls > geekshop_urls.txt
* 1:12 validate_templates | pip install pydotplus graph_models | pycharm visual db
* 1:17 sudo apt install siege | siege -f urls.txt -d1 -r29 -c1 | --debug
* 1:23 http://89.108.81.8/auth/login/ POST username=...&password=... | # csrf
* 1:34 login-url in siege
* 1:42 hw

##Задания 6
* ssh подключение (pycharm, cmd)
* восстановить функционал vk
1. Установить приложение «django-debug-toolbar». Оценить время загрузки страниц. Найти самые медленные контроллеры. Заполнить таблицу с количеством запросов и дубликатов на страницах проекта.
2. Визуализировать структуру моделей проекта при помощи «django_extensions», создать файл «geekshop_urls.txt» с URL-адресами проекта.
3. Установить утилиту «siege» и провести функциональное тестирование. Зафиксировать результаты в текстовом файле (какие контроллеры работали с ошибками).
4. Провести нагрузочное тестирование отдельных страниц и записать результаты в таблицу.
5. Провести тестирование в режиме интернета. Записать данные в таблицу. Определить условия, при которых начинаются отказы.
6. Провести оптимизацию работы с БД в проекте. Оценить эффект.
7. Визуализация БД

[comment]: <> (##Урок 5)
[comment]: <> (* 0:10 bug fixed)
[comment]: <> (* `this` add to requirements.txt and fill_db)
[comment]: <> (* 0:41 reg.ru login | vps | заказать | ubuntu)
[comment]: <> (* 0:43 settings databases postgesql)
[comment]: <> (* 0:45 lib psycopg2-binary | activate venv | pip freeze > requirements.txt | git push)
[comment]: <> (* 0:47 mail ip | terminal ssh root@89.108.81.8 login | without pass ssh-copy-id root@89.108.81.8)
[comment]: <> (* 0:49 ssh-keygen | cat /root/.ssh/id_rsa.pub | copy)
[comment]: <> (* 0:50 repository settings | deploy keys | new | paste)
[comment]: <> (* 0:51 apt update | apt install nginx | apt install postgresql postgresql-contrib | apt install python3-venv | apt install git)
[comment]: <> (* 0:54 nano /etc/postgresql/12/main/pg_hba.conf | peer -> trust | systemctl restart postgresql | systemctl status postgresql)
[comment]: <> (* 0:56 useradd -g www-data -m django | cd /home/django/ | git clone git@github.com:georgekorob/geekshop.git)
[comment]: <> (* 0:58 python3 -m venv env | source env/bin/activate | git checkout lesson_2_5 | cd geekshop/geekshop)
[comment]: <> (* 0:59 pip install -r requirements.txt | pip install `wheel`)
[comment]: <> (* 1:02 psql -U postgres | create database geekshop; | exit;)
[comment]: <> (* 1:03 pip install~~ `social-auth-app-django` ~~| python3 manage.py migrate | python3 manage.py fill_db)
[comment]: <> (* 1:04 python3 manage.py~~ `createsuperuser` ~~| python3 manage.py runserver 0.0.0.0:8000)
[comment]: <> (* 1:07 sudo nano /etc/systemd/system/gunicorn.service | edit | pip install `gunicorn`)
[comment]: <> (* 1:12 systemctl enable gunicorn | sudo systemctl start gunicorn | sudo systemctl status gunicorn)
[comment]: <> (* 1:13 chown -R django /home/django/)
[comment]: <> (* 1:14 sudo nano /etc/nginx/sites-available/geekshop | edit | systemctl disable/enable/status gunicorn)
[comment]: <> (* 1:20 sudo ln -s /etc/nginx/sites-available/geekshop /etc/nginx/sites-enabled)
[comment]: <> (* 1:21 rm /etc/nginx/sites-enabled/default | systemctl restart nginx | sudo nginx -t)
[comment]: <> (* 1:22 tail -f /var/log/nginx/error.log | cd ~ | history > /tmp/history.txt | exit)
[comment]: <> (* 1:25 scp root@89.108.81.8:/tmp/history.txt ./Documents/)
[comment]: <> (* scp D:\Programming\geekshop\.env root@89.108.81.8:/home/django/geekshop/.env)
[comment]: <> (* scp D:\Programming\geekshop\users.json root@89.108.81.8:/home/django/geekshop/users.json)
[comment]: <> (* scp D:\Programming\geekshop\media\product_image\ root@89.108.81.8:/home/django/geekshop/media/product_image/)
[comment]: <> (##Задания 5)
[comment]: <> (1. Создать файл зависимостей «requirements.txt» для проекта.)
[comment]: <> (2. Экспортировать данные из базы.)
[comment]: <> (3. Установить и настроить сервер Ubuntu Server 17.)
[comment]: <> (4. Развернуть проект на сервере.)
[comment]: <> (Так как образ виртуальной машины достаточно большого размера, вместо него необходимо в архиве с ДЗ выслать скриншоты с выполненными шагами. Если на каком-то шаге начались проблемы – необходимо написать о них в файле «readme.txt». Если удастся развернуть проект на реальном хостинге – высылайте ссылку.)
[comment]: <> (##Урок 4)
[comment]: <> (* 0:18 basket.delete)
[comment]: <> (* 0:21 basket methods &#40;get_item, save, delete&#41;)
[comment]: <> (* 0:39 basket query set)
[comment]: <> (* 0:58 order get_item and signals)
[comment]: <> (* 1:18 order js)
[comment]: <> (* 2:15 hw)
[comment]: <> (##Задания 4)
[comment]: <> (1. Организовать работу с остатками товара в проекте &#40;попробовать оба способа&#41;.)
[comment]: <> (2. Реализовать обновление статистики заказа через jQuery.)
[comment]: <> (3. Расширить функционал работы с формами при помощи «django-dynamic-formset».)
[comment]: <> (4. *Реализовать асинхронное обновление цены при добавлении нового продукта в заказ.)
[comment]: <> (##Урок 3)
[comment]: <> (* 0:15 photo and lang)
[comment]: <> (* 0:28 basket)
[comment]: <> (* 0:35 models)
[comment]: <> (* 0:53 views)
[comment]: <> (* 1:00 forms)
[comment]: <> (* 1:05 template user dropdown)
[comment]: <> (* 1:19 order templates)
[comment]: <> (* 1:23 views)
[comment]: <> (* 1:32 templates)
[comment]: <> (##Задания 3)
[comment]: <> (1. Создать выпадающее меню для ссылки на личный кабинет пользователя в меню.)
[comment]: <> (2. Создать приложение для работы с заказами пользователя.)
[comment]: <> (3. Создать контроллеры CRUD для заказа на базе Django CBV.)
[comment]: <> (4. Реализовать обновление статуса заказа при совершении покупки.)
[comment]: <> (5. Обновить контроллеры проекта – перевести на Django CBV.)
[comment]: <> (6. *Организовать работу со статусом заказов в админке &#40;имитация обработки заказа в магазине&#41;.)
[comment]: <> (##Урок 2)
[comment]: <> (* 0:08 приложение vk)
[comment]: <> (* 0:11 pip install social_auth_app_django)
[comment]: <> (* 0:12 settings)
[comment]: <> (* 0:16 backend hw)
[comment]: <> (* 0:18 urls)
[comment]: <> (* 0:20 template login)
[comment]: <> (* 0:30 models)
[comment]: <> (* 0:50 forms)
[comment]: <> (* 0:55 view)
[comment]: <> (* 1:01 template profile)
[comment]: <> (* 1:17 settings)
[comment]: <> (* 1:24 pipelines)
[comment]: <> (* 1:43 test)
[comment]: <> (* 1:47 homework)
[comment]: <> (##Задания 2)
[comment]: <> (1. Реализовать в проекте простой вариант аутентификации пользователя через социальную сеть VK+.)
[comment]: <> (2. Поработать со связью моделей «один-к-одному»: создать профиль пользователя и обеспечить возможность его редактирования.)
[comment]: <> (3. Реализовать автоматическое заполнение профиля пользователя при аутентификации через социальную сеть.)
[comment]: <> (4. Проверить работу исключения «AuthForbidden», например, задав при проверке минимальный возраст 100 лет.)
[comment]: <> (5. *Получить и сохранить язык из сети VK+.)
[comment]: <> (6. *Получить и сохранить foto из сети VK+.)
[comment]: <> (##Урок 1)
[comment]: <> (* 0:17 models user activation_key)
[comment]: <> (* 0:23 forms register save)
[comment]: <> (* 0:26 views register post)
[comment]: <> (* 0:31 urls verify)
[comment]: <> (* 0:39 dotenv)
[comment]: <> (* 0:44 .env requirements)
[comment]: <> (* 0:49 template verification)
[comment]: <> (* 1:00 test)
[comment]: <> (* 1:17 request self)
[comment]: <> (* 1:20 DebuggingServer)
[comment]: <> (* 1:27 mainapp.context_processors)
[comment]: <> (* 1:34 mail)
[comment]: <> (##Задания 1)
[comment]: <> (1. Организовать выдачу сообщения об успешной отправке письма с кодом подтверждения в окне регистрации пользователя.)
[comment]: <> (2. Реализовать активацию пользователя при переходе по ссылке из письма.)
[comment]: <> (3. Создать контекстный процессор для корзины и скорректировать код контроллеров основного приложения.)
[comment]: <> (<br>При отправке домашнего задания не нужно отправлять папку с виртуальным окружением &#40;если она есть в проекте – просто удалите&#41;. Можно проверить по объему: если больше 50 МБ – значит папка с виртуальным окружением есть.)