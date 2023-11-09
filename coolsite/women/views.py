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
    return render(request,'women/index.html', {'menu': menu})


def school(request): # HttpRequest
    return render(request,'women/school.html', {'menu': menu})
def camp(request): # HttpRequest
    return render(request,'women/camp.html', {'menu': menu})

def gym(request): # HttpRequest
    return render(request,'women/gym.html', {'menu': menu})

def stadium(request): # HttpRequest
    return render(request,'women/stadium.html', {'menu': menu})

def categories(request, cat_id):
    if cat_id == 1:
        return HttpResponse('<h1>№1 Доберман</h1> <img  weight = 1280 height = 900 src= "https://catherineasquithgallery.com/uploads/posts/2021-02/1612283953_153-p-doberman-na-fioletovom-fone-194.jpg">')
