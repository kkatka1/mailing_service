from lib2to3.fixes.fix_input import context
from random import sample

from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, TemplateView
from mailing.models import Client, Mailing

from blog.models import Blog
from mailing.models import Mailing, Client

def home(request):
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(is_active=True).count()
    unique_clients = Client.objects.values("email").distinct().count()
    random_articles = Blog.objects.order_by("?")[:3]

    context = {
        "total_mailings": total_mailings,
        "active_mailings": active_mailings,
        "unique_clients": unique_clients,
        "random_articles": random_articles,
    }
    return render(request, "mailing/home.html", context)


class MailingListView(ListView):
    model = Mailing
    context_object_name = 'mailings'


class MailingDetailView(DetailView):
    model = Mailing
    context_object_name = 'mailings'

class MailingCreateView(CreateView):
    model = Mailing
    template_name = 'mailing/mailing_form.html'
    fields = ['date_of_first_dispatch', 'periodicity', 'status', 'message_id', 'client_list', 'is_published']
    success_url = reverse_lazy('mailing:mailing_list')

class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ['date_of_first_dispatch', 'periodicity', 'status', 'message_id', 'client_list', 'is_published']
    success_url = reverse_lazy('mailing:mailing_list')

class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')



#class ClientListView(ListView):
  #  model = Mailing
 #   context_object_name = 'mailings'

class ClientDetailView(DetailView):
    model = Mailing
    context_object_name = 'mailings'

class ClientCreateView(CreateView):
    model = Mailing
    template_name = 'mailing/mailing_form.html'
    fields = ['date_of_first_dispatch', 'periodicity', 'status', 'message_id', 'client_list', 'is_published']
    success_url = reverse_lazy('mailing:mailing_list')

class ClientUpdateView(UpdateView):
    model = Mailing
    fields = ['date_of_first_dispatch', 'periodicity', 'status', 'message_id', 'client_list', 'is_published']
    success_url = reverse_lazy('mailing:mailing_list')

class ClientDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')






