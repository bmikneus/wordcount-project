from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordcount = {}
    maxCount = 0
    maxWord = ""
    for word in wordlist:
        if wordcount.get(word) is None:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
        if wordcount[word] > maxCount:
            maxCount = wordcount[word]
            maxWord = word
    sortedwords = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext, 'length':len(wordlist),'maxWord':maxWord,'maxCount':maxCount, 'sortedwords':sortedwords})

def about(request):
    name = "Brandon Mikneus"
    state = "Texas"
    thingsilike = ["Hana", "Bunny", "Hana and Bunny", "Mr. Rogers"]
    return render(request, 'about.html', {'name':name, 'state':state,'thingsilike':thingsilike})