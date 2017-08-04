import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def create_response(request):
    return dict(
        user=request.user,
        message=request.GET.get('message'),
        success=request.GET.get('success'),
        warning=request.GET.get('warning'),
        error=request.GET.get('error'),
    )


def parse_movies():
    html_doc = urllib.request.urlopen('http://movie.daum.net/premovie/released')
    soup = BeautifulSoup(html_doc, 'html.parser')

    # 영화 리스트 가져오기
    movies = soup.find_all(class_='lazy thumb_photo')

    # 영화 타이틀, 포스터 딕셔너리
    movie_list = {}
    for i in range(20):
        movie_list[movies[i]['alt']] = urlparse(movies[i]['data-original'])[4][6:]
    return movie_list
