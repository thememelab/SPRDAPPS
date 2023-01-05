from django.shortcuts import render
from datetime import datetime
from .models import Article
from django.http import HttpResponse



def get_article():
    results = Article.objects.all()
    return results

def populate_db():
        if Article.objects.count() == 0:
            testArticle1 = Article(tittle = 'First Article', content = 'this is the  first article')
            testArticle1.save()
            
def index(request):
    context = {
        'current_date':datetime.now(),
        'tittle':'Home'
    }
    return render(request,"index.html", context)

def about(request):
    context = {
        'current_date':datetime.now(),
        'tittle':'About'
    }
    return render(request,"about.html", context)

def news(request):
    if(request.POST):
        _method = request.POST.get('_method')
        tittle = request.POST.get("articleTittle")
        content = request.POST.get("articleContent")
        
        if _method == "add_method":
            newArticle = Article(tittle=tittle, content = content)
            newArticle.save()
            print(newArticle)
            return HttpResponse("New Article  has been added to databases "+newArticle.tittle)

        else :
            instance = Article.objects.get(id=_method)
            instance.delete()
            print("Article deleted")


        
            

    populate_db()
    articles = get_article()
    context = {
        'current_date':datetime.now(),
        'tittle':'News',
        'articles' : articles
    }
    return render(request,"news.html", context)
       



