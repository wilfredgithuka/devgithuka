from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils import timezone

## AutoSlug Modules
from autoslug import AutoSlugField

from ckeditor_uploader.fields import RichTextUploadingField 

STATUS = (
    (0, "Draft"),
    (1, "Publish"))


class Project(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='projects_author')
    title = models.CharField(max_length=250, null = True)
    description = RichTextUploadingField(null = True)
    tagline = models.CharField(max_length=250, null = True)
    budget = models.CharField(max_length=250, null = True)
    slug = AutoSlugField(populate_from='title', null = True)
    progress = models.IntegerField(null = True)
    github = models.CharField(max_length=250, null = True)
    image = models.ImageField(upload_to='media/images/', blank=True)
    manuals = models.FileField(upload_to='manuals/', null=True, blank=True, help_text='Manuals')
    created_on = models.DateTimeField(default=timezone.now)


    class Meta:

        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('projects:projects_detail', kwargs={'slug': self.slug})