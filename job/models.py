from django.db import models
from company.models import Company
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    image = models.ImageField(upload_to='job/')
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table ='job'