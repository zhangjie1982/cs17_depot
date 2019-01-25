from django.contrib import admin
from predict_site.models import Users

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'stu_no', 'name', 'gender', 'major', 'portrait', 'mail')


admin.site.register(Users, UsersAdmin)
