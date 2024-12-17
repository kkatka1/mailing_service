from django import forms
from .models import Mailing, Client, Message




class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['message_id', 'date_of_first_dispatch', 'periodicity', 'client_list']
        widgets = {
            'date_of_first_dispatch': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'client_list': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['client_list'].queryset = Client.objects.filter(user=user)
            self.fields['message_id'].queryset = Message.objects.filter(user=user)




class MailingManagerForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['status', 'date_of_first_dispatch', 'periodicity', 'message_id']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['message_id'].queryset = Message.objects.filter(user=user)



class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ('fullname', 'email',)


