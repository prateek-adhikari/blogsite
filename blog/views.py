from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.
class HomePageView(ListView):
   model = Post
   template_name = 'blog/home.html'
   paginate_by = 6

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' 

def about(request):
   return render(request, 'blog/about.html')

def contact(request):
   return render(request, 'blog/contact.html')