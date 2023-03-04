from django.shortcuts import render
from .models import Category,News

def show_news(request):
    all_news=News.objects.all()
    return render(request,'blog/show_news.html',{'all_news':all_news})


def new_detail(request, pk):
    one_new = News.objects.get(pk=pk)
    print(one_new)
    return render(request, 'blog/new_detail.html', {'one_new' : one_new})