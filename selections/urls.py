from django.urls import path
from . import views

app_name='selections'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # path('select/', views.select, name='select')
    
]