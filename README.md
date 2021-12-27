# Django Framework. Инструменты оптимизации

Репозиторий для сдачи домашнего задания.

Коробанов Георгий.

##Урок 5
* 0:10 bug fixed
* `this` add to requirements.txt and fill_db
* 0:41 reg.ru login | vps | заказать | ubuntu
* 0:43 settings databases postgesql
* 0:45 lib psycopg2-binary | activate venv | pip freeze > requirements.txt | git push
* 0:47 mail ip | terminal ssh ssh root@151.248.117.226 login | without pass ssh-copy-id root@151.248.117.226
* 0:49 ssh-keygen | cat /root/.ssh/id_rsa.pub | copy
* 0:50 repository settings | deploy keys | new | paste
* 0:51 apt update | apt install nginx | apt install postgresql postgresql-contrib | apt install python3-venv | apt install git
* 0:54 nano /etc/postgresql/12/main/pg_hba.conf | peer -> trust | systemctl restart postgresql | systemctl status postgresql
* 0:56 useradd -g www-data -m django | cd /home/django/ | git clone git@github.com:georgekorob/geekshop.git
* 0:58 python3 -m venv env | source env/bin/activate | git checkout lesson_2_5 | cd geekshop/geekshop
* 0:59 pip install -r requirements.txt | pip install `wheel`
* 1:02 psql -U postgres | create database geekshop; | exit;
* 1:03 pip install `social-auth-app-django` | python3 manage.py migrate | python3 manage.py fill_db
* 1:04 python3 manage.py `createsuperuser` | python3 manage.py runserver 0.0.0.0:8000
* 1:07 sudo nano /etc/systemd/system/gunicorn.service | edit | pip install `gunicorn`
* 1:12 sudo systemctl enable gunicorn | sudo systemctl start gunicorn | sudo systemctl status gunicorn
* 1:13 chown -R django /home/django/
* 1:14 sudo nano /etc/nginx/sites-available/geekshop | edit | systemctl disable/enable/status gunicorn
* 1:20 sudo ln -s /etc/nginx/sites-available/geekshop /etc/nginx/sites-enabled
* 1:21 rm /etc/nginx/sites-enabled/default | systemctl restart nginx | sudo nginx -t
* 1:22 tail -f /var/log/nginx/error.log | cd ~ | history > /tmp/history.txt | exit
* 1:25 scp root@151.248.117.226:/tmp/history.txt ./Documents/

##Задания 5
1. Создать файл зависимостей «requirements.txt» для проекта.
2. Экспортировать данные из базы.
3. Установить и настроить сервер Ubuntu Server 17.
4. Развернуть проект на сервере.

Так как образ виртуальной машины достаточно большого размера, вместо него необходимо в архиве с ДЗ выслать скриншоты с выполненными шагами. Если на каком-то шаге начались проблемы – необходимо написать о них в файле «readme.txt». Если удастся развернуть проект на реальном хостинге – высылайте ссылку.

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