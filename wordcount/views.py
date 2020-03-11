from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('Hello')
    return render(request, 'home.html')

def count(request):
    full_text = request.GET['fulltext']
    print(full_text)
    word_list = full_text.split()
    count_words = len(word_list)
    worddictionary ={}
    for word in word_list:
        if word not in worddictionary.keys():
            worddictionary[word] = 1
        else:
            worddictionary[word] += 1
    print(worddictionary)
    return render(request,'count.html',{'fulltext':full_text,'Count':count_words,'worddictionary':worddictionary.items()})

def about(request):
    return render(request, 'about.html')