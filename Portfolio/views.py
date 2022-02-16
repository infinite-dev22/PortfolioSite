from django.shortcuts import render, redirect
from .forms import ContactForm

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
