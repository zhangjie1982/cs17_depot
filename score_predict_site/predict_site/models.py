from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(u"用户名", max_length=100)
    password = models.CharField(u"密码", max_length=100)
    stu_no = models.CharField(u"学号", max_length=100)
    name = models.CharField(u"姓名", max_length=100)
    gender = models.CharField(u"性别", max_length=100)
    major = models.CharField(u"专业", max_length=100)
    portrait = models.ImageField(upload_to="static/user_portrait")
    mail = models.CharField(u"邮箱", max_length=100)
    status = models.CharField(u"状态/个性签名", max_length=255, null=True)