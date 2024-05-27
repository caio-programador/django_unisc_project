from django.urls import path

from appteste import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste/<int:id>/', views.teste, name='teste'), # urls dinâmicas get com id
]