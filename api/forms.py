from django import forms
from .models import Parkir, Saldo

class ParkirForms(forms.ModelForm):
    class Meta:
        model = Parkir
        fields = ('booking_place',)
        exclude = ('booking_status','user',)

class SaldoForms(forms.ModelForm):
    class Meta:
        model = Saldo
        fields = ('saldo',)
        exclude = ('user',)