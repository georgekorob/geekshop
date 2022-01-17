from django.conf import settings
from django.test import TestCase
from django.test.client import Client

# Create your tests here.
from django.urls import reverse

from authapp.models import User


class UserManagementTestCase(TestCase):
    username = 'django'
    email = 'djano@mail.ru'
    password = 'geekshop'

    new_user_data = {
        'username': 'djangouser',
        'first_name': 'Django',
        'last_name': 'Djangovski',
        'password1': 'geekbrains',
        'password2': 'geekbrains',
        'email': 'geekshop@mail.ru',
        'age': 31

    }

    # Предустановка параметров
    def setUp(self):
        self.user = User.objects.create_superuser(self.username, email=self.email, password=self.password)
        self.client = Client()

    # 1. Проверка авторизации
    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Проверяем что пользователь не авторизованный и является анонимным
        self.assertTrue(response.context['user'].is_anonymous)
        # пробуем авторизоваться
        self.client.login(username=self.username, password=self.password)
        # отправляем на авторизацию
        response = self.client.get(reverse('authapp:profile'))
        # Проверяем что вы авторизовались
        self.assertEqual(response.status_code, 200)

    # 2. Проверка регистрации
    def test_register(self):
        # логин без данных пользователя
        response = self.client.get('/users/register/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'регистрация')
        self.assertTrue(response.context['user'].is_anonymous)

        # начинаем регистрироваться
        response = self.client.post(reverse('authapp:register'), data=self.new_user_data)
        # print(response.)
        self.assertEqual(response.status_code, 302)
        # Вспомним логику у нас есть пользователь не активированные
        # его нужно активировать с помошью ссылки которая отправляется на емайл
        # что нам нужно сделать? давайте ее соберем сами

        # Получаем пользователя
        new_user = User.objects.get(username=self.new_user_data['username'])
        # готовим ссылку
        activation_url = f"{settings.DOMAIN_NAME}/users/verify/{self.new_user_data['email']}/{new_user.activation_key}/"
        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, 302)
        # обновляем пользователя в базе данных
        new_user.refresh_from_db()
        self.assertTrue(new_user.is_active)

        # данные нового пользователя
        self.client.login(username=self.new_user_data['username'], password=self.new_user_data['password1'])
        # логинимся
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_anonymous)
        # проверяем главную страницу
        response = self.client.get('/')
        self.assertContains(response, text=self.new_user_data['username'], status_code=200)

    def test_profile_login_redirect(self):
        # без логина должен переадресовать
        response = self.client.get('/users/profile/')
        self.assertEqual(response.url, '/users/login/?next=/users/profile/')
        self.assertEqual(response.status_code, 302)

        # с логином все должно быть хорошо
        self.client.login(username=self.username, password=self.password)

        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request['PATH_INFO'], '/users/profile/')
        self.assertIn('Корзина пуста', response.content.decode())

    def test_user_logout(self):
        # данные пользователя
        self.client.login(username=self.username, password=self.password)

        # логинимся
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_anonymous)

        # выходим из системы
        response = self.client.get('/users/logout/')
        self.assertEqual(response.status_code, 302)

        # главная после выхода
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)

    def test_user_wrong_register(self):
        new_user_data = {
            'username': 'teen',
            'first_name': 'Мэри',
            'last_name': 'Поппинс',
            'password1': 'geekbrains',
            'password2': 'geekbrains2',
            'email': 'merypoppins@geekshop.local'}

        response = self.client.post('/users/register/', data=new_user_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password2', 'Введенные пароли не совпадают.')
