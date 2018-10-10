from django.http import HttpResponse
from django.shortcuts import render
import operator

def student1(request):
    return render(request,"home.html")

def student2(request):
    return HttpResponse("this is first website")

def count(request):
    data=request.GET['fulltextarea']
    split_data=data.split()

    length_data=len(split_data)

    word_dictinary = {}

    for word in split_data:
        if word in word_dictinary:
            word_dictinary[word] +=1
        else:
            word_dictinary[word] = 1

    sorted_list = sorted(word_dictinary.items(), key = operator.itemgetter(1),reverse=True)



    return render(request,"count.html",{'data1':data,'length1':length_data,'word1':sorted_list} )


def about(request):
    return render(request,"about.html")
