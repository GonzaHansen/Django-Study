from django.shortcuts import render
from django.http import HttpResponse 
from .models import Post #Importamos el modelo del post para conmseguir la info
# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()  #Si usamos dummies antes es importante que al usar los modelos las llaves sean iguales
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About!'})