from django.contrib import admin

# Register your models here.
from .models import Newuser

@admin.register(Newuser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ['username','email','first_name', 'last_name','is_staff','is_superuser']
    fields = ('username','email','first_name','last_name',)
