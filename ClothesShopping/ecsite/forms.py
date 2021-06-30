from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from .models import Store


class SignUpFormStore(UserCreationForm):
    class Meta:
        model = Store
        fields = ("email", "store_name", "password")








