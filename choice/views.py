from django.shortcuts import render
from kinopoisk_dev import KinopoiskDev
TOKEN = 'T7K3C7Q-TADMC7N-M265A8X-DB5RR3X'

def index(request):
    if request.method == 'POST':
        kp = KinopoiskDev(token=TOKEN)
        item = kp.random()
        actors = []
        genr = []

        for i in item.persons:
            if i == None:
                pass
            else:
                actors.append(i.name)

        for j in item.genres:
            if j == None:
                pass
            else:
                genr.append(j.name)
        context = {
            'actors' : actors[:5],
            'genres' : genr,
            'name' : item.name,
            'description' : item.description,
            'image' : item.poster.url,
            'item' : True
        }
    else:
        context = {
            'a' : 'c'
        }
    return render(request, 'index.html', context)
