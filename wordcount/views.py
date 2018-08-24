from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split(" ")

    wordcountdic = {}

    for word in wordlist:
        if word in wordcountdic:
            #Incerease
            wordcountdic[word] += 1
        else:
            #add to the dictionary
            wordcountdic[word]=1

    sortedwords = sorted(wordcountdic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist),'sortedwords':sortedwords} )

def profile(request):
    return render(request, 'profile.html')
