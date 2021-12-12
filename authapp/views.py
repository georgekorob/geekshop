from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from adminapp.mixins import PageTitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm

# Create your views here.
from authapp.models import User
from basketapp.models import Basket


class UserLoginView(PageTitleMixin, LoginView):
    form_class = UserLoginForm
    title = 'авторизация'


class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass


class UserRegisterView(PageTitleMixin, FormView):
    model = User
    form_class = UserRegisterForm
    template_name = 'authapp/register.html'
    title = 'регистрация'
    success_url = reverse_lazy('authapp:login')

    def form_valid(self, form):
        messages.success(self.request, 'Вы успешно зарегистрировались!')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class UserProfileView(LoginRequiredMixin, PageTitleMixin, UpdateView):
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')
    template_name = 'authapp/profile.html'
    title = 'редактирование'

    def form_valid(self, form):
        messages.success(self.request, "Вы успешно отредактированы!")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        baskets = Basket.objects.filter(user=self.request.user)
        context['baskets'] = baskets
        context['total_sum'] = sum(basket.sum for basket in baskets)
        context['total_quantity'] = sum(basket.quantity for basket in baskets)
        return context
