from django.urls import path
from . import views
urlpatterns = [
	path('mysite/polls/', views.index, name='index'),
]
