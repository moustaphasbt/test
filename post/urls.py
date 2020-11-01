from django.urls import path

from . import views

urlpatterns = [
    path('', views.articles, name="articles"),
    path('delete/<int:id>/', views.delete_article, name="delete_article"),
    path('show/<int:id>/', views.detail_article, name="detail_article"),
]
