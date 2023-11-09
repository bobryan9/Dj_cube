from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

menu = [{'title': 'Главная', 'url_n': 'women'},
{'title': 'Школа', 'url_n': 'school'},
{'title': 'Лагерь', 'url_n': 'camp'},
{'title': 'Тренажёрный зал', 'url_n': 'gym'},
{'title': 'Стадион', 'url_n': 'stadium'},
]

def index(request):
    t = render_to_string('women/index.html')
    return HttpResponse(t)

def school(request): # HttpRequest
    t2 = render_to_string('women/school.html')
    return HttpResponse(t2)

def camp(request): # HttpRequest
    return HttpResponse('это мой лагерь <img height=100% width=100% src= "https://тур63.рф/wp-content/uploads/2019/06/administrator-1.jpg">')

def gym(request): # HttpRequest
    return HttpResponse('это мой спортивный зал <img src= "https://sportishka.com/uploads/posts/2022-11/1667566300_35-sportishka-com-p-trenazheri-v-trenazhernom-zale-vkontakte-39.jpg">')

def stadium(request): # HttpRequest
    return HttpResponse('это мой стадион <img src= "http://sd-expert.ru/img/13081947.jpg">')

def categories(request, cat_id):
    if cat_id == 1:
        return HttpResponse('<h1>№1 Доберман</h1> <img  weight = 1280 height = 900 src= "https://catherineasquithgallery.com/uploads/posts/2021-02/1612283953_153-p-doberman-na-fioletovom-fone-194.jpg">')
