from lib2to3.fixes.fix_input import context
from random import sample

from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, TemplateView

from mailing.forms import MailingForm, MessageForm, ClientForm
from mailing.models import Client, Mailing, Message

from blog.models import Post



class HomePageView(TemplateView):
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем случайные посты
        all_posts = list(Post.objects.all())
        context['random_posts'] = sample(all_posts, min(len(all_posts), 3))  # Случайные посты

        # Добавляем количество уникальных клиентов
        context['unique_clients'] = Client.objects.values('email').distinct().count()

        # Добавляем информацию о рассылках
        context['total_mailings'] = Mailing.objects.count()  # Все рассылки
        context['active_mailings'] = Mailing.objects.filter(status='B').count()  # Активные рассылки

        return context

#def home(request):
 #   total_mailings = Mailing.objects.count()
    #active_mailings = Mailing.objects.filter(is_active=True).count()
  #  unique_clients = Client.objects.values("email").distinct().count()
  #  random_articles = Blog.objects.order_by("?")[:3]

  #  context = {
  #      "total_mailings": total_mailings,
  #      #"active_mailings": active_mailings,
  #      "unique_clients": unique_clients,
  #      "random_articles": random_articles,
  #  }
  #  return render(request, "mailing/home.html", context)

# Рассылки

class MailingListView(ListView):
    model = Mailing
    context_object_name = 'mailings'


class MailingDetailView(DetailView):
    model = Mailing
    context_object_name = 'mailings'

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')



# Сообщения
class MessageListView(ListView):
    model = Message

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    #permission_required = 'mailing.add_message'
    success_url = reverse_lazy('mailing:message_list',)

class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse_lazy('mailing:message_list')


class MessageDeleteView(DeleteView):
    model = Message

    def get_success_url(self):
        return reverse_lazy('mailing:message_list')

class MessageDetailView(DetailView):
    model = Message



#Клиенты

class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'
    paginate_by = 10

class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'client'

 #   def get_context_data(self, **kwargs):
  #      context = super().get_context_data(**kwargs)
   #     print(context['clients'])
    #    return context

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')







