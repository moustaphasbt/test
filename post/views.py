from django.shortcuts import render, redirect
from .models import Article, Comment


def articles(request):
    if(request.method == "POST"):
        article = Article(
            title=request.POST["title"], content=request.POST["content"])
        article.save()

    articles = Article.objects.all()
    return render(request, "post/articles.html", {'articles': articles})


def detail_article(request, id):
    article = Article.objects.get(pk=id)
    if(request.method == "POST"):
        pass
        # comment = Comment(content=request.POST["content"])
        # comment.save()
        # article.comments.add(comment)
        # article.save()
    return render(request, "post/articles_detail.html", {'article': article})


def delete_article(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return redirect("/")
