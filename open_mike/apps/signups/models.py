from django.db import models

# Create your models here.
class SignUp(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    act_name = models.CharField(max_length=200)
    act_description = models.TextField(max_length=200)
    act_requests = models.TextField(max_length=200)

    def __unicode__(self):
        return self.name
