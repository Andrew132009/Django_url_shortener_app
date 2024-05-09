from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone
from tinymce import models as mce_models


# Create your models here.
class Page(MPTTModel):
    name = models.CharField('Название страницы', max_length=100, db_index=True)
    url = models.SlugField('URL страницы', max_length=255, db_index=True, unique=True)
    active = models.BooleanField('Отображать в меню?', default=True)
    parent = TreeForeignKey('self', blank=True, null=True, db_index=True, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ('tree_id', 'level')

    def __str__(self):
        return self.name



class Text(models.Model):
    page_id = TreeForeignKey(Page, verbose_name='Страница', db_index=True, on_delete=models.CASCADE)
    name = models.CharField('Имя в админке', max_length=255, db_index=True)
    title = models.CharField('SEO title', max_length=255)
    keywords = models.CharField('SEO keywords', max_length=255)
    description = models.CharField('SEO description', max_length=255)
    full_text = mce_models.HTMLField('Контент', blank=True, default='<p>Я новый текст</p>')
    date_create = models.DateTimeField('Дата создания текста', auto_now_add=True)
    date_update = models.DateTimeField('Дата изменения текста', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'
