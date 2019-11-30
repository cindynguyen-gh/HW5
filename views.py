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
    print(repos)
    context = {
        'repos': repos,
    }
    return render(request, 'content/projects.html', context)

def contact(request):
    context = {
    }
    return render(request, 'content/contact.html', context)



