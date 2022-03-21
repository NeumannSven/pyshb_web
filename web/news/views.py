from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def main(request):
    return HttpResponse("<h1>Hallo Welt</h1>")


def showArticles(request):
    nachricht = f""
    for item in Article.objects.all():
        nachricht += f'<h1 style="background:yellow">{item.title}</h1><p>{item.date}</p> \
                        <h2 style="color:blue">{item.subtitle}</h2> \
                        <p style="background:lightgray">{item.text}</p></br>'
    return HttpResponse(nachricht)


def showWebSite(request):
    context = {'news': Article.objects.all()}
    return render(request=request, template_name='news/index.html', context=context)
