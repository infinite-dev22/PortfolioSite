from django.shortcuts import render, redirect
from .forms import ContactForm, UploadForm

# Create your views here.
def indexView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		# print(form)
		if form.is_valid():
			form.send()
			# print('\t\t\t\t\nemail sent')
			return redirect('successful/')
	else:
		form = ContactForm()
		print('\t\t\t\t\t\nemail not sent')
	return render(request, "Portfolio/index.html", {'form': form})

def successView(request):
	return render(request, "Portfolio/success.html", {})

def imageUploadView(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.send()
			form = ContactForm()
			print('\t\t\t\t\t\nRequest Successful')
	else:
		form = ContactForm()
		print('\t\t\t\t\t\nRequest Not Successful')
	return render(request, "Portfolio/upload.html", {'form': form})
