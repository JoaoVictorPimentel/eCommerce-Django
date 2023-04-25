from django import forms
from tenis.models import Tenis

class TenisForm(forms.ModelForm):
    class Meta:
        model = Tenis
        fields = ('__all__')