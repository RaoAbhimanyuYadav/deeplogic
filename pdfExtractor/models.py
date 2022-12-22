from django.db import models

# Create your models here.


class Text(models.Model):
    filename = models.CharField(max_length=100)
    des = models.TextField(null=True, default=None)
    file = models.FileField(upload_to='pdf/', null=True, default=None)

    def __str__(self):
        return self.filename
