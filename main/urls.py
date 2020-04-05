from django.urls import path
from main import views

urlpatterns = [
		path('', views.home, name='home'),
		path('articles/', views.articles, name='articles'),
		path('career_all/', views.career, name='career'),
		path('campus_all/', views.campus, name='campus'),
]