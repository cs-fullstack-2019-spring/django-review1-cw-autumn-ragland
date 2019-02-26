from django.urls import path
from . import views

# paths that triggers functions in views/are called in html files
urlpatterns = [
    path('', views.index, name='index'),
    path('page2', views.two, name='page2'),
    path('page3', views.three, name='page3'),
    path('page4', views.four, name='page4'),
    path('page5', views.five, name='page5'),
    path('drinks', views.cocktails, name='drinks'),
    path('details/<int:drinkID>', views.details, name='details'),
]
