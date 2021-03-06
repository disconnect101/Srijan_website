from django.urls import path
from main import views

urlpatterns = [
		path('', views.home, name='home'),
		path('articles/', views.articles, name='articles'),
		path('upload/', views.uploadArticle, name='uploadarticle'),
		path('comment/', views.comment, name='comment'),
		path('career_all/', views.career, name='career'),
		path('campus_all/', views.campus, name='campus'),
		path('sos_all/', views.sos, name='sos'),
		path('show_pub/', views.publication, name='publications'),
		path('view_pub/', views.viewPublication, name='view_publication'),
		path('comment_upload/', views.comment, name='comment_upload')
]