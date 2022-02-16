from django.db import models

# Create your models here.
class ContactModel(models.Model):
	name = models.CharField(max_length=120, default='')
	email = models.EmailField(default='')
	subject = models.CharField(max_length=70, default='')
	message = models.CharField(max_length=1000, default='')

	def __str__(self):
		return self.name
