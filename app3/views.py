from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'app3/home.html')

def pagina2(request):
	return render(request, 'app3/pagina 2.html')
	
def inputs(request):
	return render(request, 'app3/inputs.html')