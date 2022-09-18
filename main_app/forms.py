from django.forms import ModelForm
from .models import Accessory

class AccessoryForm(ModelForm):
    class Meta:
        model = Accessory
        fields = ['name', 'number', 'date_purchased']