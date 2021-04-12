from .models import Deal
from django.forms import ModelForm, TextInput, NumberInput, DateInput


class DealForm(ModelForm):
    class Meta:
        model = Deal
        fields = ['customer', 'item', 'total', 'quantity', 'date']
        widgets = {
            'customer': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин'
            }),
            'item': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование товара'
            }),
            'total':  NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сумму сделки '
            }),
            'quantity':  NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество товара, шт'
            }),
            'date':  DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату и время регистрации сделки в формате 2018-12-16 00:01:13.013713'
            }),

        }

