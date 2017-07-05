from django.db import models
from django.contrib.auth.models import User,Group
from django.contrib import admin

# Create your models here.

class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name

class Blog(models.Model):
    """docstring for Blogs"""
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)