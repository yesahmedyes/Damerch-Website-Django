from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from merch.utils import unique_slug
from django.contrib.auth.models import User


class People(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="artist")
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    keywords = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    link = models.CharField(max_length=120, default="https://www.youtube.com/")

    def get_url(self):
        return reverse("people:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


def people_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug(instance)


pre_save.connect(people_pre_save, sender=People)
