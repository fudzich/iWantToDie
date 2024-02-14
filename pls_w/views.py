from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from pls_w.forms import articleForm, loginForm, registerForm
from pls_w.models import Article, Employee, Game, Genre


def show_articles(request):
    articles = list(Article.objects.all())
    return render(request, 'articles.html', {"articles": articles})

def add_article(request):
    if request.method == 'GET':
        form = articleForm()
        return render(request, "templateForm.html", {"form":form})
    else:
        form = articleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect(show_articles)
        else:
            print(form.errors)
            pass

def acc_info(request):
    user = request.user
    if user.is_authenticated:
        username = user.username
        return render(request, 'accS.html', {'username': username})
    else:
        return render(request, 'accNoS.html')
def register_user(request):
    if request.method == 'GET':
        form = loginForm()
        return render(request, "registerForm.html", {"form":form})
    else:
        if (request.POST.get('username') != '' and request.POST.get('password') != ''):
            username = request.POST["login"]
            password = request.POST["password"]
            print(username + " " + password)
            user = User.objects.create_user(username=username, password=password)
            print(username + " " + password)
            login(request, user)
            return redirect(acc_info)
        else:
            return redirect(acc_info)
def login_user(request):
    if request.method == 'GET':
        form = loginForm()
        return render(request, "loginForm.html", {"form":form})
    else:
        if (request.POST.get('login') != '' and request.POST.get('password') != ''):
            username = request.POST["login"]
            password = request.POST["password"]
            print(username+" "+password)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect(acc_info)
        else:
            return redirect(acc_info)


def show_games(request):
    genres = list(Genre.objects.all())
    return render(request, "showGames.html", {"genres": genres})


def show_games_by(request, genre_title):
    games = list(Game.objects.all())
    return render(request, "gamesByGenre.html", {"games": games, "genre_title": genre_title})


def delete_article(request, article_id):
    if Article.objects.filter(id=article_id).exists():
        ad = Article.objects.get(id=article_id)
        ad.delete()
        return render(request, "deleteArticle.html", {"id": article_id})
    else:
        return render(request, "noArticle.html")
# Create your views here.
