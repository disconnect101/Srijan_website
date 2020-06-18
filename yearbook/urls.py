from django.urls import path
from yearbook import views

urlpatterns = [
    path('', views.home, name='yearbook'),
    path('list/', views.yearlist, name='yearlist'),
    path('alumni/', views.alumni, name='alumni'),
    path('upload/', views.uploadData, name='upload'),
    path('images_api/', views.images_api, name='images_api')
]