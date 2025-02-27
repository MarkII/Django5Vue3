from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import Users

# Register your models here.

@admin.register(Users)
class PanelAdminUser(BaseUserAdmin):
    model =  Users
    fields = ['email','username','first_name','last_name']
    fieldsets = []