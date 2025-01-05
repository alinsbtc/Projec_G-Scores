from django.urls import path , include
from .import views
urlpatterns = [
       path('', views.index, name='index'),
       path('search/', views.search_scores, name='search_scores'),
       path('report/', views.report, name='report'),

]
