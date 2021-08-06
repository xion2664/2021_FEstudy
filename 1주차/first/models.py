from django.db import models

# Create your models here.


class First(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to="first/", blank=True, null=True)

    def __str__(self):
        return self.title
