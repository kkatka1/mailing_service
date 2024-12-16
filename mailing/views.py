from lib2to3.fixes.fix_input import context
from random import sample

from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from mailing.forms import MailingForm, MessageForm, ClientForm
from mailing.models import Client, Mailing, Message

from blog.models import Post

from django.http import HttpResponseForbidden

from django.http import HttpResponseForbidden




class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "mailing/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем случайные посты
        all_posts = list(Post.objects.all())
        context["random_posts"] = sample(
            all_posts, min(len(all_posts), 3)
        )  # Случайные посты

        # Добавляем количество уникальных клиентов
        context["unique_clients"] = Client.objects.values("email").distinct().count()

        # Добавляем информацию о рассылках
        context["total_mailings"] = Mailing.objects.count()  # Все рассылки
        context["active_mailings"] = Mailing.objects.filter(
            status="B"
        ).count()  # Активные рассылки

        return context


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    context_object_name = "mailings"

    def get_queryset(self):
        return Mailing.objects.filter(user=self.request.user).order_by('-created_at')


class MailingDetailView(DetailView):
    model = Mailing
    context_object_name = "mailing"


class MailingCreateView(CreateView, LoginRequiredMixin):
    model = Mailing
    form_class = MailingForm
    template_name = "mailing/mailing_form.html"
    success_url = reverse_lazy("mailing:mailing_list")

    def get_context_data(self, **kwargs):
        '''При создании рассылки показывает только клиентов пользователя'''
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.filter(user=self.request.user)
        return context

    def get_form_kwargs(self):
        '''Передаем текущего пользователя в форму'''
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Добавляем текущего пользователя
        return kwargs

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.user = user
        mailing.save()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")


# Сообщения
class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user)


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    # permission_required = 'mailing.add_message'
    success_url = reverse_lazy(
        "mailing:message_list",
    )

    def form_valid(self, form):
        '''Привязываем сообщение к пользователю'''
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def form_valid(self, form):
    #   mailing = form.save()
    #  user = self.request.user
    # mailing.owner = user
    # mailing.save()
    # return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse_lazy("mailing:message_list")


class MessageDeleteView(DeleteView):
    model = Message

    def get_success_url(self):
        return reverse_lazy("mailing:message_list")


class MessageDetailView(DetailView):
    model = Message


# Клиенты


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = "clients"
    paginate_by = 10

    def get_queryset(self):
        '''Возвращает список клиентов текущего пользователя, отсортированный по дате добавления'''
        return Client.objects.filter(user=self.request.user).order_by('-created_at')


class ClientDetailView(DetailView):
    model = Client
    context_object_name = "client"


#   def get_context_data(self, **kwargs):
#      context = super().get_context_data(**kwargs)
#     print(context['clients'])
#    return context


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client_list")

    #  def form_valid(self, form):
    ##    user = self.request.user
    #   mailing.owner = user
    #  mailing.save()
    # return super().form_valid(form)

    def form_valid(self, form):
        '''Привязываем клиента к пользователю'''
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("mailing:client_list")
