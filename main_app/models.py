from django.db import models
from django.urls import reverse

# Create your models here.

class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  image = models.ImageField(upload_to='main_app/static/uploads/', default="")

  def __str__(self):
    return f"{self.name} {self.age}"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})