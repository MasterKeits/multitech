# -*- coding: utf-8 -*-
from django.db import models
from PIL import Image
from io import BytesIO
from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Category(models.Model):
	title = models.CharField(max_length=70)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class SubCategory(models.Model):
	title = models.CharField(max_length=70)
	created = models.DateTimeField(auto_now_add=True)
	# product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)

	def __str__(self):
		return self.title


class Product(models.Model):
	title = models.CharField(max_length=70)
	description = RichTextField(blank=True, editable=True)
	created = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to="sales/images/", blank=True, editable=True)
	sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True)

	def __str__(self):
		return self.title

		def save(self):
			im = Image.open(self.image)
			output = BytesIO()
			im = im.resize((800, 800))
			im.save(output, format='JPEG', quality=100)
			output.seek(0)
			self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
			super(Product, self).save()
