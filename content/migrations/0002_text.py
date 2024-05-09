# Generated by Django 4.2.11 on 2024-04-28 16:26

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Имя в админке')),
                ('title', models.CharField(max_length=255, verbose_name='SEO title')),
                ('keywords', models.CharField(max_length=255, verbose_name='SEO keywords')),
                ('description', models.CharField(max_length=255, verbose_name='SEO description')),
                ('full_text', tinymce.models.HTMLField(blank=True, default='<p>Я новый текст</p>', verbose_name='Контент')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания текста')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения текста')),
                ('page_id', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Тексты',
            },
        ),
    ]
