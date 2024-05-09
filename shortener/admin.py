from django.contrib import admin
from .models import Links, Clicks
# Register your models here.


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_url', 'clicks_qty',)


@admin.register(Clicks)
class ClicksAdmin(admin.ModelAdmin):
    list_display = ('link_id', 'created_at',)