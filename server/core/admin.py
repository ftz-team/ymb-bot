from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username')


@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tg_id')
