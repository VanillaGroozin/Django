from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from news.models import News, Tag
from news.forms import NewsForm

def index(request):
    return render(request, 'index.html')

def news(request):
    tags = Tag.objects.all()
    news = News.objects.filter(status = 'pub')
    return render(request, 'news/news.html', {'news':news, 'tags': tags})


def create(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    form = NewsForm()
    return render(request, 'news/create.html', {'form': form})

def news_filter(request, slug):
    tag_slug = Tag.objects.get(slug=slug)
    news = tag_slug.news_set.all()
    context = {
        'news': news,
        'tags': Tag.objects.all()
    }
    return render(request, 'news/news.html', context=context)

def news_show(reqeust, id):
    news = News.objects.get(pk=id)
    return render(reqeust, 'news/show.html', {'news':news})
