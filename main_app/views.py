from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  # SELECT * FROM 'main_app_cat';
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats': cats})

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', {'cat': cat})