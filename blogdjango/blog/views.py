from django.shortcuts import render, redirect,get_object_or_404
from .models import Category, News
from .forms import NewsForm


def show_category(request, pk):
    news = News.objects.filter(pk=pk)
    all_category = Category.objects.all()
    return render(request, 'blog/show_category.html', {'all_category' : all_category,
                                                       'newss' : news})


def show_news(request):
    all_news = News.objects.all()
    return render(request, 'blog/show_news.html', {'all_news' : all_news})


def new_detail(request, pk):
    one_new = News.objects.get(pk=pk)
    print(one_new)
    return render(request, 'blog/new_detail.html', {'one_new' : one_new})


def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            img_obj = form.instance
            return render(request, 'blog/create_news.html', {'form' : form, 'img_obj' : img_obj})
    else:
        form = NewsForm()
    return render(request, 'blog/create_news.html', {'form':form})

def update_news(request,pk):
    news = News.objects.get(pk=pk)
    news_category = News.objects.all()
    if request.method == "POST":
        news.title = request.POST['title']
        news.content = request.POST['content']
        news.category__pk = request.POST['category']
        try:
            news.image = request.FILES['image']
        except:
            news.image = news.image
        news.save()
        return redirect('/')
    return render(request,'blog/update_news.html',{'news': news, 'news_category' : news_category,})


def delete_news(request,pk):
    news = News.objects.get(pk=pk)
    news.delete()
    return redirect('/')


