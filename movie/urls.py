from django.conf.urls import url
from movie.views import MovieListView

urlpatterns = [
    url(r'^movies$', MovieListView.as_view(), name='movie_list')
]
