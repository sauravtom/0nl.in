from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email', 'template']

admin.site.register(Profile, ProfileAdmin)