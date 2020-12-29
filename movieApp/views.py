from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import MovieSerializer
from .models import Movie

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer

    # @api_view(["DELETE"])
    # def delete_movie(request, movie_id):
    #     Movie.objects.get(id=movie_id).delete()
    #     return Response()   

