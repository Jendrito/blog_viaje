from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_profile
# Register your models here.

admin.site.register(User_profile)