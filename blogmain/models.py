from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length= 100)
    post = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title