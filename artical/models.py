from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.



status=(
    ('draft','draft'),
    ('publish','publish'),
)

class Tag(models.Model):
    name=models.CharField(max_length=25)

class Artical(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,related_name="tags")
    title=models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(choices=status,default='publish',max_length=50)

    def __str__(self):
        return str(self.id)

class ArticalTag(models.Model):
    artical=models.ForeignKey(Artical,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self) :
        return str(self.id) +self.name

