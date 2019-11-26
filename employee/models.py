from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    profile_img = models.ImageField(upload_to='profile/')
    contact_no = models.CharField(max_length=14,unique=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    qualification = models.CharField(max_length=100)
    website = models.URLField(unique=True,null=True,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'employee'


class Skill(models.Model):
    title = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table ='skill'



class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    duration = models.DecimalField(decimal_places=1,max_digits=3)
    designation = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'experience'

