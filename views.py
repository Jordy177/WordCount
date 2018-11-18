# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()

    worddictionary = {}

    for word in words:
        if word in worddictionary:
            # Increase
            worddictionary[word] += 1
        else:
            # Add to the dictionary
            worddictionary[word] = 1

    return render(request, 'count.html',
                  {'fulltext': fulltext, 'count': len(words), 'worddictionary': worddictionary.items()})


def about(request):
    return render(request, 'about.html')