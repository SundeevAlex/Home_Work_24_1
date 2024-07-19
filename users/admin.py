from django.contrib import admin

from users.models import User
from .models import Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Payments)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('date_of_pay', 'course', 'lesson', 'amount', 'method',)
    search_fields = ('date_of_pay',)
    list_filter = ('date_of_pay', 'course', 'lesson', 'method', )
