from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView

app_name = MailingConfig.name

urlpatterns= [
    path ('', MailingListView.as_view(), name='mailing_list'),

]