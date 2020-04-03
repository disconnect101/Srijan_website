from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Articles

# Create your views here.

def home(request):
	context = {}

	campus_articles = Articles.objects.filter(category__in=['cmp'])
	career_articles = Articles.objects.filter(category__in=['intd', 'compe', 'als'])
	sos_articles = Articles.objects.filter(category__in=['sos'])
	all_articles = Articles.objects.all()

	context['articles'] = all_articles
	context['career_articles'] = career_articles
	context['campus_articles'] = campus_articles
	context['sos_articles'] = sos_articles

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
	recentarticles = Articles.objects.order_by('-date')[:6]
	print("this is the title : " + article.title)

	return render(request, 'main/article.html', {'article': article, 'recentarticles': recentarticles})
