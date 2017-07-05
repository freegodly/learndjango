from django.contrib import admin
from weblog.models import *

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','tag_name','create_time')
    list_per_page = 15
    ordering = ("id",)



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('caption','author','publish_time','update_time')
    list_per_page = 15
    ordering = ("caption",)
