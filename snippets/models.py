from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Language(models.Model):
    name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Snippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    snippet = models.TextField(blank=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    def time_lap(self):
        delta = datetime.now().date() - self.created.date()
        if delta.days < 1:
            fecha = "hace menos de un día."
        elif delta.days == 1:
            fecha = "1 día."
        else:
            fecha = f'{delta.days} días.'

        return fecha

    def __str__(self):
        return self.name
