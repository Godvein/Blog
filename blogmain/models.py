from django.db import models


# Create your models here.
class blogs(models.Model):
    title = models.CharField(max_length= 100)
    post = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title