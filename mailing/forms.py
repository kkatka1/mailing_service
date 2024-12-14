from django import forms

from mailing.models import Mailing, Client, Message


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        #exclude = ('owner',)
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # exclude = ('owner',)
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # exclude = ('owner',)
        fields = '__all__'