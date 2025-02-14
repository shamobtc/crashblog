from django.urls import path
from .views import frontpage, about, robots_txt

app_name = 'core'
urlpatterns = [
	path('robots_txt', robots_txt, name='robots_txt'),
	path('about/', about, name='about'),
	path('', frontpage, name='frontpage'),
]