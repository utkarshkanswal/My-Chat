from django.contrib import admin
from UserManagement.models import User,Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_display=['full_name','bio',"image"]



admin.site.register(User, UserAdmin)
admin.site.register(Profile,ProfileAdmin)
