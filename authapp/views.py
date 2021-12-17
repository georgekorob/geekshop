from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView

from adminapp.mixins import PageTitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm

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
        user = form.save()
        if self.send_verify_link(user):
            messages.success(self.request, 'Ссылка для активации учетной записи отправлена Вам на почту!')
            super().form_valid(form)
            return HttpResponseRedirect(self.get_success_url())
        messages.error(self.request, form.errors)
        return render(self.request, self.template_name, {'form', form})

    def send_verify_link(self, user):
        verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
        subject = f'Для активации учетной записи {user.username} пройдите по ссылке'
        message = f'Для подтверждения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activate_key):
        try:
            user = User.objects.get(email=email)
            if user and user.activation_key == activate_key and not user.is_activation_key_expires():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(self, user)
            return render(self, 'authapp/verification.html')
        except Exception as e:
            return HttpResponseRedirect(reverse('index'))


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
        context['profile'] = UserProfileEditForm(instance=self.request.user.userprofile)
        baskets = Basket.objects.filter(user=self.request.user)
        # context['baskets'] = baskets
        context['total_sum'] = sum(basket.prod for basket in baskets)
        context['total_quantity'] = sum(basket.quantity for basket in baskets)
        return context

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(data=request.POST,files=request.FILES,instance=request.user)
        profile_form = UserProfileEditForm(request.POST,instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
        return redirect(self.success_url)
