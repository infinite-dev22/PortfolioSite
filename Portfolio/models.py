from django.db import models

# Create your models here.
class ContactModel(models.Model):
	name = models.CharField(max_length=120, default='')
	email = models.EmailField(default='')
	subject = models.CharField(max_length=70, default='')
	message = models.CharField(max_length=1000, default='')

	def __str__(self):
		return self.name

class UploadModel(models.Model):
	image = models.ImageField(upload_to='images')
	title = models.CharField(max_length=120, default='')
	about = models.CharField(max_length=220, default='')

	def __str__(self):
		return self.name
