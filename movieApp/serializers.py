from rest_framework import serializers

from .models import Movie


class TagsField(serializers.Field):
    """ custom field to serialize/deserialize TaggableManager instances.
    """
    def to_representation(self, value):
        """ in drf this method is called to convert a custom datatype into a primitive,
        serializable datatype.

        In this context, value is a plain django queryset containing a list of strings.
        This queryset is obtained thanks to get_tags() method on the Movie model.

        Drf is able to serialize a queryset, hence we simply return it without doing nothing.
        """
        return value

    def to_internal_value(self, data):
        """ this method is called to restore a primitive datatype into its internal
        python representation.

        This method should raise a serializers.ValidationError if the data is invalid.
        """
        return data



class MovieSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagsField(source="get_tags")

    def create(self, validated_data):
        tags = validated_data.pop("get_tags")
        movie = Movie.objects.create(**validated_data)
        movie.tags.add(*tags)

        return movie

    class Meta:
        model = Movie
        fields = ('id', 'title', 'storyline', 'imdb_score', 'tags', 'publish_year')
