from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.Model):
    DEFAULT_ROLES = [
    ( "Admin" , "admin"),
    ( "Moderator" , "moderator"),
    ( "User" ,"user"), 
    ]
    name=models.CharField(verbose_name="Role name", max_length=20, unique=True, null=True, blank=True)
    is_default=models.BooleanField(default=True)
    
class User(AbstractUser):
    name = models.CharField(verbose_name="Full Name", blank=True, null=True, max_length=30)
    last_ip = models.GenericIPAddressField(verbose_name="Last IP Address", blank=True, null=True, protocol="both")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Role", blank=True, null=True)






    # @classmethod
    # def create_defaults(cls):
    #     for label, code in cls.DEFAULT_ROLES:
    #         cls.objects.get_or_create(name=code, is_default=True)





#  @classmethod
#     def create_defaults(cls):
#         for code, label in cls.DEFAULT_ROLES:
#             cls.objects.get_or_create(name=label, is_default=True)

# class Users(AbstractUser):
#     role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)