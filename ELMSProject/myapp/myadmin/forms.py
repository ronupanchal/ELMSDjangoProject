from django.forms import ModelForm
from .models import UserTable


class UserTableForm(ModelForm):
    class Meta:
        model = UserTable
        fields = "__all__"
