from django.db import models


class HomeImage(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='home/', null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=120)
    social = models.CharField(max_length=120, default="#")
    image = models.ImageField(upload_to='home/', null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
