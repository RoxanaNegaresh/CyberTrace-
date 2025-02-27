from django.db import models

# Create your models here.
class VisitorLog(models.Model):
    ip_adderss = models.GenericIPAddressField(verbose_name="Visitor's ip", blank=True, null=True, protocol="both")
    user_agent = models.CharField(verbose_name="agent", null=True, blank=True, max_length=10)
    first_visit = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
    referrer = models.URLField(verbose_name="referrer", null=True, blank=True)
    path = models.CharField(max_length=255)
    duration = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.ip_adderss} - {self.last_visit} - {self.referrer} - {self.path} - {self.duration}"
    