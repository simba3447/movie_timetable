from django.shortcuts import render
from movie.utils import *

# Create your views here.
from django.views.generic import TemplateView


class MovieListView(TemplateView):
    template_name = 'movieList.html'

    def get(self, request, *args, **kwargs):
        response = create_response(request)
        response['movies'] = parse_movies()
        return render(request, self.template_name, response)
