# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Contact(models.Model):
	contact_name = models.CharField(max_length=50, blank=False, null=True)
	contact_position = models.CharField(max_length=50, blank=False, null=True)
	contact_phone = models.CharField(max_length=24, blank=True, null=True)
	contact_email = models.CharField(max_length=50, blank=True, null=True)
	contact_image = models.ImageField(upload_to="contact/images/", null=True, blank=True, editable=True)
	created = models.DateTimeField(auto_now_add=True, blank=True)

	def save(self):
		im = Image.open(self.contact_image)
		output = BytesIO()
		im = im.resize((800, 800))
		im.save(output, format='JPEG', quality=100)
		output.seek(0)
		self.contact_image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.contact_image.name.split('.')[0], 'contact_image/jpeg', sys.getsizeof(output), None)
		super(Contact, self).save()

	def __str__(self):
			return self.contact_name
