from django.db import models

# Create your models here.

class Users(models.Model):
    Name=models.CharField(max_length=30)
    Message=models.Field(max_length=300)
    date = models.DateTimeField(auto_now_add=True, db_index=True, )


