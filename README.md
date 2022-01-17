# Django Framework. Инструменты оптимизации

Репозиторий для сдачи домашнего задания.

Коробанов Георгий.

##Урок 8
[comment]: <> (* 0:13 F&Q objects)
[comment]: <> (* 0:19 update is_active)
[comment]: <> (* 0:21 baskets quantity)
[comment]: <> (* 0:28 category discount)
[comment]: <> (* 0:36 Q)
[comment]: <> (* 0:47 action table discount sort)
[comment]: <> (* 1:17 relax 1:27)
[comment]: <> (* 1:28 smoke tests)
[comment]: <> (* 1:43 disable debug panel)
[comment]: <> (* 1:46 test_login)
[comment]: <> (* 1:54 test_register)
##Задания 8
[comment]: <> (1. Исправить баг при управлении активностью категории. Активность товаров тоже должна обновляться.)
[comment]: <> (2. Реализовать возможность сделать скидку на товары категории в админке при помощи метода «.upadate&#40;&#41;».)
[comment]: <> (3. Поработать с F-объектом, убедиться, что обновление значений выполняется на уровне БД, а не в python-коде.)
[comment]: <> (4. Написать несколько запросов с логическим «ИЛИ|. Написать сложный запрос в базу с использованием «conditional-expressions».)
[comment]: <> (5. Провести тестирование работоспособности одного из приложений.)
[comment]: <> (6. Протестировать процесс логина пользователя и переадресацию при доступе корзине.)
[comment]: <> (7. Исправить ошибку в функции «get_hot_product&#40;&#41;».)
8. Написать тесты для методов моделей проекта.
9. В качестве защиты курсового проекта необходимо записать в любой удобной для вас программе видеоролик (скринкаст) продолжительностью 1-5 минут. Представьте, что вам необходимо презентовать вашу работу заказчику или аудитории. В скринкасте расскажите о вашем проекте, продемонстрируйте его возможности и функционал. Ссылку на видео приложите к практическому заданию, например, в комментарии к уроку. И не забудьте открыть доступ на просмотр! :) Видеопрезентация продукта развивает у вас дополнительные мягкие навыки и является обязательной для засчитывания курсового проекта.


[comment]: <> (##Урок 7)
[comment]: <> (* 0:20 get_item_cached related_name)
[comment]: <> (* 0:23 **@cached_property [1]**)
[comment]: <> (* 0:39 get_summary)
[comment]: <> (* 0:43 **with [2]** templates | 1:46 correct =)
[comment]: <> (* 0:47 apt install memcached | apt install libmemcached-dev | pip3 install python-memcached)
[comment]: <> (* 0:49 nano /etc/memcached.conf | -m 256 | systemctl restart memcached | systemctl status memcached)
[comment]: <> (* 0:51 **LOW_CACHE memcached [3]** | settings.py | CACHE... | 1:13 django.core.cache...)
[comment]: <> (* 0:59 pip install django-extensions)
[comment]: <> (* 1:01 from django.conf import settings | from django.core.cache import cache | models add db_index)
[comment]: <> (* 1:06 views | get_link_category)
[comment]: <> (* 1:18 get_link_product | get_product)
[comment]: <> (* 1:38 ~~after relax~~ | **fragment templetes cache**)
[comment]: <> (* 1:49 order_from.html | field.name == 'product' {% cache 3600 orderitemform_product field.value %})
[comment]: <> (* 2:00 views **@cache_page&#40;3600&#41; [4]**)
[comment]: <> (* 2:01 urls **cache_page&#40;3600&#41;&#40;products&#41;**)
[comment]: <> (* 2:03 **all_site** | settings middleware)
[comment]: <> (* 2:13 @never_cache)
[comment]: <> (* 2:17 hw)
[comment]: <> (* нужно убрать в модели Product, в методе str self.category)
[comment]: <> (##Задания 7)
[comment]: <> (1. Найти в проекте повторяющиеся вызовы методов для одного экземпляра модели и применить к ним декоратор **@cached_property**. Оценить, насколько уменьшилось число дублей при выполнении SQL-запросов и каков прирост производительности.)
[comment]: <> (2. Применить тег **with** в одном из шаблонов. Оценить, насколько уменьшилось число дублей при выполнении SQL-запросов и каков прирост производительности.)
[comment]: <> (3. Установить и настроить приложение **Memcached**. Реализовать кеширование на низком уровне для функций, возвращающих редко изменяющиеся данные &#40;продукты каталога, список категорий и т.д.&#41;. Оценить прирост производительности.)
[comment]: <> (4. Реализовать кеширование в шаблоне для набора форм. Оценить эффект.)
[comment]: <> (5. ***Реализовать работу с некоторыми пунктами меню через AJAX и кешировать соответствующие страницы. Оценить эффект от применения технологии AJAX и эффект от кеширования.)
[comment]: <> (6. *Попробовать реализовать кеширование всего сайта в проекте. Оценить прирост производительности и возникающие при этом проблемы с обновлением контента.)
[comment]: <> (##Урок 6)
[comment]: <> (* 0:14 pip install django-debug-toolbar | pip install django-debug-toolbar-template-profiler)
[comment]: <> (* 0:17 settings 'debug_toolbar', 'template_profiler_panel' | if DEBUG: ...)
[comment]: <> (* 0:19 urls)
[comment]: <> (* 0:24 STATIC_ROOT | collectstatic)
[comment]: <> (* 0:27 restart gunicorn)
[comment]: <> (* 0:30 vk)
[comment]: <> (* 0:31 debug toolbar)
[comment]: <> (* 0:43 card.html)
[comment]: <> (* 0:47 select_related)
[comment]: <> (* 1:10 pip install django-extensions | python manage.py show_urls > geekshop_urls.txt)
[comment]: <> (* 1:12 validate_templates | pip install pydotplus graph_models | pycharm visual db)
[comment]: <> (* 1:17 sudo apt install siege | siege -f urls.txt -d1 -r29 -c1 | --debug)
[comment]: <> (* 1:23 http://89.108.81.8/auth/login/ POST username=...&password=... | # csrf)
[comment]: <> (* 1:34 login-url in siege)
[comment]: <> (* 1:42 hw)
[comment]: <> (##Задания 6)
[comment]: <> (* ssh подключение &#40;pycharm, cmd&#41;)
[comment]: <> (* восстановить функционал vk)
[comment]: <> (1. Установить приложение «django-debug-toolbar». Оценить время загрузки страниц. Найти самые медленные контроллеры. Заполнить таблицу с количеством запросов и дубликатов на страницах проекта.)
[comment]: <> (2. Визуализировать структуру моделей проекта при помощи «django_extensions», создать файл «geekshop_urls.txt» с URL-адресами проекта.)
[comment]: <> (3. Установить утилиту «siege» и провести функциональное тестирование. Зафиксировать результаты в текстовом файле &#40;какие контроллеры работали с ошибками&#41;.)
[comment]: <> (4. Провести нагрузочное тестирование отдельных страниц и записать результаты в таблицу.)
[comment]: <> (5. Провести тестирование в режиме интернета. Записать данные в таблицу. Определить условия, при которых начинаются отказы.)
[comment]: <> (6. Провести оптимизацию работы с БД в проекте. Оценить эффект.)
[comment]: <> (7. Визуализация БД)
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