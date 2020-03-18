from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Articles

# Create your views here.

def home(request):
	context = {}
	articles = Articles.objects.all()
	context['articles'] = articles
	return render(request, 'main/home.html', context)


def uploadArticle(request):
	context = {}

	if request.method == 'POST':
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')

	form = ArticleForm()
	context['form'] = form
	return render(request, 'main/upload_article.html', context)

def articles(request):
	id = request.GET['id']
	article = Articles.objects.get(id=id)
	print("this is the title : " + article.title)

	return render(request, 'main/article.html', {'article': article})
