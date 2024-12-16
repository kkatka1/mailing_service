import secrets
import random
import string

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(email, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


# def change_password(request):
#    if request.method == 'POST':
#        email = request.POST.get('email')
#        try:
#            user = User.objects.get(email=email, is_active=True)
#        except User.DoesNotExist:
#            return render(request,'users/change_password.html', {'error': 'Пользователь не найден'})
#        else:
#            new_password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
#            user.password = make_password((new_password))
#            user.save()
#            send_mail(
#                subject='Восстановление пароля',
#                message=f'Ваш новый пароль: {new_password}',
#                from_email=EMAIL_HOST_USER,
#                recipient_list=[user.email],
#               fail_silently=False
#            )
#            return redirect(reverse('users:login'))
#    return render(request, 'users/change_password.html')

#
