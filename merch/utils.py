import random
import string
from django.utils.text import slugify


def random_string():
    a = ''
    for i in range(4):
        a = a + random.choice(string.ascii_lowercase+string.digits)
    return a


def unique_slug(instance, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        try:
            slug = slugify(instance.title)
        except AttributeError:
            slug = slugify(instance.name)

    temp_instance = instance.__class__
    qs_exits = temp_instance.objects.filter(slug=slug).exists()
    if qs_exits:
        new_slug = "{slug}-{temp}".format(slug=slug, temp=random_string())
        return unique_slug(instance, new_slug=new_slug)
    return slug


