from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

from django.urls import reverse
from django.utils import timezone

## AutoSlug Modules
from autoslug import AutoSlugField

from ckeditor_uploader.fields import RichTextUploadingField 

STATUS = (
    (0, "Draft"),
    (1, "Publish"))


class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    title = models.CharField(max_length=250, null = True)
    slug = AutoSlugField(populate_from='title', null = True)
    image = models.ImageField(upload_to='media/images/', blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now= True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='weblog_project')
    content = RichTextUploadingField(null=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
    
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('weblog:post_detail', kwargs={'slug': self.slug})