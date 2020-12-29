import datetime
from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _



class Movie(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('Title'))
    storyline = models.TextField(max_length=200, verbose_name=_('StoryLine'))
    cover_image = models.ImageField(null=True, verbose_name=_('Cover'))
    imdb_score = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)],
                                     verbose_name=_('Score'))
    tags = TaggableManager()
    publish_year = models.IntegerField(null=True, verbose_name=_('Year'))

    def __str__(self):
        return self.title

    def get_tags(self):
        return self.tags.names()    
