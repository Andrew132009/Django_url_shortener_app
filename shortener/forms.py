from django import forms
from .models import Links


class CreateUrlForm(forms.ModelForm):  # формами ModelForm легче управлять при создании новых объектов БД
    class Meta:
        model = Links
        fields = ["name", "original_url", ]  # указываю поля, которые должны будут отображаться в форме
    # exclude = ["user", "short_url", "clicks_qty", "created_at",]
    # fields = "__all__" <- оставить ВСЕ поля модели для отображения в форме
