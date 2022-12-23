from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Text(models.Model):
    owner = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    filename = models.CharField(max_length=100)
    des = models.TextField(null=True, default=None)
    file = models.FileField(upload_to='pdf/', null=True, default=None)

    def __str__(self):
        return self.filename
