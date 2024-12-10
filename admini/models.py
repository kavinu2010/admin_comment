from django.db import models

# Create your models here.
class Admin_comment(models.Model):
  title=models.CharField(max_length=200)
  comment=models.TextField()
  createdat=models.DateField()

  def __str__(self):
    return f'{self.title}:{self.comment}'