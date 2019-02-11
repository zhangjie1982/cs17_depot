from django.contrib import admin
from predict_site.models import Users, Courses


# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'stu_no', 'name', 'gender', 'major', 'portrait', 'mail', 'status','Uphy', 'Amath', 'Lalg', 'C', 'Cpp')


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro', 'course_id')


admin.site.register(Users, UsersAdmin)
admin.site.register(Courses, CoursesAdmin)
