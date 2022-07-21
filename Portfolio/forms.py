from django import forms
from django.forms import ModelForm
from django.conf import settings
from django.core.mail import send_mail
from .models import ContactModel, UploadModel

class ContactForm(ModelForm):
	"""docstring for ContactForm"""
	name = forms.CharField(max_length=100,
       widget= forms.TextInput
       (attrs={'class':'some_class',
			'id':'name',
			'placeholder':'Your name...'}))
	email = forms.CharField(max_length=100,
       widget= forms.TextInput
       (attrs={'class':'some_class',
		'id':'email',
		'placeholder':'Your email...'}))
	subject = forms.CharField(max_length=100,
       widget= forms.TextInput
       (attrs={'class':'some_class',
       	'id':'subject',
       	'placeholder':'Subject...'}))
	message = forms.CharField(max_length=1000,
		widget=forms.Textarea
		(attrs={'class':'form-control',
		 'id':'message',
		 'placeholder':'Your message...',
		 'rows':'6'}))

	class Meta:
		model = ContactModel
		fields = '__all__'

	def get_info(self):
		# cleaned data
		cl_data = super().clean()

		name = cl_data.get('name').strip()
		from_email = cl_data.get('email')
		subject = cl_data.get('subject')

		msg = f'{name} with email {from_email} said:'
		msg += f'\n"{subject}"\n\n'
		msg += cl_data.get('message')

		return subject, msg

	def send(self):
		subject, msg = self.get_info()
		send_mail(
			subject=subject,
			message=msg,
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[settings.EMAIL_RECIPIENT],
			fail_silently=True,
		)
class UploadForm(ModelForm):
	class Meta:
		# To specify the model to be used to create form  
		models = UploadModel
		# It includes all the fields of model  
		fields = '__all__'  