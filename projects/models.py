from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils import timezone


## AutoSlug Modules
from autoslug import AutoSlugField

STATUS = (
    (0, "Draft"),
    (1, "Publish"))


class Project(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='projects_author')
    title = models.CharField(max_length=250, null = True)
    description = models.CharField(max_length=250, null = True)
    budget = models.CharField(max_length=250, null = True)
    slug = AutoSlugField(populate_from='title', null = True)
    image = models.FileField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(default=timezone.now)


    class Meta:

        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('projects:projects_detail', kwargs={'slug': self.slug})