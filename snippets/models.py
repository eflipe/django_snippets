from __future__ import unicode_literals

from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50, blank=False)
    # slug blank=False

    def __str__(self):
        return self.name


class Snippet(models.Model):
    # user = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    snippet = models.TextField(blank=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name
