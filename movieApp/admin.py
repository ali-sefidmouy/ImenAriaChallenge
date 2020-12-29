from django.contrib import admin
from . import models


@admin.register(models.Movie)
class Movie(admin.ModelAdmin):
    list_display = ('title', 'storyline', 'cover_image', 'imdb_score', 'tags', 'publish_year')
    ordering = ('-imdb_score', )
    list_filter = ('tags', 'imdb_score', )
    search_fields = ('title',)
