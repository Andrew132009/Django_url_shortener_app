from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # фиксируем модель пользователя из Django


# Create your models here.
class Links(models.Model):
    name = models.CharField('Имя ссылки: ', max_length=100, default=f'Link {id}')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField('Оригинальная ссылка: ', max_length=255)
    short_url = models.CharField('Сокращенная ссылка: ', max_length=255)
    clicks_qty = models.IntegerField('Количество кликов: ', default=0)
    created_at = models.DateTimeField('Дата создания: ', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'


class Clicks(models.Model):
    link_id = models.ForeignKey('Links', on_delete=models.CASCADE)
    ip_address = models.CharField('IP адрес устройства: ', max_length=100)
    user_agent = models.CharField('User-Agent: ', max_length=255)
    created_at = models.DateTimeField('Дата перехода: ', auto_now=True)

    class Meta:
        verbose_name = 'Клик'
        verbose_name_plural = 'Клики'

    def __str__(self):
        return f'Клик по ссылке {self.link_id}'
