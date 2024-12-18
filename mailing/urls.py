from linecache import cache
from django.urls import path
from django.views.decorators.cache import cache_page
from mailing import views
from mailing.apps import MailingConfig
from mailing.models import Client
from mailing.views import (MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView, MailingDeleteView,
    MessageCreateView, MessageUpdateView, MessageDeleteView, MessageDetailView, MessageListView, HomePageView, ClientListView,
    ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView,
)
app_name = MailingConfig.name

urlpatterns = [
    # рассылка
    path("mailing/", cache_page(60)(MailingListView.as_view()), name="mailing_list"),
    path("create/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing/<int:pk>/view/", MailingDetailView.as_view(), name="mailing_detail"),
    path("<int:pk>/update/", MailingUpdateView.as_view(), name="mailing_update"),
    path("<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing_delete"),
    path("", HomePageView.as_view(), name="home"),
    # сообщения
    path("message/", MessageListView.as_view(), name="message_list"),
    path("message/create/", MessageCreateView.as_view(), name="message_create"),
    path(
        "message/<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"
    ),
    path(
        "message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"
    ),
    path("mailing/<int:pk>/view/", MessageDetailView.as_view(), name="message_detail"),
    # клиенты
    path("client/", ClientListView.as_view(), name="client_list"),
    path("client/create/", ClientCreateView.as_view(), name="client_create"),
    path("client/<int:pk>/view/", ClientDetailView.as_view(), name="client_detail"),
    path("client/<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),
]
