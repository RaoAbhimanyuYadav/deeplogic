from django.db import models

# Create your models here.


class Text(models.Model):
    filename = models.CharField(max_length=100)
    des = models.TextField()

    def __str__(self):
        return self.filename
