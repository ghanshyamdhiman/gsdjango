from django.db import models

class Blog(model.Model):
  title = models.CharField(max_length=123)
  content = models.TextField()
 
  def __str__(self):
        return self.title

# Create your models here.
