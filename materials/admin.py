from django.contrib import admin
from .models import Lesson, Course


@admin.register(Lesson)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'description', 'image', 'link_to_video',)
    search_fields = ('name',)
    list_filter = ('name', 'course', )


@admin.register(Course)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'owner',)
    search_fields = ('name',)
    list_filter = ('name',)
