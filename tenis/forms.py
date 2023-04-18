from django import forms
from tenis.models import NovoTenis

class TenisForm(forms.ModelForm):
    class Meta:
        model = NovoTenis
        fields = ('__all__')