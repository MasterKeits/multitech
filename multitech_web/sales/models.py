# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from PIL import Image
from io import BytesIO
from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Category(models.Model):
	name = models.CharField(max_length=50, blank=False, null=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class SubCategory(models.Model):
	name = models.CharField(max_length=50, blank=False, null=True)
	created = models.DateTimeField(auto_now_add=True)
	parent_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=50, blank=False, null=True)
	content = RichTextField(null=True, blank=True, editable=True)
	image = models.ImageField(upload_to="product/images/", null=True, blank=True, editable=True)
	sub_category = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	def save(self):
		if self.image:
			im = Image.open(self.image)
			output = BytesIO()
			im = im.resize((800, 600))
			im.save(output, format='JPEG', quality=100)
			output.seek(0)
			self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		super(Product, self).save()

	def __str__(self):
		return self.name
