from django.contrib import admin
from .models import Page, Text
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter


# Register your models here.
@admin.register(Page)
class PageAdmin(DraggableMPTTAdmin):
    search_fields = ("name_startswith",)
    list_display = ("tree_actions", "indented_title", "name", "url", "active",)
    list_filter = ("active",)
    list_display_links = ("indented_title",)
    prepopulated_fields = {"url": ('name',)}


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "date_create", "date_update", "page_id",)
    list_filter = (
     ("page_id", TreeRelatedFieldListFilter,),
     )
    list_editable = ("title",)



