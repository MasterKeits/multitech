from django.urls import path
# from django.contrib import admin
# from django.views.generic import TemplateView
from . import views

app_name = 'home'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('autos', views.AutosView.as_view(), name='about'),
	path('contact', views.ContactView.as_view(), name='contact'),
	path('forklift', views.ForkLiftView.as_view(), name='reference'),
]
