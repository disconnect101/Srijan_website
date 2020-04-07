from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Articles, Comment
from django.http import JsonResponse

# Create your views here.

def home(request):
	context = {}

	campus_articles = Articles.objects.filter(category__in=['cmp']).order_by('-date')
	career_articles = Articles.objects.filter(category__in=['intd', 'compe', 'als']).order_by('-date')
	sos_articles = Articles.objects.filter(category__in=['sos']).order_by('-date')
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
	comments = Comment.objects.filter(article_id=id)
	article = Articles.objects.get(id=id)
	recentarticles = Articles.objects.order_by('-date')[:6]
	all_articles_images = Articles.objects.order_by('date')[:8]

	print("this is the title : " + article.title)
	#article = []
	#recentarticles = []

	return render(request, 'main/template_blog.html' , {'article': article, 'recentarticles': recentarticles, 'all_articles_images': all_articles_images, 'comments': comments })


def career(request):
	articles = Articles.objects.filter(category__in=['intd', 'compe', 'als']).order_by('-date')
	recentarticles = Articles.objects.order_by('-date')[:6]
	all_articles_images = Articles.objects.order_by('date')[:8]
	return render(request, 'main/career.html', {'articles': articles, 'recentarticles': recentarticles, 'all_articles_images': all_articles_images})

def campus(request):
	articles = Articles.objects.filter(category__in=['cmp']).order_by('-date')
	recentarticles = Articles.objects.order_by('-date')[:6]
	all_articles_images = Articles.objects.order_by('date')[:8]
	return render(request, 'main/campus.html', {'articles': articles, 'recentarticles': recentarticles, 'all_articles_images': all_articles_images})

def comment(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		ajaxresponse = request.POST
		if form.is_valid():
			form.save()
			return JsonResponse(ajaxresponse)

