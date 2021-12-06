from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=60)
    category = models.CharField(max_length=25, default="book")
    subCategory = models.CharField(max_length=25, default="subBook")
    slug = models.SlugField(max_length=70, unique_for_date='publish')
    author = models.CharField(max_length=30)
    body = models.TextField()
    link = models.URLField(max_length=120, default='example.com')
    secondLink = models.TextField(max_length=120, default='this')
    thirdLink = models.URLField(max_length=120, default='secondExample.com')
    image = models.ImageField("Image", blank=True, null=True, upload_to="images/")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

   # def get_absolute_url(self):
    #    return reverse('post_detail', kwargs={'slug': self.slug})
