# Основы Django Framework

Репозиторий для сдачи домашнего задания.

Коробанов Георгий.

##Урок 8
* 0:16 фильтрация по категориям
* 0:22 пагинация view
* 0:35 пагинация template
* 0:50 CBV
* 1:13 update
* 1:27 delete

##Задания 8
[comment]: <> (1. Организовать фильтрацию продуктов по категориям.)
[comment]: <> (2. Организовать постраничный вывод в каталоге.&#40;по возможности сделать на CBV&#41;)
[comment]: <> (3. Перевести как можно больше контроллеров в проекте на CBV. Обязательно выполнение 3его задания. Это необходимо для следующего уровня!)
[comment]: <> (5. Обязательно выполните эти задания. Это необходимо для следующего уровня!)
4. *Перевести админку на AJAX.

[comment]: <> (##Задания 3)
[comment]: <> (1. Создать модель пользователя в проекте. Обязательно добавить поле с изображением и возраст . Выполнить настройки в файле конфигурации.)
[comment]: <> (2. Реализовать механизм аутентификации и авторизации в проекте.)
[comment]: <> (3. Реализовать механизм регистрации пользователя. И не забыть добавить logout)
[comment]: <> (4. Создать base.html для login.html и register.html в templates папке приложения authapp.)
[comment]: <> (* ##Урок 4)
[comment]: <> (* Создание приложения authapp, подключение модели)
[comment]: <> (* Создание модели User, изменение структуры urls)
[comment]: <> (* Регистрация приложения в admin)
[comment]: <> (* Обновление базы данных)
[comment]: <> (* Создание шаблонов и форм в authapp)
[comment]: <> (* Создание views, редактирование urls)
[comment]: <> (* Форма для регистрации)
[comment]: <> (* Шаблон и отображение регистрации)
[comment]: <> (* Добавление logout и ссылки на admin)
[comment]: <> (##Задания 4)
[comment]: <> (1. Создать модель пользователя в проекте. Обязательно добавить поле с изображением и возраст . Выполнить настройки в файле конфигурации.)
[comment]: <> (2. Реализовать механизм аутентификации и авторизации в проекте.)
[comment]: <> (3. Реализовать механизм регистрации пользователя. И не забыть добавить logout)
[comment]: <> (4. Создать base.html для login.html и register.html в templates папке приложения authapp.)
[comment]: <> (5. *Разобраться с механизмом валидации данных формы. Создать свои валидаторы.)
[comment]: <> (##Урок 5)
[comment]: <> (* 0:17 validator clean_username)
[comment]: <> (* 0:37 errors form.non_field_errors)
[comment]: <> (* 0:47 error | escape)
[comment]: <> (* 0:50 messages)
[comment]: <> (* 0:56 profile)
[comment]: <> (* 1:10 form template)
[comment]: <> (* 1:20 view instance)
[comment]: <> (* 1:24 фото пользователя)
[comment]: <> (* 1:27 post hw token multi-data url)
[comment]: <> (* 1:34 baskets)
[comment]: <> (* 1:49 backet_add)
[comment]: <> (* 2:07 sum)
[comment]: <> (* 2:15 basket_remove)
[comment]: <> (* 2:19 @login_required)
[comment]: <> (##Задания 5)
[comment]: <> (1. Реализовать механизм редактирования информации о пользователе &#40;личный кабинет&#41; в проекте. Обязательно реализовать механизм загрузки аватара пользователя и валидация на форме.)
[comment]: <> (2. Добавиь обработку ошибок для страниц авторизации и регистрации. И добавить сообщения об успешних действиях.)
[comment]: <> (3. Создать приложение корзины. Создать новую модель для корзины.)
[comment]: <> (4. Добавить включенный шаблон basket.html в profile.html. Реализовать вывод товаров корзины.)
[comment]: <> (5. Реализовать механизм добавления и удаление товара корзины.)
[comment]: <> (6. Создать метод sum&#40;&#41;, который будет отвечать за вывод итоговой стоимости для товара.)
[comment]: <> (7. Написать в модели корзины методы для определения общего количества и стоимости добавленных товаров. Вывести эти величины в шаблоне.)
[comment]: <> (8. *Добавить обработку ошибок для страницы профиля &#40;личного кабинета&#41;. И добавить сообщения об успешних действиях.)
[comment]: <> (##Урок 6)
[comment]: <> (* 0:13 total and sum)
[comment]: <> (* 0:19 property)
[comment]: <> (* 0:20 успешно сохранили профиль html)
[comment]: <> (* 0:30 message.success)
[comment]: <> (* 0:47 styles)
[comment]: <> (* 0:54 AJAX)
[comment]: <> (* 0:56 basket.js)
[comment]: <> (* 1:11 basket_edit)
[comment]: <> (* 1:21 send command from ajax)
[comment]: <> (* 1:35 ДЗ)
[comment]: <> (* 1:43 AJAX для добавления в корзину)
[comment]: <> (##Задания 6)
[comment]: <> (1. Добавить к модели корзины методы total_sum,&#40;&#41; и total_quantity&#40;&#41; и вывести в меню количество товара и их полную стоимость.)
[comment]: <> (2. Защитить доступ к корзине и личному кабинету декоратором @login_required.)
[comment]: <> (3. Реализовать асинхронное редактирование количества товаров в корзине при помощи AJAX.)
[comment]: <> (4. Сделать шаблон для детализации товара *)
[comment]: <> (##Урок 7)
[comment]: <> (* 0:13 DetailView)
[comment]: <> (* 0:24 админка)
[comment]: <> (* 0:37 шаблоны)
[comment]: <> (* 0:52 запуск admin)
[comment]: <> (* 1:00 контроллеры)
[comment]: <> (##Задания 7)
[comment]: <> (1. Создать приложение админки и интегрировать его в проект.)
[comment]: <> (2. Реализовать механизм CRUD для объектов пользователей магазина. Можно полностью удалять объекты &#40;не использовать свойство is_active&#41;)
[comment]: <> (3. Реализовать механизм CRUD для объектов категорий И товара. Можно полностью удалять объекты &#40;не использовать свойство is_active&#41;)
[comment]: <> (4. Защитить доступ к админке декоратором @user_passes_test.)
[comment]: <> (5. *Реализовать удаление через свойство is_active.)
[comment]: <> (6. *Реализовать «подсветку» в админке неактивных объектов пользователей и категорий.)
