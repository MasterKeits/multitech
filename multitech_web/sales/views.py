# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from .models import Category, Product, SubCategory

# Create your views here.


class CategoryView(generic.ListView):
	model = Category
	paginate_by = 4
	template_name = 'sales/index.html'
	context_object_name = 'category_list'

	def get_queryset(self):
		return Category.objects.order_by('-created')


class SubCategoryView(generic.DetailView):
	model = SubCategory
	paginate_by = 4
	template_name = 'sales/subcat.html'
	context_object_name = 'subcategory_list'

	def get_queryset(self):
		return Category.objects.order_by('-created')


class ProductView(generic.DetailView):
	model = Product
	template_name = 'sales/detail.html'
