from django.urls import path

from . import views

app_name = 'sales'
urlpatterns = [
	path('', views.CategoryView.as_view(), name='index'),
	path('<int:pk>/', views.ProductView.as_view(), name='detail'),
	# path('<int:pk>/', views.SubCategoryView.as_view(), name='subcat'),
]
