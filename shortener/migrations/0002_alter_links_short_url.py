# Generated by Django 4.2.11 on 2024-05-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='short_url',
            field=models.CharField(max_length=255, verbose_name='Shortened link: '),
        ),
    ]