from django.db import models
from django.db import models
class StuRecord(models.Model):
    stu_Fnm=models.CharField(max_length=200)
    stu_Lnm = models.CharField(max_length=200)
    stu_cls = models.CharField(max_length=20)
    stu_add = models.TextField()
    stu_mob = models.IntegerField()
    def __str__(self):
        return self.stu_Fnm


# Create your models here.
