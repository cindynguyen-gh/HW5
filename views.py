import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
    }
    return render(request, 'content/index.html', context)


def projects(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    response = requests.get('https://api.github.com/users/cindynguyen-gh/repos')
    repos = response.json()
    images=["/static/img/project/dandelion.jpg", "/static/img/project/drop.jpg", "/static/img/project/elephnatjpg.jpg","/static/img/project/italy.jpg","/static/img/project/nature.jpg"  ]
    context = {
        'repos': repos,
        'images': images,
    }
    return render(request, 'content/projects.html', context)

def contact(request):
    context = {
    }
    return render(request, 'content/contact.html', context)



