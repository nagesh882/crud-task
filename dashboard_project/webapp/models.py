from django.db import models
from autoslug import AutoSlugField


class CRUD(models.Model):

    title = models.CharField(max_length=255, default=None, null=False, unique=True)
    description = models.TextField(default=None, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', default=None, null=False, unique=True)

    def __str__(self):
        return self.title