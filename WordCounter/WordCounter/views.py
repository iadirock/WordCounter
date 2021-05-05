from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def counter(request):
    textbox = request.GET['textbox']
    
    countlist = textbox.split()

    wordDictionary = {}

    for word in countlist:
        if word in  wordDictionary:
            #Increase the count
            wordDictionary[word] += 1
        else:
            #Set to 1
            wordDictionary[word] = 1

    sortedwords = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, 'counter.html', {'textbox':textbox, 'counts':len(countlist), 'sortedwords':sortedwords})