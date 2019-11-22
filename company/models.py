from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_no = models.CharField(unique=True,max_length=10)
    website = models.URLField(unique=True,null=True,blank=True)
    profile = models.ImageField(upload_to='profile/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'
