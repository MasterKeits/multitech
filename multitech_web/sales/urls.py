from django.urls import path

from . import views

app_name = 'sales'
urlpatterns = [
	path('', views.CategoryListView.as_view(), name='index'),
	path('<int:pk>/category', views.CategoryDetailView.as_view(), name='subcat'),
	path('category/<int:pk>/sub', views.SubCategoryDetailView.as_view(), name='detail'),
	path('<int:pk>/sub/product/', views.ProductDetailView.as_view(), name='product'),
]
