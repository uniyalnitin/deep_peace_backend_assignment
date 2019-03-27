from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'company_name', 'city', 'state', 'zip', 'email', 'web', 'age')
# Register your models here.
